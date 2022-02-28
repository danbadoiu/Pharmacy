from Domain.medicament_validator import Medicament_validator


from Repository.file_repository import FileRepository
from Service.card_client_service import Card_client_service
from Service.medicament_service import Medicament_service
from Service.tranzactie_service import Tranzactie_service
from Service.undoredo_service import UndoRedoService
from Tests.utils import clear_file


def test_create_medicament():
    undo_redo_service = UndoRedoService()
    filename = 'test_medicament.txt'
    clear_file(filename)
    repository = FileRepository(filename)
    validator = Medicament_validator()
    tranzactie_repository = FileRepository(filename)
    service = Medicament_service(repository, validator, tranzactie_repository, undo_redo_service)
    service.create(1,'aas','dsasd',56.7,True)
    assert len(service.get_all()) == 1
    try:
        service.create(3,'aas','dsda',56.7,True)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
    assert len(service.get_all()) == 1

    try:
        service.create(1,'aas','dsasd',56.7,True)
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
    assert len(service.get_all()) == 1

    added = repository.find_by_id(1)
    assert added is not None
    assert added.id_masina == 1
    assert added.nume == 'aas'

def test_ordonare():
    undo_redo_service = UndoRedoService()
    filename = 'test_medicament.txt'
    clear_file(filename)
    repository = FileRepository(filename)
    validator = Medicament_validator()
    tranzactie_repository = FileRepository(filename)
    service = Medicament_service(repository, validator, tranzactie_repository, undo_redo_service)
    service.create(1, 'aas', 'dsasd', 56.7, False)
    service.create(2, 'aasdas', 'safdsd', 87, True)
    service.create(3, 'afsdaf', 'dsasd', 47, False)
    service.create(4, 'aas', 'dssdfd', 57.2, True)
    service2 = Tranzactie_service(repository, repository, repository,undo_redo_service )
    service3 = Card_client_service(repository, undo_redo_service)
    service3.create(1,'asd','ads',43242,13/2/2001,14/2/2003)
    service2.create(1,1,1,2423,2/3/2002/12/34)
    lista = service.afisare_medicamente_nr_tranzactii()
    assert lista[0].id_entity == 1


