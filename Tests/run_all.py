from Tests.test_card_service import test_create_card, test_stergere_card, test_update_card
from Tests.test_domain import test_medicament, test_tranzactie, test_card_client
from Tests.test_medicament_service import test_create_medicament, test_ordonare
from Tests.test_tranzactie_service import test_create_tranzactie, test_stergere_interval, test_stergere


def run_all_tests():
    test_medicament()
    test_tranzactie()
    test_card_client()
    test_create_medicament()
    test_create_card()
    test_create_tranzactie()
    test_stergere_interval()
    test_stergere()
    test_stergere_card()
    test_update_card()
    test_ordonare()