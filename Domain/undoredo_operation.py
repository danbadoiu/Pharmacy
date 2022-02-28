from Repository.file_repository import FileRepository


class UndoRedoOperation:

    def __init__(self, repository: FileRepository):
        self.__repository = repository

    def undo(self):
        raise NotImplemented('Should use a derived class')

    def redo(self):
        raise NotImplemented('Should use a derived class')