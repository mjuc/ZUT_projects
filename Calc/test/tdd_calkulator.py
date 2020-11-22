try:
    from Calc import calculator
except:
    print("Nie udalo sie zaimportowac pakietu calculator")

try:
    from tkinter import *
except:
    print("Nie udalo sie zaimportowac pakietu tkinter")

root = Tk()
root.title("TDD calculator")
root.geometry("750x750")
root.mainloop()




