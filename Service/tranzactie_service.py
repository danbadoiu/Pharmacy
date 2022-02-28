
from datetime import datetime

from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.tranzactie import Tranzactie
from Domain.update_operation import UpdateOperation
from Repository.file_repository  import FileRepository
from Service.undoredo_service import UndoRedoService
from ViewModels.tranzactie_viewmodel import TranzactieViewModel


class Tranzactie_service:
    def __init__(self, tranzactie_repository: FileRepository,
                 medicament_repository: FileRepository,
                 card_client_repository: FileRepository,
                 undo_redo_service: UndoRedoService):
        self.__tranzactie_repository = tranzactie_repository
        self.__medicament_repository = medicament_repository
        self.__card_client_repository = card_client_repository
        self.__undo_redo_service = undo_redo_service


    def create(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data_si_ora):
        '''
        creeaza o tranzactie
        :param id_tranzactie: id tranzactie
        :param id_medicament:id ul medicamentului
        :param id_card_client: id ul cardului
        :param nr_bucati: nr de bucati
        :param data_si_ora: data  si ora

        :return:
        '''
        reducere = 0
        tranzactie = Tranzactie(id_tranzactie, id_medicament, id_card_client, nr_bucati, data_si_ora)

        if self.__card_client_repository.find_by_id(id_card_client) is None:
            raise KeyError(f'Nu exista cardul cu id-ul: {id_card_client}!')
        if self.__medicament_repository.find_by_id(id_medicament) is None:
            raise KeyError(f'Nu exista medicamentul cu id-ul: {id_medicament}!')


        day, month, year, hour, minutes = data_si_ora.split('/')

        tranzactie.data_si_ora = datetime(int(year), int(month), int(day), int(hour), int(minutes))



        medicament = self.__medicament_repository.find_by_id(tranzactie.id_medicament)
        card_client = self.__card_client_repository.find_by_id(tranzactie.id_card_client)
        self.__tranzactie_repository.create(tranzactie)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__tranzactie_repository, tranzactie))
        self.__undo_redo_service.clear_redo()


        if card_client is not None:
            if medicament.reteta == False:

                medicament.pret = medicament.pret - (10 / 100) * medicament.pret
                reducere = (10 / 100) * medicament.pret


            else:


                medicament.pret = medicament.pret - (15 / 100) * medicament.pret
                reducere = (15 / 100) * medicament.pret


        return reducere



    def delete(self, id_tranzactie):
        '''
        sterge o tranzactie dupa id ul dat
        :param id_tranzactie:
        :return:
        '''
        obiect = self.__tranzactie_repository.find_by_id(id_tranzactie)
        self.__tranzactie_repository.delete(id_tranzactie)

        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__tranzactie_repository, obiect))
        self.__undo_redo_service.clear_redo()

    def update(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data_si_ora):
        '''
        updateaza o tranzactie
        :param id_tranzactie: idul tranzactiei
        :param id_medicament:id ul medicamentului
        :param id_card_client: id ul cardului
        :param nr_bucati: nr de bucati
        :param data_si_ora: data si ora date
        :return:
        '''
        reducere = 0
        tranzactie = self.__tranzactie_repository.find_by_id(id_tranzactie)
        tranzactie_before_update = tranzactie
        id_medicament_before = tranzactie.id_medicament
        id_card_client_before = tranzactie.id_card_client
        if id_medicament != '':
            tranzactie.id_medicament = id_medicament

        if id_card_client != '':
            tranzactie.id_card_client = id_card_client

        if nr_bucati != '':
            tranzactie.nr_bucati = nr_bucati

        if data_si_ora != '':
            tranzactie.data_si_ora = data_si_ora

            day, month, year, hour, minutes = data_si_ora.split('/')
            tranzactie.data_si_ora = datetime(int(year), int(month), int(day), int(hour), int(minutes))



        self.__tranzactie_repository.update(tranzactie)

        medicament = self.__medicament_repository.find_by_id(tranzactie.id_medicament)
        card_client = self.__card_client_repository.find_by_id(tranzactie.id_card_client)

        if id_medicament_before != tranzactie.id_medicament or id_card_client_before != tranzactie.id_card_client:
            if card_client is not None:
                if medicament.reteta == False:

                    reducere = (10 / 100) * medicament.pret

                else:


                    reducere = (15 / 100) * medicament.pret

        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__tranzactie_repository, tranzactie, tranzactie_before_update))
        self.__undo_redo_service.clear_redo()
        return reducere

    def get_all(self):
        '''
        returneaza toate tranzactiile
        :return:
        '''
        viewmodels = []
        for tranzactie in self.__tranzactie_repository.get_all():
            medicament = self.__medicament_repository.find_by_id(tranzactie.id_medicament)
            card_client = self.__card_client_repository.find_by_id(tranzactie.id_card_client)
            viewmodels.append(TranzactieViewModel(medicament, card_client, tranzactie.nr_bucati, tranzactie.data_si_ora))
        return viewmodels



    def afisare_tranzactii_dupa_interval(self, interval):
        '''
        afiseaza tranzactiile din intervalul dat.
        :param interval:
        :return:
        '''
        interval_nou = interval.split(',')
        tranzactii = self.__tranzactie_repository.get_all()



        def myfunc(tranzactie):
            if tranzactie.data_si_ora.day <= int(interval_nou[1]) and tranzactie.data_si_ora.day >= int(interval_nou[0]):
                return True
            else:
                return False

        list = filter(myfunc, tranzactii)
        return list






    def stergere_tranzactii_dupa_interval(self, interval):
        '''
        sterge tranzactiile din intervalul dat.
        :param interval:
        :return:
        '''
        interval_nou = interval.split(',')
        tranzactii = self.__tranzactie_repository.get_all()
        i = len(tranzactii)
        #for tranzactie in tranzactii:
            #if tranzactie.data_si_ora.day <= int(interval_nou[1]) and tranzactie.data_si_ora.day >= int(interval_nou[0]):
                #self.__tranzactie_repository.delete(tranzactie.id_entity)

        list(map(lambda tranzactie: self.__tranzactie_repository.delete(tranzactie.id_entity) if tranzactie.data_si_ora.day <= int(interval_nou[1]) and tranzactie.data_si_ora.day >= int(interval_nou[0]) else 0, tranzactii))






    def data_recursiv(self, data, tranzactii, tranzactii_interval):
        '''

        :param data: data citita
        :param tranzactii: lista de tranzactii
        :param tranzactii_interval: tranzactiile din intervalul dat
        :return:
        '''
        
        if len(tranzactii) == 0:
            return
        tranzactie = tranzactii[0]
        data_noua = data.split(',')
        if tranzactie.data_si_ora.day <= int(data_noua[1]):
            if tranzactie.data_si_ora.day >= int(data_noua[0]):
                tranzactii_interval.append(tranzactie)

        self.data_recursiv(data, tranzactii[1:], tranzactii_interval)

    def afisare_recursiv(self, data):
        '''
        returneaza tranzactiile din intervalul dat
        :param data:
        :return:
        '''
        data.split(',')
        tranzactii_interval = []
        tranzactii = self.__tranzactie_repository.get_all()
        self.data_recursiv(data, tranzactii, tranzactii_interval)
        return tranzactii_interval








