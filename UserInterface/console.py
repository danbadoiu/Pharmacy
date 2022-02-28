import datetime

from Service.card_client_service import Card_client_service
from Domain.exceptie import Exceptie
from Service.functii import Functie
from Service.medicament_service import Medicament_service

from Service.tranzactie_service import Tranzactie_service
from Service.undoredo_service import UndoRedoService


class console:
    def __init__(self, medicament_service: Medicament_service,
                 card_client_service: Card_client_service,
                 tranzactie_service: Tranzactie_service,
                 functie: Functie,
                 undo_redo_service: UndoRedoService):
        self.medicament_service = medicament_service
        self.card_client_service = card_client_service
        self.tranzactie_service = tranzactie_service
        self.functie = functie
        self.undo_redo_service = undo_redo_service


    def print_menu(self):
        print('1. CRUD Medicament')
        print('2. CRUD Card client')
        print('3. CRUD Tranzactie')
        print('4. Ordonare medicamente')
        print('5. Scumpire medicamente')
        print('6. Afisare tranzactii dupa interval')
        print('7. Stergere tranzactii din interval')
        print('8. Afisare carduri ordonate')
        print('9. Export')
        print('u. Undo')
        print('r. Redo')
        print('b. Back')


    def run_console(self):

        while True:
            self.print_menu()
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.run_crud_medicamente()
            elif op == '2':
                self.run_crud_card()
            elif op == '3':
                self.run_crud_tranzactie()
            elif op == '4':
                self.afisare_ordonate()
            elif op == '5':
                self.scumpire()
            elif op == '6':
                self.afisare_tranzactii_din_interval()
            elif op == '7':
                self.stergere_tranzactii_din_interval()
            elif op == '8':
                self.afisare_card_ord()
            elif op == '9':
                self.export()
            elif op == 'u':
                self.undo_redo_service.do_undo()
            elif op == 'r':
                self.undo_redo_service.do_redo()



            elif op == 'b':
                break

            else:
                print('Comanda invalida!')

    def run_crud_medicamente(self):
        while True:
            print('1. Create')
            print('2. Delete')
            print('3. Update')
            print('4. Showall')
            print('5. Get by anything')
            print('6. Random create')
            print('b. Back')
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.handle_create_medicamente()
            elif op == '2':
                self.handle_delete_medicamente()
            elif op == '3':
                self.handle_update_medicamente()
            elif op == '4':
                self.handle_show_all()
            elif op == '5':
                self.get_by_anything_medicament()
            elif op == '6':
                self.create_random()

            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def handle_create_medicamente(self):
        try:
            id_medicament = input('Dati id ul: ')
            nume = input('Dati numele: ')
            producator = input('Dati producatorul: ')
            pret = float(input('Dati pretul: '))
            reteta = input('necesita reteta(da/nu): ')
            self.medicament_service.create(id_medicament, nume, producator, pret, reteta)

            print('Medicamentul a fost adaugat cu succes!')
        except ValueError as c:
            print(c)
        #except KeyError as v:
            #print(v)
        except Exceptie as v:
            print(v)


    def handle_delete_medicamente(self):
        try:
            id_medicament = input('Dati id-ul: ')
            self.medicament_service.delete(id_medicament)

            print('Medicamentul a fost sters!')
        except KeyError as v:
            print(v)

    def handle_update_medicamente(self):
        try:
            id_medicament = input('Dati id-ul: ')
            nume = input('Dati numele: ')
            producator = input('Dati producatorul: ')
            pret = float(input('Dati pretul: '))
            reteta = input('necesita reteta(da/nu): ')

            self.medicament_service.update(id_medicament, nume, producator, pret, reteta)
            print('Medicamentul a fost modificat! ')
        except ValueError as v:
            print(v)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all(self):
        if len(self.medicament_service.get_all()) == 0:
            print('Lista e goala!')
        for medicament in self.medicament_service.get_all():
            print(medicament)

    def get_by_anything_medicament(self):


        t = input('Dati stringul: ')
        print(self.medicament_service.get_by_anything(t))



    def create_random(self):
        n = int(input('Dati un nr n: '))
        for i in range(n):
            self.medicament_service.random_medicament()
    def run_crud_card(self):
        while True:
            print('1. Create')
            print('2. Delete')
            print('3. Update')
            print('4. Showall')
            print('5. Get by anything')
            print('b. Back')
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.handle_create_card()
            elif op == '2':
                self.handle_delete_card()
            elif op == '3':
                self.handle_update_carduri()
            elif op == '4':
                self.show_all_carduri()
            elif op == '5':
                self.get_by_anything()


            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def handle_create_card(self):
        try:
            id_card = input('Dati id-ul: ')
            nume = input('Dati numele: ')
            prenume = input('Dati prenumele: ')
            cnp = input('Dati cnp-ul: ')
            data_nasterii = input('Dati data (dd/mm/yyyy): ')
            data_inregistrarii = input('Dati data inregistrarii (dd/mm/yyyy): ')
            self.card_client_service.create(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)
            print('Cardul a fost adaugat!')

        except ValueError as v:
            print(v)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)



    def handle_delete_card(self):
        try:
            id_card = input('Dati id-ul: ')
            self.card_client_service.delete(id_card)
            print('Cardul a fost sters!')
        except KeyError as v:
            print(v)

    def handle_update_carduri(self):
        try:
            id_card = input('Dati id-ul: ')
            nume = input('Dati numele: ')
            prenume = input('Dati prenumele: ')
            cnp = input('Dati cnp-ul: ')
            data_nasterii = input('Dati data (dd/mm//yyyy): ')
            data_inregistrarii = input('Dati data inregistrarii (dd/mm/yyyy): ')

            self.card_client_service.update(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)
            print('Cardul a fost modificat! ')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
    def show_all_carduri(self):
        if len(self.card_client_service.get_all()) == 0:
            print('Lista este goala!')
        for card in self.card_client_service.get_all():
            print(card)

    def get_by_anything(self):
        t = input('Dati stringul: ')
        print(self.card_client_service.get_by_anything(t))


    def run_crud_tranzactie(self):
        while True:
            print('1. Create')
            print('2. Delete')
            print('3. Update')
            print('4. Showall')

            print('b. Back')
            op = input('Alegeti optiunea: ')
            if op == '1':
                self.handle_create_tranzactie()
            elif op == '2':
                self.handle_delete_tranzactie()
            elif op == '3':
                self.handle_update_tranzactie()
            elif op == '4':
                self.show_all_tranzactii()




            elif op == 'b':
                break
            else:
                print('Comanda invalida!')
    def handle_create_tranzactie(self):
        try:

            id_tranzactie = input('Dati id-ul: ')
            id_medicament = input('Dati id medicament: ')
            id_card_client = input('Dati id card client: ')
            nr_bucati = input('Dati nr-ul bucatilor: ')
            data_si_ora = input('Dati data si ora (dd/mm/yyyy/hh/mm): ')

            reducere = self.tranzactie_service.create(id_tranzactie,id_medicament,id_card_client,nr_bucati,data_si_ora)
            print('Reducerea acordata a fost:', reducere)
            print('Tranzactia a fost adaugata!')
        except ValueError as v:
            print(v)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)


    def handle_delete_tranzactie(self):
        try:
            id_tranzactie = input('Dati id-ul: ')
            self.tranzactie_service.delete(id_tranzactie)
            print('Tranzactia a fost stearsa!')
        except KeyError as v:
            print(v)

    def handle_update_tranzactie(self):
        try:
            id_tranzactie = input('Dati id-ul: ')
            id_medicament = input('Dati id medicament: ')
            id_card_client = input('Dati id card client: ')
            nr_bucati = input('Dati nr-ul bucatilor: ')
            data_si_ora = input('Dati data si ora (dd/mm/yyyy/hh/mm): ')

            reducere = self.tranzactie_service.update(id_tranzactie, id_medicament, id_card_client, nr_bucati, data_si_ora)
            print('Reducerea acordata a fost:', reducere)
            print('Tranzactia a fost modificata! ')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)


    def show_all_tranzactii(self):
        if len(self.tranzactie_service.get_all()) == 0:
            print('Lista este goala!')
        for tranzactie in self.tranzactie_service.get_all():
            print(tranzactie)



    def scumpire(self):
        procent = input('Dati procentajul de scumpire: ')
        valoare = input('Dati valoarea: ')
        self.medicament_service.scumpire(procent, valoare)

    def afisare_tranzactii_din_interval(self):
        interval = input('Dati intervalul(xx,yy): ')
        #interval2 = interval.split(',')
        tranzactii = self.tranzactie_service.afisare_recursiv(interval)

        #tranzactii = self.tranzactie_service.afisare_tranzactii_dupa_interval(interval)
        for tranzactie in tranzactii:
            print(tranzactie)

    def stergere_tranzactii_din_interval(self):
        interval = input('Dati intervalul(xx,yy): ')
        self.tranzactie_service.stergere_tranzactii_dupa_interval(interval)


    def afisare_ordonate(self):
        medicamente = self.medicament_service.afisare_medicamente_nr_tranzactii()
        #medicamente = self.medicament_service.afisare_medicamente_merge_sort()
        for medicament in medicamente:
            print(medicament)



    def afisare_card_ord(self):
        list = self.functie.ordonare()
        for i,j in list:
            print(i,'valoarea este: ',j)

    def export(self):
        self.medicament_service.export()