# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
from random import randint

str_size = 10


def buble_sort(sorted_list):
    for i in range(str_size):
        for j in range(str_size - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[
                    j]  # меняем j-й и (j+1)-й элементы местами


print(my_list := [randint(0, 100) for i in
                  range(str_size)])  # рандомно создаём лист из  str_size элементов в пределах от 0 до 99
buble_sort(my_list)
print(my_list)
