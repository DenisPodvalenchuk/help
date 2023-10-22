import tkinter as tk
from tkinter import ttk
import numpy as np

def generate_matrix():
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())
    global matrix
    matrix = np.random.randint(1, 100, (rows, cols))
    matrix_label.config(text=str(matrix))

def find_max_product():
    details, result = compute_max_product(matrix)
    details_text = "\n".join(details)
    result_label.config(text=f"{details_text}\n\nМаксимальное произведение: {result}")

def compute_max_product(matrix):
    max_product = float('-inf')
    details = []
    for i in range(0, matrix.shape[0], 2):
        row = matrix[i]
        top1, top2 = sorted(row)[-2:]
        current_product = top1 * top2
        details.append(f"Строка {i+1}: [{', '.join(map(str, row))}] -> Наибольшие: {top1} и {top2}. Произведение: {current_product}")
        if current_product > max_product:
            max_product = current_product
    return details, max_product

app = tk.Tk()
app.title("Матричный калькулятор")

frame_input = ttk.Frame(app)
frame_input.pack(pady=20)

rows_label = ttk.Label(frame_input, text="Строки:")
rows_label.grid(row=0, column=0)
rows_entry = ttk.Entry(frame_input, width=5)
rows_entry.grid(row=0, column=1)

cols_label = ttk.Label(frame_input, text="Столбцы:")
cols_label.grid(row=0, column=2)
cols_entry = ttk.Entry(frame_input, width=5)
cols_entry.grid(row=0, column=3)

generate_button = ttk.Button(app, text="Сгенерировать матрицу", command=generate_matrix)
generate_button.pack(pady=20)

matrix_label = ttk.Label(app, text="")
matrix_label.pack(pady=20)

result_button = ttk.Button(app, text="Найти максимальное произведение", command=find_max_product)
result_button.pack(pady=20)

result_label = ttk.Label(app, text="")
result_label.pack(pady=20)

app.mainloop()

