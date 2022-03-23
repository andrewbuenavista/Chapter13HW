import tkinter
from tkinter import font
import tkinter.messagebox

class pizzaOrder():

    def __init__(self):

        self.mainwindow = tkinter.Tk()
        self.mainwindow.config(bg='orange')
        self.mainwindow.title("Pizza Order")
        self.mainwindow.geometry('600x500')


        #frame creation and packing
        self.topframe1 = tkinter.Frame(self.mainwindow,bg='orange')
        self.topframe2 = tkinter.Frame(self.mainwindow,bg='orange')
        self.topframe3 = tkinter.Frame(self.mainwindow,bg='orange')
        self.midframe1 = tkinter.Frame(self.mainwindow,bg='orange')
        self.midframe2 = tkinter.Frame(self.mainwindow,bg='orange')
        self.bottomframe = tkinter.Frame(self.mainwindow,bg='orange')

        self.topframe1.pack()
        self.topframe2.pack()
        self.topframe3.pack()
        self.midframe1.pack(side='left')
        self.midframe2.pack(side='right')
        self.bottomframe.pack(side='bottom')

        #name/address label and entry including packing
        self.nameLabel = tkinter.Label(self.topframe1,text='Enter Name:',font=('Arial',24),bg='orange')
        self.nameEntry = tkinter.Entry(self.topframe1,width=25,font=('Arial',12),bg='orange')

        self.addLabel = tkinter.Label(self.topframe2,text='Enter Address:',font=('Arial',24),bg='orange')
        self.addDescr = tkinter.Label(self.topframe3,text='(street,city,state,zip)',font=('Arial',12),bg='orange')
        self.addEntry = tkinter.Entry(self.topframe2,width=40,font=('Arial',12),bg='orange')

        self.nameLabel.pack(side='left',anchor='w')
        self.nameEntry.pack(side='left',anchor='w')

        self.addLabel.pack(side='left',anchor='w')
        self.addEntry.pack(side='left',anchor='w')
        self.addDescr.pack(side='bottom')

        #crust type selection using radio buttons
        self.radioVar = tkinter.DoubleVar()
        self.radioVar.set(12)

        self.crustLabel = tkinter.Label(self.midframe1,text='Crust Options:',pady=20,font=('Arial',15),bg='orange')

        self.thinButton = tkinter.Radiobutton(self.midframe1,text='Thin Crust: $10',variable=self.radioVar,value=10,font=('Arial',12),bg='orange')
        self.regularButton = tkinter.Radiobutton(self.midframe1,text='Regular: $12',variable=self.radioVar,value=12,font=('Arial',12),bg='orange')
        self.deepdishButton = tkinter.Radiobutton(self.midframe1,text='Deep Dish: $15',variable=self.radioVar,value=15,font=('Arial',12),bg='orange')

        self.crustLabel.pack()
        self.regularButton.pack(anchor='w')
        self.thinButton.pack(anchor='w')
        self.deepdishButton.pack(anchor='w')

        #toppings
        self.toppingsLabel = tkinter.Label(self.midframe2,text='Toppings Options:',pady=20,font=('Arial',15),bg='orange')

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

        self.pC = tkinter.Checkbutton(self.midframe2,text='Pepperoni: $.25',variable=self.pCVar,font=('Arial',12),bg='orange')
        self.pnC = tkinter.Checkbutton(self.midframe2,text='Pineapple: $.25',variable=self.pnCVar,font=('Arial',12),bg='orange')
        self.mC = tkinter.Checkbutton(self.midframe2,text='Mushrooms: $.30',variable=self.mCVar,font=('Arial',12),bg='orange')
        self.sC = tkinter.Checkbutton(self.midframe2,text='Sausage: $.40',variable=self.sCVar,font=('Arial',12),bg='orange')
        self.jC = tkinter.Checkbutton(self.midframe2,text='Jalapeno: $.50',variable=self.jCVar,font=('Arial',12),bg='orange')

        self.toppingsLabel.pack()
        self.pC.pack(anchor='w')
        self.pnC.pack(anchor='w')
        self.mC.pack(anchor='w')
        self.sC.pack(anchor='w')
        self.jC.pack(anchor='w')

        #checkout and quit buttons

        self.checkoutButton = tkinter.Button(self.bottomframe,text='Checkout',command=self.calculate,height=3,width=18,bg='green')
        self.quitButton = tkinter.Button(self.bottomframe,text='Quit',command=self.mainwindow.destroy,height=3,width=18,bg='red')

        self.checkoutButton.pack(side='left')
        self.quitButton.pack(side='right',anchor='e')

        tkinter.mainloop()


    def calculate(self):
    
    #checks to ensure a name is entered, if not an error is returned
        if len(self.nameEntry.get()) != 0 and len(self.addEntry.get()) != 0:
            total = 0

            total += self.radioVar.get()

            orderDetails = ""

            if self.radioVar.get() == 10:
                orderDetails += 'Thin Crust' + '\n'
            elif self.radioVar.get() == 12:
                orderDetails += 'Regular' + '\n'
            else:
                orderDetails += 'Deep dish' + '\n'

            if self.pCVar.get() == 1:
                total += .25
                orderDetails += 'Pepperoni' + '\n'
            if self.pnCVar.get() == 1:
                total += .25
                orderDetails += 'Pineapple' + '\n'
            if self.mCVar.get() == 1:
                total += .3
                orderDetails += 'Mushrooms' + '\n'
            if self.sCVar.get() == 1:
                total += .4
                orderDetails += 'Sausage' + '\n'
            if self.jCVar.get() == 1:
                total += .5
                orderDetails += 'Jalapenos' + '\n'

            total = round(total,2)


            tkinter.messagebox.showinfo('Order Confirmation',self.nameEntry.get() +', your order is on the way!' + 
                                        '\n' + 'Will be delivered to: ' + self.addEntry.get() + '\n' + 'Total: $' + 
                                        str(total) +'\n' + "Order Details:" + '\n' + orderDetails)
        else:
            tkinter.messagebox.showerror('Invalid Order','Please enter a name & address before ordering.')

ourPizza = pizzaOrder()
        
