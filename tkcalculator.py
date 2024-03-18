import tkinter
from tkinter import *

window = tkinter.Tk()
window.geometry("500x400")
# label = tkinter.Label(window, text="hello world")
# label.pack(padx=20, pady=40)

inputField = tkinter.Entry(window, width=40, borderwidth=1)
inputField.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(btn_text):
    current = inputField.get()
    inputField.delete(0, tkinter.END)
    inputField.insert(0, str(current) + str(btn_text))
    if btn_text == 'AC':
        inputField.delete(0, tkinter.END)
    if btn_text == '=':
        # try:
            result = str(eval(inputField.get()))
            inputField.delete(0, tkinter.END)
            inputField.set(result)
        # except Exception as e:
        #     inputField.delete(0, tkinter.END)
        #     inputField.insert(0, 'Error')


button_texts = ["AC", "+|-", "%", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ",", "=", ""]
button = tkinter.Button(window, text=button_texts[2], padx=50, pady=40)

buttons = [tkinter.Button(window, text=button_text, padx=40, pady=20, width=1, height=1, borderwidth=2, command=lambda bt=button_text : button_click(bt)) for button_text in button_texts ]

i = 0
for row in range(5):
  for column in range(4):
    buttons[i].grid(row=row + 3, column=column)
    i += 1


# button.grid(row=3, column=0)

window.mainloop()