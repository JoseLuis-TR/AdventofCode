def arriba_abajo(lista):
    """
    [Función que recibe la lista con los inputs y compara cada uno de los valores recorridos con su anterior,
    si es mayor se añade 1 a la suma y si no lo es se sigue con el proceso]
    Recibe:
        lista: Lista con los inputs del reto

    Devuelve:
        suma: Un número entero que sacamos tras revisar cuantas veces el submarino asciende
    """
    suma = 0
    for x in range(len(lista)):
        if lista[x] > lista[x-1]:
            suma += 1
        else:
            continue
    return suma


def main():
    """
    [Función principal del programa que lee el archivo input.txt y convierte los datos en una lista que pasa más
    adelante a la función arriba_abajo]

    Devuelve:
        print: número de veces que el submarino asciende gracias a la función arriba_abajo

    """
    with open("input.txt") as f:
        listainputs = [int(line) for line in f]

    print(arriba_abajo(listainputs))


if __name__ == "__main__":
    main()
