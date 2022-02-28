from Repository.file_repository import FileRepository
from Service.tranzactie_service import Tranzactie_service
from Service.undoredo_service import UndoRedoService
from Tests.utils import clear_file


def test_create_tranzactie():
    undo_redo_service = UndoRedoService()
    filename = 'test_tranzactie.txt'
    clear_file(filename)
    repository_tranzactie = FileRepository(filename)
    repository_medicament = FileRepository(filename)
    repository_card = FileRepository(filename)

    service = Tranzactie_service(repository_tranzactie, repository_medicament, repository_card, undo_redo_service)
    service.create(5,1,1,45,2001-12-20)
    assert len(service.get_all()) == 1
    try:
        service.create(5, 1, 1, 45, 2001 - 12 - 20)

        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
    assert len(service.get_all()) == 1

    try:
        service.create(5,2,1,45,2001-12-20)
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
    assert len(service.get_all()) == 1

def test_stergere_interval():
    undo_redo_service = UndoRedoService()
    filename = 'test_tranzactie.txt'
    clear_file(filename)
    repository_tranzactie = FileRepository(filename)
    repository_medicament = FileRepository(filename)
    repository_card = FileRepository(filename)
    service = Tranzactie_service(repository_tranzactie, repository_medicament, repository_card, undo_redo_service)
    service.create(5, 1, 1, 45, 2001 - 12 - 20)
    service.stergere_tranzactii_dupa_interval('19,21')
    assert len(service.get_all()) == 0

def test_stergere():
    undo_redo_service = UndoRedoService()
    filename = 'test_tranzactie.txt'
    clear_file(filename)
    repository_tranzactie = FileRepository(filename)
    repository_medicament = FileRepository(filename)
    repository_card = FileRepository(filename)
    service = Tranzactie_service(repository_tranzactie, repository_medicament, repository_card, undo_redo_service)
    service.create(5, 1, 1, 45, 2001 - 12 - 20)
    service.create(7, 1, 1, 34, 2001 - 12 - 17)
    service.delete(7)
    assert len(service.get_all()) == 1


