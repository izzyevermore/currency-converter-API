from tkinter import *
import requests
from tkinter import ttk


window = Tk()
window.title("Currency Converter")
window.geometry("700x500")
window.config(bg="green")

amount = IntVar()

repsonse = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
responsej = repsonse.json()

conversion_rate = responsej['conversion_rates']
print(conversion_rate)


# Creating the amount convertable label and entry
amount_label = Label(window, text="Amount", font=("Comic Sans MS", 20), width=20, bg="light blue")
amount_label.place(x=0, y=0)

amount_entry = Entry(window, textvariable=amount, width=40)
amount_entry.place(x=300, y=6)

# Creating the FROM (Standard amount is USD)

from_label = Label(window, text="From: USD", font=("Comic Sans MS", 20), width=40, bg="light blue")
from_label.place(x=130, y=50)

# Creating the conversion rates listbox

convert = Label(window, text="TO:", font=("Comic Sans MS", 20), bg="light blue")
convert.place(x=0, y=150)

convert_list = Listbox(window, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.place(x=50, y=150)

# Creating label to display converted amount

convert_label = Label(window, text="Converted to: ", font=("Comic Sans MS", 20), bg="light blue")
convert_label.place(x=0, y=450)

# Creating the button that converts the currency as inputed

def convert_curr():
    num = float(amount_entry.get())
    print(responsej['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num*responsej['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = ans

convert_btn = Button(window, command=convert_curr, text="Convert", font=("Comic Sans MS", 20), width=20)
convert_btn.place(x=10, y=350)


window.mainloop()