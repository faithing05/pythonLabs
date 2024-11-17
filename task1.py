money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

money_count = money_capital
number = 0

while money_count > 0:
    if number > 1:
        money_count -= spend + (spend * increase)
        increase += 0.05
    else:
        money_count -= spend + (spend * increase)
    if money_count <= 0:
        break
    money_count += salary
    number += 1

print("Количество месяцев, которое можно протянуть без долгов:", number)
