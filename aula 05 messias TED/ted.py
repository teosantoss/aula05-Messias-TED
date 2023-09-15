numeros_que_atendem = []
for numero in range(100, 2001):
    if numero % 11 == 5:
        numeros_que_atendem.append(numero)
        print("Números entre 1000 e 2000 que, quando divididos por 11, produzem um resto igual a 5:")
        for numero in numeros_que_atendem:
            print(numero)