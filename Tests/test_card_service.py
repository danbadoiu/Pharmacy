
from Repository.file_repository import FileRepository

from Service.card_client_service import Card_client_service
from Service.undoredo_service import UndoRedoService
from Tests.utils import clear_file


def test_create_card():
    undo_redo_service = UndoRedoService()
    filename = 'test_card.txt'
    clear_file(filename)
    repository = FileRepository(filename)

    service = Card_client_service(repository, undo_redo_service)
    service.create(2, 'ana', 'asf', 68789, 2303-23-23, 2303-23-23)
    assert len(service.get_all()) == 1
    try:
        service.create(2, 'ana', 'asf', 68789, 2303-23-23, 2303-23-23)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
    assert len(service.get_all()) == 1

    try:
        service.create(2, 'ana', 'asf', 68789, 2303-23-23, 2303-23-23)
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
    assert len(service.get_all()) == 1

    added = repository.find_by_id(2)
    assert added is None

def test_stergere_card():
    undo_redo_service = UndoRedoService()
    filename = 'test_card.txt'
    clear_file(filename)
    repository = FileRepository(filename)

    service = Card_client_service(repository, undo_redo_service)
    service.create(2, 'ana', 'asf', 68789, 2303 - 23 - 23, 2303 - 23 - 23)
    service.delete(2)
    assert len(service.get_all()) == 0

def test_update_card():
    undo_redo_service = UndoRedoService()
    filename = 'test_card.txt'
    clear_file(filename)
    repository = FileRepository(filename)
    
    service = Card_client_service(repository, undo_redo_service)
    service.create(2, 'ana', 'asf', 68789, 2303 - 23 - 23, 2303 - 23 - 23)
    service.update(2, 'sdf', 'ddd', 68789, 2303 - 23 - 23, 2303 - 23 - 23)
    card = service.get_all()[0]
    assert card.nume == 'sdf'