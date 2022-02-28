from Domain.entity import Entity


class Card_client(Entity):
    '''

    '''
    def __init__(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        super().__init__(id_card)
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        self.__data_nasterii = data_nasterii
        self.__data_inregistrarii = data_inregistrarii

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def prenume(self):
        return self.__prenume

    @prenume.setter
    def prenume(self, value):
        self.__prenume = value

    @property
    def cnp(self):
        return self.__cnp
    @cnp.setter
    def cnp(self, value):
        self.__cnp = value

    @property
    def data_nasterii(self):
        return self.__data_nasterii

    @data_nasterii.setter
    def data_nasterii(self, value):
        self.__data_nasterii = value

    @property
    def data_inregistrarii(self):
        return self.__data_inregistrarii

    @data_inregistrarii.setter
    def data_inregistrarii(self, value):
        self.__data_inregistrarii = value



    def __str__(self):
        return f'Cardul cu id-ul: {self.id_entity}, cu numele: {self.__nume}, cu prenumele: {self.__prenume}, cu cnp-ul: {self.__cnp}, cu data nasterii: {self.__data_nasterii}, cu data inregistrarii: {self.__data_inregistrarii}'
