money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
while salary + money_capital >= spend :
    months += 1
    money_capital -= spend
    spend += spend * increase
    money_capital += salary


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
print("Количество месяцев, которое можно протянуть без долгов:", months)
