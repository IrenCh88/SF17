error = 'ПЕРЕЗАПУСТИТЕ ПРОГРАММУ'
numbersall = input('Введите числа через пробел: ')
numberind = int(input('Введите число: '))

#######################################################################
# Функция для определения цифр в строке

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in numbersall:
    print("\nмежду числами нет пробелов")
    numbersall = input('Введите целые числа через пробел: ')
if not is_int(numbersall):
    print('\nвы ввели не цифры\n')
    print(error)
else:
    numbersall = numbersall.split()


list_numbersall = [int(item) for item in numbersall]


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result
list_numbersall = merge_sort(list_numbersall)


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число больше списка, введите меньшее число.'

print(f'Упорядоченный по возрастанию: {list_numbersall}')

if not binary_search(list_numbersall, numberind, 0, len(list_numbersall)):
    rI = min(list_numbersall, key=lambda x: (abs(x - numberind), x))
    ind = list_snumbersall.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < numberind:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_numbersall[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_numbersall.index(rI)}
В списке нет меньшего элемента''')
    elif rI > numberind:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_numbersall.index(rI)}
Ближайший меньший элемент: {list_numbersall[min_ind]} его индекс: {min_ind}''')
    elif list_numbersall.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_numbersall.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_numbersall, numberind, 0, len(list_numbersall))}')