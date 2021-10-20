def read_list():
    '''
    Citire lista nr intregi (ex.1)
    :return: lista
    '''
    list_str = input("Enter list items: ").split(" ")
    lst = []
    for el in list_str:
        lst.append(int(el))
    return lst

def list_negative_elems(lst):
    '''
    Afisare elemente negative nenule (ex.2)
    :param lst: lista
    :return: lista numere negative nenule
    '''
    rez = []
    for el in lst:
        if el < 0:
            rez.append(el)
    return rez

def test_list_negatives_elems():
    assert list_negative_elems([-1, 5, 25, 0, -56]) == [-1, -56]
    assert list_negative_elems([1, 3]) == []
    assert list_negative_elems([]) == []

def nr_last_digit(lst , cfr):
    '''
    Afisare numarul cel mai mic care are ultima cifra egata cu o cifra citita de la tastatura (ex.3)
    :param lst: lista in care vom cauta numarul minim
    :param cfr: cifra care va determina ultima cifra a numarului cerut
    :return: cel mai mic numar intreg
    '''
    mini = None
    for n in lst:
        int_n = int(n)
        if int_n % 10 == cfr:
            if mini == None or int_n < mini:
                mini = int_n
    return mini

def test_nr_last_digit():
    assert nr_last_digit([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert nr_last_digit([3, 33, 24, 89], 3) == 3

def is_superprime(n):
    '''
    Verifica daca un numar este superprim
    :param n: numar intreg
    :return: True daca este superprim, False daca nu este superprim
    '''
    ok = 1
    while n:
        d = 0
        for i in range(1, int(n)):
            if n % i == 0:
                d = d + 1
        if d > 2:
            ok = 0
        n = n // 10
    if ok == 1:
        return True
    return False

def test_is_superprime():
    assert is_superprime(233) == 1
    assert is_superprime(237) == 0
    assert is_superprime(67) == 0

def list_all_superprime(lst):
    '''
    Afisarea tuturor numerelor superprime din lista (ex.4)
    :param lst: lista de numere intregi
    :return: numerele superprime in lista de numere intregi
    '''
    rez = []
    for el in lst:
        if el > 0 and is_superprime(el):
            rez.append(el)
    return rez

def test_list_all_superprime():
    assert list_all_superprime([239, 73, 5, 18, 832]) == [239, 73, 5]
    assert list_all_superprime([3, 78, 23]) == [3, 23]

def invert_digits(n):
    '''
    Inverseaza cifrele numerelor negative
    :param n: numar intreg
    :return: numar intreg
    '''
    og = 0
    nat_n = -1 * n
    while nat_n > 0:
        og = og*10 + nat_n%10
        nat_n = nat_n//10
    return og * (-1)

def test_invert_digits():
    assert invert_digits(-76) == -67
    assert invert_digits(-87) == -78

def list_modified(lst):
    '''
    Modifica lista conform cerintei (ex.5)
    :param lst: lista de numere intregi
    :return: lista de numere intregi
    '''
    rez= []
    for el in lst:
        if el <= 0:
            elneg = invert_digits(el)
            rez.append(elneg)
        elif el > 0:
            pass
    return rez

def test_list_modified():
    assert list_modified([-75, -76, 89]) == [-57, -67]

def show_menu():
    '''
    Printare meniu
    :return: meniu
    '''
    print('''
    1. Citeste lista
    2. Afișarea tuturor numerelor negative nenule din listă
    3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    4. Afișarea tuturor numerelor din listă care sunt superprime.
    5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    x. Iesire
    ''')

def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Command: ")
        if cmd == '1':
            lst = read_list()
        elif cmd == '2':
            rez = list_negative_elems(lst)
            print(rez)
        elif cmd == '3':
            cfr = int(input("Enter digit: "))
            rez = nr_last_digit(lst, cfr)
            print(rez)
        elif cmd == '4':
            rez = list_all_superprime(lst)
            print(rez)
        elif cmd == '5':
            rez = list_modified(lst)
            print(rez)
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida")

def run_tests():
    test_list_negatives_elems()
    test_nr_last_digit()
    test_is_superprime()
    test_list_all_superprime()
    test_invert_digits()
    test_list_modified()

if __name__ == '__main__':
    run_tests()
    main()
