try:
    from Calc.calculator.calc import *
except:
    print("Nie udalo sie zaimportowac pakietu Calc")

try:
    from tkinter import *
except:
    print("Nie udalo sie zaimportowac pakietu tkinter")

class TestCalc(Frame):
    """ Klasa do testowania kalkulatora. """
    def __init__(self, master_obj):
        super(TestCalc, self).__init__(master_obj)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label_class = Label(self, text="Sprawdzam ladowanie\n klasy Calc")
        self.label_class.grid()
        self.button_class = Button(self, text="sprawdz", bg="green")
        self.button_class.grid()
        self.button_class["command"] = self.loadCalkClass()

        self.label2 = Label(self, text="...")
        self.label2.grid()
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text="...")

        self.label3 = Label(self, text="...")
        self.label3.grid()
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "..."

    def loadCalkClass(self):
        #pass
        #self.button_class.configure(bg="red")
        #calkus = Calc()
        try:
            calk = Calc()
        except:
            self.button_class.configure(bg="red")
        else:
            self.button_class.configure(bg="green")



root = Tk()
root.title("TDD Calc")
root.geometry("750x750")

#app = Frame(root)
#app.grid()
#label_class = Label(app, text="Sprawdzam ladowanie\n klasy Calk")
#lbl.grid()
#button_class = Button(app, text = "sprawdz")
#button_class.grid()

tdd_test = TestCalc(root)

root.mainloop()