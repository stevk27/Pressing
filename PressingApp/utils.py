import random
import secrets
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def hash_key():
    key = secrets.token_hex(3)
    print(key)
    key1 = key.upper()
    hexa = 0
    for el in key.upper():
        print(int(el, 16))
        hexa = hexa + int(el, 16)
    est_premier = is_prime(hexa)
    if est_premier:
        second_hexa = hex(hexa)
        test = second_hexa.replace("0x","")
    else:
        add_hexa = hexa
        i = hexa
        while not is_prime(i):
            i += 1
        first_test = i + add_hexa
        second_hexa = hex(first_test)
        test = second_hexa.replace("0x","")
    if len(str(test)) < 4:
        nbre = 4 - int(len(str(test)))
        keygen = secrets.token_hex(nbre)
        key2 = keygen.upper() + test.upper()
    else:
        key2 = test
    hexa3 = 0
    for el in key2:
        print(int(el, 16))
        hexa3 = hexa3 + int(el, 16)
    print(hexa3)
    premier = is_prime(hexa3)
    if premier:
        third_hexa = hex(hexa3)
        test2 = third_hexa.replace("0x","")
    else:
        add_hexa2 = hexa3
        i = hexa
        while not is_prime(i):
            i += 1
        second_test = i + add_hexa2
        third_hexa = hex(second_test)
        test2 = third_hexa.replace("0x","")
    if len(str(test2)) < 4:
        nbre2 = 4 - int(len(str(test2)))
        keygen2 = secrets.token_hex(nbre2)
        key3 = keygen2.upper() + test2.upper()
    else:
        key3 = test2
    
    cle = key1 + '-' + key2 + '-' + key3
    print(cle)
    return cle



def create_new_ref_number():
    # return str(random.randint(1000000000, 9999999999))
    return hash_key()

