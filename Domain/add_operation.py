from Domain.undoredo_operation import UndoRedoOperation


class AddOperation(UndoRedoOperation):

    def __init__(self, repository, added_object):
        super().__init__(repository)
        self.added_object = added_object


    def undo(self):
        self.__repository.delete(self.added_object.id_entity)

    def redo(self):
        self.__repository.create(self.added_object)