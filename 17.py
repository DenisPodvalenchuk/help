matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

min_product = float('inf')  # Инициализируем начальное минимальное произведение как положительную бесконечность

for j in range(0, len(matrix[0]), 2):  
    column = [matrix[i][j] for i in range(len(matrix))] 

    # Сортируем столбец по возрастанию
    sorted_column = sorted(column)

    # Находим два наименьших элемента
    min1, min2 = sorted_column[:2]

    # Находим произведение этих элементов
    current_product = min1 * min2

    # Сравниваем с текущим минимальным произведением
    if current_product < min_product:
        min_product = current_product

print(f"Два наименьших элемента среди четных столбцов матрицы: {min1} и {min2}")
print(f"Минимальное произведение двух элементов среди четных столбцов матрицы: {min_product}")