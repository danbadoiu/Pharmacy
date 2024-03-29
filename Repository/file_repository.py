import jsonpickle
from copy import deepcopy

from Domain.exceptie import Exceptie


class FileRepository:
    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __write_file(self):
        with open(self.__filename, 'w') as f:
            f.write(jsonpickle.encode(self.__storage))

    def __load_file(self):
        try:
            with open(self.__filename, 'r') as f:
                self.__storage = jsonpickle.decode(f.read())

        except:
            self.__storage = {}

    def find_by_id(self, id_entity):
        '''
        returneaza entitatea cu id ul dat
        :param id_entity:
        :return:
        '''
        self.__load_file()
        if str(id_entity) in self.__storage:
            return deepcopy(self.__storage[str(id_entity)])
        return None



    def create(self, entity):
        '''
        creeaza o entitate
        :param entity: entitatea creata
        :return:
        '''

        if self.find_by_id(entity.id_entity) is not None:
            #raise KeyError(f'Exista deja o entitate cu id-ul: {entity.id_entity}!')
            raise Exceptie(f'Exista deja o entitate cu id-ul: {entity.id_entity}!')

        self.__storage[entity.id_entity] = entity
        self.__write_file()

    def update(self, entity):
        '''
        update parametriilor din entitate

        :param entity:
        :return:
        '''

        if self.find_by_id(entity.id_entity) is None:
            raise KeyError(f'Nu exista entitatea cu id-ul: {entity.id_entity}!')
        self.__storage[entity.id_entity] = entity
        self.__write_file()

    def delete(self, id_entity):
        '''
        sterge o entitate
        :param id_entity:
        :return:
        '''

        if self.find_by_id(id_entity) is None:
            raise KeyError(f'Nu exista entitatea cu id-ul: {id_entity}!')
        del self.__storage[id_entity]
        self.__write_file()

    def get_all(self):
        self.__load_file()
        return list(self.__storage.values())
