from tkinter import *
import math

class calc():

    def __init__(self):
        self.total = 0
        self.current = ""
        self.op = ""
        self.result = False
        self.input_value = True
        self.check_sum = False
    
    
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)

    
    def enternumber(self,num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)

        if self.input_value :
            self.current = secondnum
            self.input_value = False
        
        else :
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum+ secondnum
        self.display(self.current)

    def is_equal_to(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else :
            self.total = float(txtDisplay.get())
 
    def valid_function(self):
        if self.op == "add":
            self.total+=self.current
        elif self.op == "sub":
            self.total-=self.current
        elif self.op == "Mul":
            self.total *= self.current
        elif self.op == "Div":
            self.total/=self.current
            
        self.check_sum = False
        self.input_value = True
        self.display(self.total)

    
    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum :
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True

        self.check_sum = True
        self.op = op
        self.result = False


    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)


    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0


    def opPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)


    def squareroot(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)


root = Tk()
added_value = calc()
root.title("Calculator")
calc = Frame(root)
root.resizable(width =False,height =False)
calc.grid()

#====================================================ROW0============================================================
txtDisplay = Entry(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",width = 18,bd = 5,justify = RIGHT)
txtDisplay.grid(row = 0, column = 0,columnspan = 4)
txtDisplay.insert(0,"0")

#====================================================ROW1============================================================
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "CE",width = 4,height=1,pady = 1,command = added_value.all_clear_entry).grid(row = 1,column = 0)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "C",width = 4,height=1,pady = 1,command = added_value.clear_entry).grid(row = 1,column = 1)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "√",width = 4,height=1,pady = 1,command = added_value.squareroot).grid(row = 1,column = 2)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "+",width = 4,height=1,pady = 1,command = lambda:added_value.operation("add")).grid(row = 1,column = 3)

#====================================================ROW2============================================================
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "7",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(7)).grid(row = 2,column = 0)
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "8",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(8)).grid(row = 2,column = 1)
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "9",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(9)).grid(row = 2,column = 2)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "-",width = 4,height=1,pady = 1,command = lambda:added_value.operation("sub")).grid(row = 2,column = 3)

#====================================================ROW3============================================================
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "4",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(4)).grid(row = 3,column = 0)
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "5",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(5)).grid(row = 3,column = 1)
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "6",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(6)).grid(row = 3,column = 2)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "X",width = 4,height=1,pady = 1,command = lambda:added_value.operation("Mul")).grid(row = 3,column = 3)

#====================================================ROW4============================================================
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "1",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(1)).grid(row = 4,column = 0)
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "2",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(2)).grid(row = 4,column = 1)
Button(calc,font = ("Times new roman",20,"bold"),bg = "light salmon",fg = "snow",text = "3",width = 4,height = 1,pady= 1,command = lambda:added_value.enternumber(3)).grid(row = 4,column = 2)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "/",width = 4,height=1,pady = 1,command = lambda:added_value.operation("Div")).grid(row = 4,column = 3)

#====================================================ROW5============================================================
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = ".",width = 4,height=1,pady = 1,command = lambda:added_value.enternumber('.')).grid(row = 5,column = 0)
Button(calc,font = ("MV Boli",20,"bold"),bg = "light salmon",fg = "snow",text = "0",width = 4,height=1,pady = 1,command = lambda:added_value.enternumber("0")).grid(row = 5,column = 1)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "+/-",width = 4,height=1,pady = 1,command = added_value.opPM).grid(row = 5,column = 2)
Button(calc,font = ("MV Boli",20,"bold"),bg = "snow",fg = "red",text = "=",width = 4,height=1,pady = 1,command = added_value.is_equal_to).grid(row = 5,column = 3)

root.mainloop()