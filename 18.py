matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_product = float('-inf')  # Инициализируем начальное максимальное произведение как отрицательную бесконечность

for i in range(0, len(matrix), 2): 
    row = matrix[i]

    # Сортируем строку по возрастанию
    sorted_row = sorted(row)

    # Находим два наибольших элемента
    max1, max2 = sorted_row[-2:]

    # Находим произведение этих элементов
    current_product = max1 * max2

    # Сравниваем с текущим максимальным произведением
    if current_product > max_product:
        max_product = current_product

print(f"Два наибольших элемента среди нечетных строк матрицы: {max1} и {max2}")
print(f"Максимальное произведение двух элементов среди нечетных строк матрицы: {max_product}")