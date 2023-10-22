import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

# Основная функция поиска значения
def find_max_product(matrix):
    max_product = float('-inf')
    
    # Находим нечетные строки матрицы
    for i in range(0, matrix.shape[0], 2):
        row = matrix[i]
        
        # Выводим строку и её номера
        print(f"Строка {i+1}: {row}")
        
        # Находим два наибольших элемента в строке и их произведение
        top1, top2 = sorted(row)[-2:]
        current_product = top1 * top2
        print(f"Наибольшие элементы: {top1} и {top2}. Их произведение: {current_product}")
        
        # Сравниваем значения строк и обновляем максимальное произведение
        if current_product > max_product:
            max_product = current_product
            print(f"Новое максимальное произведение: {max_product}\n")
        else:
            print(f"Текущее максимальное произведение остается неизменным: {max_product}\n")
            
    return max_product

def main():
    # Создаем базовое окно
    root = tk.Tk()
    root.withdraw() # Это скрывает основное окно
    
    # Запрашиваем размерность матрицы
    rows = simpledialog.askinteger("Ввод размерности", "Количество строк:")
    cols = simpledialog.askinteger("Ввод размерности", "Количество столбцов:")

    # Создаем случайную матрицу
    matrix = np.random.randint(1, 100, (rows, cols))
    print("Сгенерированная матрица:")
    print(matrix)

    # Вычисляем и выводим результат
    result = find_max_product(matrix)
    messagebox.showinfo("Результат", f"Максимальное произведение: {result}")

    root.destroy()

if __name__ == '__main__':
    main()
