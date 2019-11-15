def personal_data(**kwargs):
    print(
        kwargs['f_name'],
        kwargs['l_name'],
        kwargs['year'],
        kwargs['city'],
        kwargs['email'],
        kwargs['phone']
    )


param_1 = input("Введите имя: ")
param_2 = input("Введите фамилию: ")
param_3 = input("Введите год рождения: ")
param_4 = input("Введите город: ")
param_5 = input("Введите email: ")
param_6 = input("Введите телефон: ")
personal_data(
    f_name=param_1,
    l_name=param_2,
    year=param_3,
    city=param_4,
    email=param_5,
    phone=param_6
)
