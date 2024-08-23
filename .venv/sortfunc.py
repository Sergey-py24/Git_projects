nums = [33, 22, 44, 99, 77, 88, 66, 55]


def bubble_sort(ls):  # пузырьковая сортировка
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True


# bubble_sort(nums)
# print(nums)


def selection_sort(ls):  # сортировка выборкой
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


# selection_sort(nums)
# print(nums)


def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j = 1
        ls[j + 1] = key
    return ls


selection_sort(nums)
print(nums)