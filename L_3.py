def main(file_name):
    symbols = ["(", ".", ":"]  # Тире и точка как символы для кодирования 1

    with open(file_name, "r") as file_text:
        lines = file_text.readlines()

    bit_arrays = []

    for line in lines:
        bit_array = []  # Создаем массив битов для текущей строки
        for char in line:
            if char in symbols:
                bit_array.append(1)  # Если символ в symbols, добавляем 1
            else:
                bit_array.append(0)  # Иначе добавляем 0
        bit_arrays.append(bit_array)  # Добавляем массив битов в общий список

    stegan_preo = []
    stegan_no_preo = []

    for index, bits in enumerate(bit_arrays):
        result = any(bits)  # Проверяем наличие хотя бы одной единицы в bits
        if result:
            print("№{} Строка| Есть преобразования в тексте: {}".format(index + 1, lines[index][:-1]))
            stegan_preo.append(lines[index])
            lines[index] = "Стеганографические преобразования | " + lines[index]  # Добавляем пометку в строку
        else:
            print("№{} Строка | Нет преобразований в тексте: {}".format(index + 1, lines[index][:-1]))
            stegan_no_preo.append(lines[index])

    with open(file_name + "_marked.txt", "w") as marked_file:  # Записываем помеченные строки в новый файл
        marked_file.writelines(lines)

    print("--------------------------------------------")
    print("Преобразования в тексте: {}".format(len(stegan_preo)))
    print("Преобразования в тексте отсутствуют: {}".format(len(stegan_no_preo)))

if __name__ == "__main__":
    print("Метод сокрытия:")
    main(r"D:\share\.Course_5\Стеганография\L_3\L_3.txt")
