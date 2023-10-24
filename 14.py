matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

min_product = float('inf')  # инициализируем начальное минимальное произведение как положительную бесконечность
min_product_elements = None  # переменные для хранения двух элементов с минимальным произведением
min_product_rows = []  # переменная для хранения строк с минимальными произведениями

for i in range(0, len(matrix), 2):  
    row = matrix[i]

    # Сортируем строку по возрастанию
    sorted_row = sorted(row)

    # Находим два наименьших элемента
    min1, min2 = sorted_row[:2]

    # Находим произведение этих элементов
    current_product = min1 * min2

    # Сравниваем с текущим минимальным произведением
    if current_product < min_product:
        min_product = current_product
        min_product_elements = (min1, min2)
        min_product_rows = row

print(f"Два наименьших элемента среди нечетных строк матрицы: {min_product_elements[0]} и {min_product_elements[1]}")
print(f"Минимальное произведение двух элементов среди нечетных строк матрицы: {min_product}")
print(f"Строки с минимальными произведениями двух элементов:\n{min_product_rows}")