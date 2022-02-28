from Domain.undoredo_operation import UndoRedoOperation


class UpdateOperation(UndoRedoOperation):
    def __init__(self, repository, updated_object, to_update_object):
        super().__init__(repository)
        self.updated_object = updated_object
        self.to_update_object = to_update_object


    def undo(self):
        self.__repository.update(self.to_update_object)

    def redo(self):
        self.__repository.update(self.updated_object)