matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_product = float('-inf')  # инициализируем начальное максимальное произведение как отрицательную бесконечность
top1, top2 = None, None  

for i in range(0, len(matrix), 2):
    row = matrix[i]
    
    # Сортируем строку по возрастанию
    sorted_row = sorted(row)
    
    # Находим два наибольших элемента
    top1, top2 = sorted_row[-2:]
    
    # Находим произведение этих элементов
    current_product = top1 * top2
    
    # Сравниваем с текущим максимальным произведением
    if current_product > max_product:
        max_product = current_product
        max_product_row = row  # Сохраняем строку с максимальным произведением

print(f"Строка с двумя наибольшими элементами среди нечетных строк матрицы: {max_product_row}")
print(f"Два наибольших элемента среди нечетных строк матрицы: {top1} и {top2}")
print(f"Максимальное произведение двух элементов среди нечетных строк матрицы: {max_product}")