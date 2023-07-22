# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
def is_all_rentable(companeis):
    return all([sum(i) > 0 for i in companeis.values()])

dict_companeis = {}
company_names = ["aaa", "bbb", "ccc"]
aaa_digit = [10, -20, 30, 40]
bbb_digit = [21, 212, -44]
ccc_digit = [33, -3333, -22222]

dict_companeis[company_names[0]] = aaa_digit
dict_companeis[company_names[1]] = bbb_digit
dict_companeis[company_names[2]] = ccc_digit

print(is_all_rentable((dict_companeis)))
