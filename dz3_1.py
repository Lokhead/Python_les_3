def division(num1, num2):
    return a / b


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
if b == 0:
    print("Вы пытаетесь делить на ноль")
else:
    print(division(a, b))
