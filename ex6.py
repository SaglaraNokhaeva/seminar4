# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def cut_cum(lst, start, stop):
    return sum(lst[min(start, stop)+1:max(start, stop)])

lst = [i for i in range(100)]
print(lst)

print(cut_cum(lst, 97, 105))