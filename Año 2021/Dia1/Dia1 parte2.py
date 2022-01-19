def arriba_abajo_tres(lista):
    """
    [Función que recibe la lista con los inputs y primero se usa un for para sumar los elementos de la lista de tres en
    tres como se indica en el reto para después con otro for hacer la comprobación elemento a elemento y ver cuales son
    mayores a su elemento predecesor]
    Args:
        lista: Lista con los inputs del reto

    Returns:
        suma: Número entero con las veces que un grupo de tres asciende más que el anterior
    """
    suma = 0
    listatres = []
    for x in range(len(lista) - 2):
        listatres.append(sum(lista[x:x+3]))

    for i in range(len(listatres)):
        if listatres[i] > listatres[i-1]:
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

    print(arriba_abajo_tres(listainputs))


if __name__ == "__main__":
    main()
