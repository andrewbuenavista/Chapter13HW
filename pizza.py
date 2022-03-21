import tkinter
import tkinter.messagebox

class pizzaOrder():

    def __init__(self):

        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Pizza Order")
        self.mainwindow.geometry('350x350')

        #frame creation and packing
        self.topframe = tkinter.Frame(self.mainwindow)
        self.midframe1 = tkinter.Frame(self.mainwindow)
        self.midframe2 = tkinter.Frame(self.mainwindow)
        self.bottomframe = tkinter.Frame(self.mainwindow)

        self.topframe.pack()
        self.midframe1.pack(side='left')
        self.midframe2.pack(side='right')
        self.bottomframe.pack(side='bottom')

        #name label and entry including packing
        self.nameLabel = tkinter.Label(self.topframe,text='Enter Name:')
        self.nameEntry = tkinter.Entry(self.topframe,width=30)

        self.nameLabel.pack(side='left')
        self.nameEntry.pack(side='left')

        #crust type selection using radio buttons
        self.radioVar = tkinter.DoubleVar()
        self.radioVar.set(12)

        self.crustLabel = tkinter.Label(self.midframe1,text='Crust Options:')
        self.thinButton = tkinter.Radiobutton(self.midframe1,text='Thin Crust: $10',variable=self.radioVar,value=10)
        self.regularButton = tkinter.Radiobutton(self.midframe1,text='Regular: $12',variable=self.radioVar,value=12)
        self.deepdishButton = tkinter.Radiobutton(self.midframe1,text='Deep Dish: $15',variable=self.radioVar,value=15)

        self.crustLabel.pack()
        self.regularButton.pack()
        self.thinButton.pack()
        self.deepdishButton.pack()

        #toppings
        self.toppingsLabel = tkinter.Label(self.midframe2,text='Toppings:')

        self.pCVar = tkinter.DoubleVar()
        self.pnCVar = tkinter.DoubleVar()
        self.mCVar = tkinter.DoubleVar()
        self.sCVar = tkinter.DoubleVar()
        self.jCVar = tkinter.DoubleVar()

        self.pCVar.set(0)
        self.pnCVar.set(0)
        self.mCVar.set(0)
        self.sCVar.set(0)
        self.jCVar.set(0)

        self.pC = tkinter.Checkbutton(self.midframe2,text='Pepperoni: $.25',variable=self.pCVar)
        self.pnC = tkinter.Checkbutton(self.midframe2,text='Pineapple: $.25',variable=self.pnCVar)
        self.mC = tkinter.Checkbutton(self.midframe2,text='Mushrooms: $.30',variable=self.mCVar)
        self.sC = tkinter.Checkbutton(self.midframe2,text='Sausage: $.40',variable=self.sCVar)
        self.jC = tkinter.Checkbutton(self.midframe2,text='Jalapeno: $.50',variable=self.jCVar)

        self.toppingsLabel.pack()
        self.pC.pack()
        self.pnC.pack()
        self.mC.pack()
        self.sC.pack()
        self.jC.pack()

        #checkout and quit buttons

        self.checkoutButton = tkinter.Button(self.bottomframe,text='Checkout',command=self.calculate)
        self.quitButton = tkinter.Button(self.bottomframe,text='Quit',command=self.mainwindow.destroy)

        self.checkoutButton.pack(side='left')
        self.quitButton.pack(side='right')

        tkinter.mainloop()


    def calculate(self):
    
        if len(self.nameEntry.get()) != 0:
            total = 0

            total += self.radioVar.get()

            if self.pCVar.get() == 1:
                total += .25
            if self.pnCVar.get() == 1:
                total += .25
            if self.mCVar.get() == 1:
                total += .3
            if self.sCVar.get() == 1:
                total += .4
            if self.jCVar.get() == 1:
                total += .5

            total = round(total,2)

            tkinter.messagebox.showinfo('Order Confirmation',self.nameEntry.get() +', your order is on the way!' + 
                                        '\n' + 'Total: $' + str(total))
        else:
            tkinter.messagebox.showerror('Invalid Order','Please enter a name before ordering.')

ourPizza = pizzaOrder()
        
