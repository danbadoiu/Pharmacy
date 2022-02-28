class TranzactieViewModel:
    def __init__(self, medicament, card_client, nr_bucati, data_si_ora):

        self.__medicament = medicament
        self.__card_client = card_client
        self.__nr_bucati = nr_bucati
        self.__data_si_ora = data_si_ora

    def __str__(self):
        return f'Tranzactia cu  {self.__medicament} si  {self.__card_client}, '\
               f'cu nr de bucati {self.__nr_bucati} si data si ora {self.__data_si_ora}.'