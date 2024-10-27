salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Подушка безопасности

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

# Этим циклом я посчитал в какой минус уйдёт человек за 10 месяцев без подушки безопасности
for i in range(months):
    money_capital += (salary - spend)
    spend *= (1+increase)

money_capital *= -1



print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
