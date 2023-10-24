matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

min_product = float('inf')  # инициализируем начальное минимальное произведение как положительную бесконечность
min_product_elements = None  # переменные для хранения двух элементов с минимальным произведением
min_product_columns = []  # переменная для хранения нечетных столбцов

for j in range(0, len(matrix[0]), 2):  
    column = [matrix[i][j] for i in range(len(matrix))]
    min_product_columns.append(column)

    # Сортируем столбец по возрастанию
    sorted_column = sorted(column)

    # Находим два наименьших элемента
    min1, min2 = sorted_column[:2]

    # Находим произведение этих элементов
    current_product = min1 * min2

    # Сравниваем с текущим минимальным произведением
    if current_product < min_product:
        min_product = current_product
        min_product_elements = (min1, min2)

print(f"Два наименьших элемента среди нечетных столбцов матрицы: {min_product_elements[0]} и {min_product_elements[1]}")
print(f"Минимальное произведение двух элементов среди нечетных столбцов матрицы: {min_product}")

print("Нечетные столбцы:")
for column in min_product_columns:
    print(column)