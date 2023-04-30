# simular el comportamiendo del operador in

print(5 in [2, 3, 4, 5])
print('k' in 'kilo')


def sim_in(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False


print(sim_in('hola', 'j'))
print(sim_in('hola', 'h'))
print(sim_in([1, 2, 3, 4, 5], 6))
print(sim_in([1, 2, 3, 4, 5], 2))
