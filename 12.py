matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_product = float('-inf')  # инициализируем начальное максимальное произведение как отрицательную бесконечность
max_product_elements = None  # переменные для хранения двух элементов с максимальным произведением
max_product_row = []  # переменная для хранения строк с максимальными произведениями

for i in range(1, len(matrix), 2):  
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
        max_product_elements = (top1, top2)
        max_product_row = row

print(f"Два наибольших элемента среди четных строк матрицы: {max_product_elements[0]} и {max_product_elements[1]}")
print(f"Максимальное произведение двух элементов среди четных строк матрицы: {max_product}")
print(f"Строка с максимальным произведением двух элементов: {max_product_row}")