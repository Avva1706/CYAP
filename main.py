with open('Fzad11.txt', 'w') as file:
    print("Ввод данных в файл Fzad1,1.txt. Для завершения введите пустую строку.")
    while True:
        line = input()
        if not line:
            break
        file.write(line+'\n')
with open('Fzad11.txt', 'r') as write_file, open('Fzad12.txt', 'w') as copy_file:
    linia = write_file.readlines()
    second_linia = [line for index, line in enumerate(linia, start=1) if index % 2 == 0]
    copy_file.writelines(second_linia)
with open('Fzad11.txt', 'rb') as file:
    bytees1 = len(file.read())
with open('Fzad11.txt', 'rb') as file:
    bytees2 = len(file.read())
print(bytees1, "байт")
print(bytees2, "байт")