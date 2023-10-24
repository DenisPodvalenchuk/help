matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_product = float('-inf')  # инициализируем начальное максимальное произведение как отрицательную бесконечность
max_product_elements = None  # переменные для хранения двух элементов с максимальным произведением
even_columns = [] # Список для хранения четных столбцов

for j in range(1, len(matrix[0]), 2):  
    column = [matrix[i][j] for i in range(len(matrix))]  # извлекаем четный столбец
    even_columns.append(column)

    # Сортируем столбец по возрастанию
    sorted_column = sorted(column)

    # Находим два наибольших элемента
    top1, top2 = sorted_column[-2:]

    # Находим произведение этих элементов
    current_product = top1 * top2

    # Сравниваем с текущим максимальным произведением
    if current_product > max_product:
        max_product = current_product
        max_product_elements = (top1, top2)

print(f"Два наибольших элемента среди четных столбцов матрицы: {max_product_elements[0]} и {max_product_elements[1]}")
print(f"Максимальное произведение двух элементов среди четных столбцов матрицы: {max_product}")

print("Четные столбцы:")
for column in even_columns:
    print(column)