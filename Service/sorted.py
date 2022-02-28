def my_sorted(lista, functie_sort, reverse = False):
    '''
    returneaza lista ordonata dupa functia de sortare citita
    :param lista:
    :param functie_sort:
    :param reverse:
    :return:
    '''
    lungime = len(lista)
    for i in range(lungime-1):
        for j in range(lungime):
            if functie_sort(lista[i], lista[j]) == reverse:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#print(my_sorted([5,8,7,2,32], lambda x,y: x<y, reverse = True))