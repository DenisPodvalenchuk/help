matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_product = float('-inf')  # инициализируем начальное максимальное произведение как отрицательную бесконечность
max_product_row = []  # переменная для хранения строк с максимальными произведениями

for j in range(0, len(matrix[0]), 2):  
    column = [matrix[i][j] for i in range(len(matrix))]  # извлекаем нечетный столбец

    # Сортируем столбец по возрастанию
    sorted_column = sorted(column)

    # Находим два наибольших элемента
    top1, top2 = sorted_column[-2:]

    # Находим произведение этих элементов
    current_product = top1 * top2

    # Сравниваем с текущим максимальным произведением
    if current_product > max_product:
        max_product = current_product
        max_product_row = [matrix[i] for i in range(len(matrix))]  # Сохраняем строки с максимальными произведениями

print(f"Максимальное произведение двух элементов среди нечетных столбцов матрицы: {max_product}")
print(f"Строки с максимальными произведениями двух элементов:\n{max_product_row}")