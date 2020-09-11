check_email = input("Введите логин:")
check_password = input("Введите пароль:")
repeat_password = input("Введите пароль:")

if check_password == repeat_password:
    print ("Вы успешно зарегистрировались")
    print("Вы хотите войти в систему?")
    check  = input("Да или Нет")
    if check == 'Да':
        login = input("Введите логин:")
        password = input("Введите пароль:")
        if login == check_email and password == check_password:
            print ("Вы вошли в систему ")
        else:
           print("повторите попытку")
    else :
        print("Переход на главную страницу!")
else :
    print('Пароли не совпадают')

