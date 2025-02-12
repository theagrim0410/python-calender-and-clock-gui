from tkinter import *
import calendar
import datetime
import time


root = Tk()
root.title("Calendar with Digital Clock")
root.geometry("400x570")
root.configure(bg="#2C3E50") 

def center_widget(widget, relx, rely):
    widget.place(relx=relx, rely=rely, anchor="center")

def show():
    try:
        months = int(entry1.get())
        years = int(entry2.get())

        if not (1 <= months <= 12):
            cal = "Month must be between 1-12!"
        elif not (1800 <= years <= 9999):
            cal = "Year must be between 1800-9999!"
        else:
            cal = calendar.month(years, months)

    except ValueError:
        cal = "Invalid Input! Please enter numbers."

    txt.config(state='normal')
    txt.delete(1.0, END)
    txt.insert(INSERT, cal)
    txt.config(state='disabled')


def end():
    now = datetime.datetime.now()
    hour = now.hour

    if 4 <= hour < 12:
        greeting = "Good Morning! "
    elif 12 <= hour < 16:
        greeting = "Good Afternoon! "
    elif 16 <= hour < 20:
        greeting = "Good Evening! "
    else:
        greeting = "Good Night! "

    message_label.config(text=f"{greeting}\nThank You for Using the Calendar!", fg="cyan")


def close():
    root.destroy()


def update_clock():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)  

Label(root, text="Month (1-12):", font=("Arial", 10, "bold"), fg="white", bg="#2C3E50").place(relx=0.4, rely=0.1, anchor="center")
Label(root, text="Year (1800-9999):", font=("Arial", 10, "bold"), fg="white", bg="#2C3E50").place(relx=0.4, rely=0.2, anchor="center")


entry1 = Entry(root, width=5, font=("Arial", 12))
center_widget(entry1, 0.65, 0.1)

entry2 = Entry(root, width=7, font=("Arial", 12))
center_widget(entry2, 0.65, 0.2)


show_btn = Button(root, text="Show Calendar", command=show, bg="#27AE60", fg="white", font=("Arial", 10, "bold"), width=15)
center_widget(show_btn, 0.5, 0.3)


txt = Text(root, width=20, height=8, font=("Arial", 10), fg="#2C3E50", bg="white", state='disabled')
center_widget(txt, 0.5, 0.5)


end_btn = Button(root, text="End", command=end, bg="#3498DB", fg="white", font=("Arial", 10, "bold"), width=12)
center_widget(end_btn, 0.3, 0.75)


close_btn = Button(root, text="Close", command=close, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"), width=12)
center_widget(close_btn, 0.7, 0.75)


clock_btn = Button(root, text="Show Clock", command=update_clock, bg="#F39C12", fg="white", font=("Arial", 10, "bold"), width=12)
center_widget(clock_btn, 0.5, 0.85)


message_label = Label(root, text="", font=("Arial", 12, "bold"), fg="cyan", bg="#2C3E50")
center_widget(message_label, 0.5, 0.92)

clock_label = Label(root, text="", font=("Arial", 14, "bold"), fg="yellow", bg="#2C3E50")
center_widget(clock_label, 0.5, 0.98)

root.mainloop()
