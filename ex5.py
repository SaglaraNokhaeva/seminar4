# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
#
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

from pprint import pprint

def grants_dict (names, pays, persents):
    persents = list(map(lambda x: float(x[:-1])/100, persents))
    return {name: pay*persent for name, pay, persent in zip(names, pays, persents)}

names = ["Иван", "Петр", "Михаил"]
pays = [10000, 15000, 20000]
persents = ['50.25%', '20%', '30.6%']

pprint(grants_dict(names, pays, persents))