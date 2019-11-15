def sum_func():
    global sum_a
    list_a = input(
        'Введите несколько чисел, разделенных пробелом.\n'
        'Для немедленного выхода из программы введите символ "!".\n'
        'Для получения суммы и выхода из программы введите '
        'числа и символ "!", через пробел.'
    ).split()
    if '!' in list_a:
        stop_symbol = '!'
        list_a.remove('!')
    else:
        stop_symbol = 'ok'
    sum_a = (sum(float(el) for el in list_a))
    return stop_symbol


symbol = 'ok'
work = 'ok'
sum_b = 0
while symbol is work:
    work = sum_func()
    sum_b += sum_a
    print(sum_b)
