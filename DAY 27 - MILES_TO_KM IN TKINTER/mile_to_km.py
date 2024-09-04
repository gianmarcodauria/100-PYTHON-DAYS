from tkinter import *

def calculate_button_clicked():
    num = input.get()
    res = 0
    res = round(float(num) * 1.6093445)
    new_label_result["text"] = res

#window
new_window = Tk()
new_window.title("Mile to Km Converter")
new_window.minsize(width=500, height=300)
new_window.config(padx=50, height=50)

#entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

#label
new_label_is_equal = Label(text="is equal to", font=("Arial", 24, "bold"))
new_label_is_equal.grid(column=0, row=1)
new_label_is_equal.config(padx=5, pady=5)

new_label_result = Label(text=0, font=("Arial", 24, "bold"))
new_label_result.grid(column=1, row=1)
new_label_result.config(padx=5, pady=5)

new_label_miles = Label(text="Miles", font=("Arial", 24, "bold"))
new_label_miles.grid(column=2, row=0)
new_label_miles.config(padx=5, pady=5)

new_label_km = Label(text="Km", font=("Arial", 24, "bold"))
new_label_km.grid(column=2, row=1)
new_label_km.config(padx=5, pady=5)

#button
button = Button(text="Calculate", command=calculate_button_clicked) # name of the funct, no () needed
button.grid(column=1, row=2)

new_window.mainloop()