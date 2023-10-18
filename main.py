def sum_even_digits(n):
    even_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit
        n //= 10
    return even_sum
input_num = 0
while True:
    try:
        input_num = int(input("Введите натуральное число: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
    finally:
        print("Программа прошла круг.")
result_sum = sum_even_digits(input_num)
print("Сумма четных цифр в числе ", input_num, ":", result_sum)
def create_chessboard(n, m):
    chessboard = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        chessboard.append(row)
    return chessboard
while True:
    try:
        n = int(input("Введите размерность n: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
while True:
    try:
        m = int(input("Введите размерность m: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
chessboard = create_chessboard(n, m)
for row in chessboard:
    print(" ".join(row))
def process_argument(arg):
    if isinstance(arg, set):
        if len(arg) >= 3:
            largest_values = sorted(arg, reverse=True)[:3]
            print("Первые три наибольших значения:", largest_values)
        else:
            print("Множество содержит менее трех элементов.")

    elif isinstance(arg, int):
        n = 3
        while n != arg:
            if arg % (n-1) == 0:
                print("Число не является простым.")
                break
            else:
                print("Число является простым")
                break
            n += 1
    else:
        print("Неизвестный тип аргумента.")
process_argument({4, 7, 2, 9, 5, 8})
process_argument(8)

