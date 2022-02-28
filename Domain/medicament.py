from Domain.entity import Entity


class Medicament(Entity):
    '''
    descrie un medicament
    '''


    def __init__(self, id_medicament, nume, producator, pret, reteta):
        super().__init__(id_medicament)
        self.__nume = nume
        self.__producator = producator
        self.__pret = pret
        self.__reteta = reteta


    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def producator(self):
        return self.__producator

    @producator.setter
    def producator(self, value):
        self.__producator = value

    @property
    def pret(self):
        return self.__pret

    @pret.setter
    def pret(self, value):
        self.__pret = value

    @property
    def reteta(self):
        return self.__reteta

    @reteta.setter
    def reteta(self, value):
        self.__reteta = value


    def __str__(self):
        return f'Medicamentul cu id: {self.id_entity}, nume: {self.__nume}, producator: {self.__producator}, ' \
               f'pret: {self.__pret}, reteta: {self.__reteta}'

