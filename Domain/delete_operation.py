from Domain.undoredo_operation import UndoRedoOperation


class DeleteOperation(UndoRedoOperation):
    def __init__(self, repository, deleted_object):
        super().__init__(repository)
        self.deleted_object = deleted_object


    def undo(self):
        self.__repository.create(self.deleted_object)

    def redo(self):
        self.__repository.delete(self.deleted_object.id_entity)