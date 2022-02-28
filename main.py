
from Domain.medicament_validator import Medicament_validator
from Repository.file_repository import  FileRepository

from Service.card_client_service import Card_client_service
from Service.functii import Functie
from Service.medicament_service import Medicament_service
from Service.tranzactie_service import Tranzactie_service
from Service.undoredo_service import UndoRedoService
from Tests.run_all import run_all_tests
from UserInterface.console import console


def main():
    card_repository = FileRepository('card.txt')
    medicament_repository = FileRepository('medicament.txt')
    tranzactie_repository = FileRepository('tranzactie.txt')
    undo_redo_service = UndoRedoService()

    medicament_validator = Medicament_validator()
    medicament_service = Medicament_service(medicament_repository, medicament_validator, tranzactie_repository, undo_redo_service)



    card_client_service = Card_client_service(card_repository, undo_redo_service)


    tranzactie_service = Tranzactie_service(tranzactie_repository, medicament_repository, card_repository, undo_redo_service)

    functie = Functie(tranzactie_repository, card_repository, medicament_repository)

    userinterface = console(medicament_service, card_client_service, tranzactie_service, functie, undo_redo_service)
    userinterface.run_console()
    run_all_tests()

    medicament_service.export()





main()


