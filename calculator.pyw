global screen,calculation
calculation = ""

def clr():
    global screen,calculation
    screen.config(text=':)')
    calculation = ""

def addStr(thing):
     global screen,calculation
     calculation += str(thing)
     screen.config(text=calculation)

def calc():
    global screen,calculation
    screen.config(text=eval(calculation))
    calculation = ""
    
import tkinter
top = tkinter.Tk()
top.title("Calculator")
top.geometry("180x212")
A = tkinter.Button(width=5, height = 2, text ="1", command = lambda : addStr('1')).place(x=0,y=50)
B = tkinter.Button(width=5, height = 2, text ="2", command = lambda : addStr('2')).place(x=0,y=90)
C = tkinter.Button(width=5, height = 2, text ="3", command = lambda : addStr('3')).place(x=0,y=130)
D = tkinter.Button(width=5, height = 2, text ="4", command = lambda : addStr('4')).place(x=45,y=50)
E = tkinter.Button(width=5, height = 2, text ="5", command = lambda : addStr('5')).place(x=45,y=90)
F = tkinter.Button(width=5, height = 2, text ="6", command = lambda : addStr('6')).place(x=45,y=130)
G = tkinter.Button(width=5, height = 2, text ="7", command = lambda : addStr('7')).place(x=90,y=50)
H = tkinter.Button(width=5, height = 2, text ="8", command = lambda : addStr('8')).place(x=90,y=90)
I = tkinter.Button(width=5, height = 2, text ="9", command = lambda : addStr('9')).place(x=90,y=130)
J = tkinter.Button(width=5, height = 2, text ="0", command = lambda : addStr('0')).place(x=0,y=171)
K = tkinter.Button(width=5, height = 2, text ="+", command = lambda : addStr('+')).place(x=45,y=171)
M = tkinter.Button(width=5, height = 2, text ="-", command = lambda : addStr('-')).place(x=90,y=171)
div = tkinter.Button(width=5, height = 2, text ="%", command = lambda : addStr('/')).place(x=135,y=90)
mult = tkinter.Button(width=5, height = 2, text ="x", command = lambda : addStr('*')).place(x=135,y=50)
eq = tkinter.Button(width=5, height = 2, text ="=", command = lambda : calc()).place(x=135,y=130)
dl = tkinter.Button(width=5, height = 2, text ="CLR", command = lambda : clr()).place(x=135,y=171)
screen = tkinter.Label(width = 15,height = 2,text = ":)")
screen.pack()
top.mainloop()
