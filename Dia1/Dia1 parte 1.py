def arriba_abajo(lista):
    suma = 0
    for x in range(len(lista)):
        if lista[x] > lista[x-1]:
            suma += 1
        else:
            continue
    print(suma)


if __name__ == "__main__":
    with open("input.txt") as f:
        listainputs = [int(line) for line in f]

    arriba_abajo(listainputs)