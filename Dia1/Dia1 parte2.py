def arriba_abajo_tres(lista):
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


if __name__ == "__main__":
    with open("input.txt") as f:
        listainputs = [int(line) for line in f]

    print(arriba_abajo_tres(listainputs))
