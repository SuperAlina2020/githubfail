combo1 = 200
combo2 = 300
print("Меню : Комбо1 = ", combo1, "сом")
print("Комбо2 =", combo2 ,"сом")
meal = input("Выберите бдюдо : комбо1 , комбо2")
money = int (input("Введите ваш баланс :"))
if meal == 'комбо1':
    if money >= combo1:
        print("Ваш заказ Комбо1")
    if money < combo1:
        print("У вас недостаточно средств")
elif meal == 'комбо2':
    time = int(input("Введите время прибытия:"))
    combo_time = 18
    if time <= combo_time:
        print("У нас действует акция, стоимость Комбо2 =", combo2*0.8, "сом")
        if money >= combo2*0.8:
            print("Ваш заказ Комбо2")
        else :
            print("У вас недостаточно средств")
    else:
        print("Акция не действует")
        if money >= combo2:
            print("Ваш заказ комбо2")
else:
    print("Такого блюда нет")