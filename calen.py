from tkinter import *
from tkcalendar import Calendar
from datetime import date

tk = Tk()
tk.title("Календарь")  
tk.geometry("700x700")  

current_date = date.today()
cal = Calendar(tk, selectmode = 'day',
               year = current_date.year,
               month = current_date.month,
               day = current_date.day)
cal.pack(pady=20, fill="both", expand=True) 

def grad_date():
    date.config(text="Selected Date is:"  + cal.get_date(), font="Arial")

Button(tk, text="Get Date",font="Arial", command=grad_date).pack(pady=20)

date = Label(tk, text="")
date.pack(pady=20)

tk.mainloop()

# bailiev XD