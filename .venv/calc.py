import tkinter as tk



def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)



def per():
    num1, num2 = get_values()
    res = (num2 / num1) * 100
    insert_values(res)


window = tk.Tk()
window.title('Счетная машина')
window.geometry("400x400")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=5, height=2, command=add,bg='blue')
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="-", width=5, height=2, command=sub, bg='blue')
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=5, height=2, command=mul, bg='blue')
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=5, height=2, command=div, bg='blue')
button_div.place(x=250, y=200)
button_per = tk.Button(window, text='%', width=5, height=2, command=per, bg='blue')
button_per.place(x=300, y=200)
number1_entry = tk.Entry(window, width=32)
number1_entry.place(x=100, y=90)
number2_entry = tk.Entry(window, width=32)
number2_entry.place(x=100, y=165)
answer_entry = tk.Entry(window, width=32)
answer_entry.place(x=100, y=315)
number1 = tk.Label(window, text="Введите первое число:", font=("Helvetica", "13", "italic"))
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:", font=("Helvetica", "13", "italic"))
number2.place(x=100, y=125)
answer = tk.Label(window, text="Результат:", font=("Helvetica", "13", "italic"))
answer.place(x=100, y=275)
window.mainloop()

