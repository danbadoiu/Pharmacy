
class Medicament_validator:
    def validate(self, medicament):

        erori = [ ]
        if float(medicament.pret) < 0:

            erori.append('Pretul este negativ.')
        if len(erori)>0:
            raise ValueError(erori)