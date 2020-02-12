from tkinter import *
import math

root = Tk()

titlePage = Label(root, text='Prime Factor', font=('Courier New',15,"bold")).pack()
frameOne=Frame(root)
Label(frameOne, text="Enter a number :", font=('Courier New',15)).pack(side='left')
entryInput=Entry(frameOne, font=('Courier New',15))
entryInput.pack(side='left')
frameOne.pack(side='top')

titlePage = Label(root, text='The prime factors are :', font=('Courier New',15,"bold")).pack()
def primeFactors(n):

    while n % 2 == 0: 
        print (2),
        Label(root, text=2, font=('Courier New',15,"bold")).pack()
        n = n / 2
         
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            print (i),
            Label(root, text=i, font=('Courier New',15,"bold")).pack()
            n = n / i 
            
    if n > 2: 
        print ( n )
        Label(root, text=n, font=('Courier New',15,"bold")).pack()
def submit():
    primeFactors(int(entryInput.get()))

btn=Button(root, text="Check", command=submit, font=('Courier New',15))
btn.pack()
root.mainloop()