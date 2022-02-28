from Repository.file_repository import FileRepository


class Functie:
    def __init__(self, tranzactie_repository: FileRepository,
                 card_repository: FileRepository,
                 medicament_repository: FileRepository):
        self.__tranzactie_repository = tranzactie_repository
        self.__card_repository = card_repository
        self.__medicament_repository = medicament_repository

    def ordonare(self):
        '''
        afiseaza lista de carduri ordonate descrescatordupa valoarea reducerilor obtinute
        :return:
        '''
        carduri = self.__card_repository.get_all()
        tranzactii = self.__tranzactie_repository.get_all()

        dictionar = {}
        for card in carduri:
            valoare = 0
            for tranzactie in tranzactii:
                if tranzactie.id_card_client == card.id_entity:
                    medicament = self.__medicament_repository.find_by_id(tranzactie.id_medicament)

                    if medicament.reteta == False:

                        reducere = (10 / 100) * medicament.pret
                        valoare = valoare + reducere
                    elif medicament.reteta == True:

                        reducere = (15 / 100) * medicament.pret
                        valoare = valoare + reducere
            dictionar[card.id_entity] = valoare

        def get_valoare(card):
            '''
            returneaza valoarea din dictionar a cardului dat
            :param card:
            :return:
            '''
            return dictionar[card.id_entity]

        #return carduri.sort(key = get_valoare, reverse = True)


        return list(map(lambda i: (i,get_valoare(i)), carduri))



