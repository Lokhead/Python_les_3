def my_func_a(x, y):
    print(x ** y)


def my_func_b(x, y):
    num_3 = x
    for n in range(y, -1):
        num_3 *= x
    print(1 / num_3)


num_1 = float(input("Введите положительное число"))
num_2 = int(input("Введите целое отрицательное число"))
my_func_a(num_1, num_2)
my_func_b(num_1, num_2)
