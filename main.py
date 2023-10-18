rez_sum = 1
n = 2
while rez_sum < 3:
      rez_sum = rez_sum + 1/n
      n = n+1
print("Количество:", n+1)
input_string = input("Введите строку текста: ")
numbers = ""
for char in input_string:
    if char.isdigit():
        numbers += char
if numbers:
    print("Числа в строке:")
    print(numbers)
else:
    print("В строке нет чисел.")
while True:
    try:
        num_elements = int(input("Введите количество элементов в списке: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
my_list = []
for i in range(num_elements):
    while True:
        try:
            element = int(input(f"Введите элемент {i + 1} : "))
            my_list.append(element)
            break
        except ValueError:
            print("Ошибка! Введите целое число.")
print("Заполненный список:", my_list)
while True:
    try:
        c = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
count_greater_than_C = sum(1 for x in my_list if x > c)
print("Количество элементов больше с:", count_greater_than_C)
max_abs_value = max(my_list)
max_abs_index = my_list.index(max_abs_value)
product_after_max_abs = 1
for x in my_list[max_abs_index + 1:]:
    product_after_max_abs *= x
print("Произведение элементов после максимального по модулю элемента:", product_after_max_abs)
my_list = [x for x in my_list if x <= 0]
print("Список после удаления положительных элементов:", my_list)
input_string = 'I love Python'
letter_counts = {}
for letter in input_string:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
print("Словарь с количеством вхождений букв:")
print(letter_counts)
jewelry_store = {
    'Кольцо': ['Золото', 500, 10],
    'Браслет': ['Серебро', 250, 15],
    'Ожерелье': ['Золото', 700, 5],
    'Серьги': ['Золото', 350, 8],
    'Цепь': ['Серебро', 150, 12]
}
while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню (1/2/3/4/5/6): ")

    if choice == '1':
        item = input("Введите название изделия: ")
        if item in jewelry_store:
            description = jewelry_store[item][0]
            print(f"Описание {item}: {description}")
        else:
            print("Такого изделия нет в магазине.")

    elif choice == '2':
        item = input("Введите название изделия: ")
        if item in jewelry_store:
            price = jewelry_store[item][1]
            print(f"Цена {item}: {price} рублей")
        else:
            print("Такого изделия нет в магазине.")

    elif choice == '3':
        item = input("Введите название изделия: ")
        if item in jewelry_store:
            quantity = jewelry_store[item][2]
            print(f"Количество {item} в наличии: {quantity} штук")
        else:
            print("Такого изделия нет в магазине.")

    elif choice == '4':
        print("Вся информация о ювелирных изделиях:")
        for item, details in jewelry_store.items():
            description, price, quantity = details
            print(f"{item}: Описание - {description}, Цена - {price} рублей, Количество - {quantity} штук")

    elif choice == '5':
        item = input("Введите название изделия для покупки (или 'n' для выхода): ")
        if item == 'n':
            break
        if item in jewelry_store:
            quantity = int(input(f"Введите количество {item} для покупки: "))
            if quantity <= jewelry_store[item][2]:
                total_price = quantity * jewelry_store[item][1]
                jewelry_store[item][2] -= quantity
                print(f"Покупка успешно совершена. Сумма к оплате: {total_price} рублей")
            else:
                print(f"Извините, недостаточно {item} в наличии.")
        else:
            print("Такого изделия нет в магазине.")

    elif choice == '6':
        print("До свидания!")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите пункт меню от 1 до 6.")
set1 = {1, 2, 3, 4, 7}
set2 = {4, 5, 6, 7, 9}
result = set1 - set2
if result:
    print("Элементы первого множества, которых нет во втором множестве:")
    for element in result:
        print(element)
else:
    print("Все элементы первого множества присутствуют во втором множестве.")
