
import datetime

from Domain.add_operation import AddOperation
from Domain.card_client import Card_client

from Domain.delete_operation import DeleteOperation
from Domain.update_operation import UpdateOperation

from Repository.file_repository import FileRepository
from Service.undoredo_service import UndoRedoService


class Card_client_service:
    def __init__(self, card_repository: FileRepository,

                 undo_redo_service: UndoRedoService):

        self.__card_repository = card_repository
        self.__undo_redo_service = undo_redo_service



    def create(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        '''
        creeaza un card 
        :param id_card:id ul cardului
        :param nume: numele cardului
        :param prenume: prenumele cardului
        :param cnp: cnp ul cardului
        :param data_nasterii: data nasterii
        :param data_inregistrarii: data inregistrarii
        :return:
        '''
        card = Card_client(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)
        day,month,year = data_nasterii.split('/')

        card.data_nasterii = datetime.date(int(year), int(month), int(day))


        day, month, year = data_inregistrarii.split('/')

        card.data_inregistrarii = datetime.date(int(year), int(month), int(day))
        for i in self.__card_repository.get_all():
            if i.cnp == cnp:
                raise KeyError(f'Exista deja o entitate cu cnp-ul: {cnp}!')




        self.__card_repository.create(card)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__card_repository, card))
        self.__undo_redo_service.clear_redo()



    def delete(self, id_card):
        '''
        sterge un card
        :param id_card: id ul de stergere
        :return:
        '''
        obiect = self.__card_repository.find_by_id(id_card)
        self.__card_repository.delete(id_card)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__card_repository, obiect))
        self.__undo_redo_service.clear_redo()



    def update(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        '''
        updateaza un card prin parametrii dati
        :param id_card: id ul cardului
        :param nume: numele cardului
        :param prenume: prenumele cardului
        :param cnp: cnp ul cardului
        :param data_nasterii: data nasterii
        :param data_inregistrarii: data inregistrarii
        :return:
        '''
        card = self.__card_repository.find_by_id(id_card)
        card_before_update = card

        if nume != '':
            card.nume = nume

        if prenume != '':
            card.prenume = prenume

        if cnp != '':
            card.cnp = cnp

        if data_nasterii != '':
            card.data_nasterii = data_nasterii

        if data_inregistrarii != '':
            card.data_inregistrarii = data_inregistrarii

        day, month, year = data_nasterii.split('/')

        card.data_nasterii = datetime.date(int(year), int(month), int(day))


        day, month, year = data_inregistrarii.split('/')

        card.data_inregistrarii = datetime.date(int(year), int(month), int(day))





        self.__card_repository.update(card)
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__card_repository, card, card_before_update))
        self.__undo_redo_service.clear_redo()

    def get_all(self):
        return self.__card_repository.get_all()


    def get_by_anything(self, t):
        '''
        returneaza entitatea gasita dupa stringul dat
        :param t: stringul citit
        :return:
        '''
        carduri = self.__card_repository.get_all()


        for card_client in carduri:
            if card_client.cnp == t:
                return card_client
            if card_client.data_inregistrarii == str(t):
                return card_client
            if card_client.data_nasterii == str(t):
                return card_client
            if card_client.nume == str(t):
                return card_client
            if card_client.prenume == str(t):
                return card_client
        return None










