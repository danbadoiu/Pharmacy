from Domain.entity import Entity


class Tranzactie(Entity):
    def __init__(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data_si_ora):
        super().__init__(id_tranzactie)
        self.__id_medicament = id_medicament
        self.__id_card_client = id_card_client
        self.__nr_bucati = nr_bucati
        self.__data_si_ora = data_si_ora



    @property
    def id_medicament(self):
        return self.__id_medicament
    @id_medicament.setter
    def id_medicament(self, value):
        self.__id_medicament = value
    @property
    def id_card_client(self):
        return self.__id_card_client

    @id_card_client.setter
    def id_card_client(self, value):
        self.__id_card_client = value
    @property
    def nr_bucati(self):
        return self.__nr_bucati

    @nr_bucati.setter
    def nr_bucati(self, value):
        self.__nr_bucati = value

    @property
    def data_si_ora(self):
        return self.__data_si_ora

    @data_si_ora.setter
    def data_si_ora(self, value):
        self.__data_si_ora = value






    def __str__(self):
        return f"Tranzactia cu id-ul: {self.id_entity}, cu id-ul medicamentului: {self.__id_medicament}, " \
               f" cu id-ul cardului: {self.__id_card_client}, cu nr de bucati: {self.__nr_bucati}, " \
               f"din data si ora de: {self.__data_si_ora}."