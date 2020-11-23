def enumeracoes(items: list):  # items = [1, 2, 3]
    len_items = len(items)  # 3
    list_zeros = [0] * (len_items + 1)  # [0] * (3 + 1) → [0, 0, 0, 0]
    element = 0
    while True:
        if list_zeros[element] < len_items:  # 3 < 3
            prox_element = element + 1  # 2 + 1 = 3
            list_zeros[prox_element] = list_zeros[element] + 1  # 2 + 1 = 3
            # list_zeros = [0, 1, 2, 3]
            element += 1  # 2 + 1 = 3
        else:
            list_zeros[element - 1] += 1  # list_zeros[3 - 1] → list_zeros[2] = 2 + 1 = 3
            # list_zeros = [0, 1, 3, 3]
            element -= 1  # 3 - 1 = 2

        if element == 0:
            break

        else:
            lista = []
            for list_item in range(1, element + 1):
                obj = items[list_zeros[list_item] - 1]
                lista.append(obj)
            yield lista


def combinacoes(items, n):
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in combinacoes(items[:i] + items[i+1:], n-1):
                yield [items[i]] + cc


def permutacoes(items):
    return combinacoes(items, len(items))

##print ('Permutacoes')
# for p in permutacoes([1, 2, 3]):
#     print (p)
##
##print ('Enumeracoes')
for p in enumeracoes([1, 2, 3]):
    print (p)

# for p in permutacoes(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
##    print (p)
##
# for p in enumeracoes(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
##    print (p)
