import string
import random

import xlsxwriter

from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.medicament import Medicament
from Domain.medicament_validator import Medicament_validator
from Domain.update_operation import UpdateOperation
from Repository.file_repository import FileRepository
from Service.merge_sort import mergeSort
from Service.sorted import my_sorted
from Service.undoredo_service import UndoRedoService


class Medicament_service:
    def __init__(self,medicament_repository: FileRepository,
                 medicament_validator: Medicament_validator,
                 tranzactie_repository: FileRepository,
                 undo_redo_service: UndoRedoService):
        self.__medicament_repository = medicament_repository
        self.__medicament_validator = medicament_validator
        self.__tranzactie_repository = tranzactie_repository
        self.__undo_redo_service = undo_redo_service






    def create(self, id_medicament, nume, producator, pret, reteta):
        '''
        creeaza un medicament
        :param id_medicament:id ul medicamentului
        :param nume: numele medicamentului
        :param producator: producatorul
        :param pret: pretul
        :param reteta: reteta
        :return:
        '''
        medicament = Medicament(id_medicament, nume, producator, pret, reteta)

        self.__medicament_validator.validate(medicament)


        if reteta == 'da':
            medicament.reteta = True
        else:
            medicament.reteta = False

        self.__medicament_repository.create(medicament)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__medicament_repository, medicament))
        self.__undo_redo_service.clear_redo()






    def delete(self, id_medicament):
        '''
        sterge un medicament dupa id ul dat
        :param id_medicament: id ul medicamentului de sters
        :return:
        '''
        obiect = self.__medicament_repository.find_by_id(id_medicament)
        self.__medicament_repository.delete(id_medicament)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__medicament_repository, obiect))
        self.__undo_redo_service.clear_redo()

    def update(self, id_medicament, nume, producator, pret, reteta):
        '''
        updateaza un medicament
        :param id_medicament:
        :param nume:
        :param producator:
        :param pret:
        :param reteta:
        :return:
        '''
        medicament = self.__medicament_repository.find_by_id(id_medicament)
        medicament_before_update = medicament
        if medicament is None:
            raise KeyError(f'Medicamentul cu id-ul {id_medicament} nu exista!')

        if nume != '':
            medicament.nume = nume

        if producator != '':
            medicament.producator = producator

        if pret != '':
            medicament.pret = pret

        if reteta != '':
            medicament.reteta = reteta

        if reteta == 'da':
            medicament.reteta = True

        self.__medicament_validator.validate(medicament)
        if reteta == 'da' or reteta == '':
            medicament.reteta = True
        else:
            medicament.reteta = False

        self.__medicament_repository.update(medicament)
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__medicament_repository, medicament, medicament_before_update))
        self.__undo_redo_service.clear_redo()

    def get_all(self):
        return self.__medicament_repository.get_all()


    def get_by_anything(self, t):
        '''
        returneaza entitatea gasita dupa stringul dat
        :param t: stringul dat
        :return: medicamentul gasit dupa stringul citit
        '''
        medicamente = self.__medicament_repository.get_all()

        for medicament in medicamente:
            if medicament.pret == str(t):
                return medicament
            if medicament.reteta == str(t):
                return medicament
            if medicament.producator == str(t):
                return medicament
            if medicament.nume == str(t):
                return medicament
        return None

    def random_medicament(self):
        def random_string(length):
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(length))
            return result_str

        medicament = Medicament(random.randint(1,99999),random_string(5), random_string(6), random.uniform(1,999),random.randint(0,1))
        try:
            self.__medicament_repository.create(medicament)
        except KeyError:
            self.random_medicament()


    def scumpire(self, procentaj, valoare):
        '''
        realizeaza o scumpire a medicamentelor cu procentajul citit daca pretul este mai mic decat valoarea data.
        :param procentaj:
        :param valoare:
        :return:
        '''
        medicamente = self.__medicament_repository.get_all()
        for medicament in medicamente:
            if medicament.pret < float(valoare):
                medicament.pret = medicament.pret + (int(procentaj) / 100) * medicament.pret
                self.__medicament_repository.update(medicament)



    def afisare_medicamente_nr_tranzactii(self):
        

        def nr_tranzactii(medicament):
            
            nr = 0
            tranzactii = self.__tranzactie_repository.get_all()
            for tranzactie in tranzactii:
                if tranzactie.id_medicament == medicament.id_entity:
                    nr += 1
            return nr


        medicamente = self.__medicament_repository.get_all()

        my_sorted(medicamente, lambda x, y: nr_tranzactii(x) < nr_tranzactii(y), reverse= True)
        return medicamente



    def export(self):
        '''
        export tuturor medicamentelor intr un tabel excel
        :return:
        '''

        workbook = xlsxwriter.Workbook('Example2.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0
        column = 0
        medicament_repository = FileRepository('medicament.txt')
        content = []

        for i in medicament_repository.get_all():
            content.append(i.id_entity)

        for item in content:
            worksheet.write("A1", "Id medicament")
            worksheet.write("B1", "nume")
            worksheet.write("C1", "producator")
            worksheet.write("D1", "pret")
            worksheet.write("E1", "reteta")
            row = row + 1

        content2 = []

        for i in medicament_repository.get_all():
            content2.append([i.id_entity, i.nume, i.producator, i.pret, i.reteta])
        row = 1


        for id, nume, producator, pret, reteta in content2:
            worksheet.write(row, column, id)

            worksheet.write(row, column + 1, nume)

            worksheet.write(row, column + 2, producator)

            worksheet.write(row, column + 3, pret)

            worksheet.write(row, column + 4, reteta)
            row += 1

        workbook.close()


    def afisare_medicamente_merge_sort(self):
        '''
        ordoneaza printr un mergesort medicamentele
        :return: lista de medicamente ordonate
        '''

        def nr_tranzactii(medicament):

            nr = 0
            tranzactii = self.__tranzactie_repository.get_all()
            for tranzactie in tranzactii:
                if tranzactie.id_medicament == medicament.id_entity:
                    nr += 1
            return nr
        medicamente = self.__medicament_repository.get_all()
        return list(mergeSort(medicamente, key=nr_tranzactii, reverse = True))


