def my_func(num_1, num_2, num_3):
    max_1 = max(num_1, num_2, num_3)
    if max_1 is num_1:
        max_2 = max(num_2, num_3)
    elif max_1 is num_2:
        max_2 = max(num_1, num_3)
    else:
        max_2 = max(num_1, num_2)
    sum_a = max_1 + max_2
    print(f"Сумма наибольших двух аргументов: {sum_a}")


a_1 = float(input("Введите первое число"))
a_2 = float(input("Введите второе число"))
a_3 = float(input("Введите третье число"))
my_func(a_1, a_2, a_3)
