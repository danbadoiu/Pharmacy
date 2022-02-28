from Domain.card_client import Card_client
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie


def test_medicament():
    m = Medicament(1,'ana', 'dasd', 56.8, True)

    assert m.nume == 'ana'
    assert m.reteta == True
    assert m.pret == 56.8

def test_card_client():
    c = Card_client(2,'ana','ddd',555,'24.03.2019','3.01.2001')
    assert c.nume == 'ana'
    assert c.id_entity == 2
    assert c.cnp == 555

def test_tranzactie():
    t = Tranzactie(4, 5, 6, 56,'3.10.3')
    assert t.id_entity == 4
    assert t.id_medicament == 5
    assert t.id_card_client == 6
