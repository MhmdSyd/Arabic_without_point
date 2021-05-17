# import Require Modules
from tkinter import *
import pyperclip as pc
import json
import os 

# change directory to project file directory.
os.chdir(os.path.dirname(__file__))

# read json file that has transform letter.
def readJson():
    # read transform letter Dictionary.
    myfile = open("transform_dict.json", "r", encoding="utf-8")
    return json.load(myfile)[0]

# button 1 call this method to transform letter without dots.
def transform():
    # read text from text box 1.
    inputValue = t1.get("1.0",'end-1c') 
    inputValue = inputValue + " "
    # clear content from textbox2.
    t2.delete("1.0",END) 
    # read json dictionary and store it in mydict.
    mydict = readJson()
    # loop for all letter to check that is letter is in dictionary to transform it or not.
    for i in range(len(inputValue)):
        # check where letter noun in word to decided if i replace it or not 
        if inputValue[i] == noun.decode("utf-8") and (inputValue[i+1] != " " and inputValue[i+1] != "\n"):
            y = baq.decode("utf-8")
        else:
            y = inputValue[i]

        if y in mydict.keys():
            # True condition: transform letter.
            t2.insert(INSERT,mydict[y])
        else:
            # False condition: don't transform.
            t2.insert(INSERT,y)
# this method use to clear textbox1 then paste text which you copy in textbox1.
def pasteText():
    t1.delete("1.0",END)
    t1.insert(INSERT,pc.paste())

# this method use to get transform text from textbox2 and then take copy.
def copyText():
    inputVal = t2.get("1.0",'end-1c')
    pc.copy(inputVal)

def reset():
    t1.delete("1.0",END)
    t2.delete("1.0",END)

# start of main code.
if __name__ == "__main__":
    # letter baq and noun encoding in utf-8
    noun = b'\xd9\x86'
    baq = b'\xd8\xa8'
    # create frame of window GUI
    window = Tk()
    window.title("Arabic_without_point")
    window.geometry("600x300")
    window.resizable(width=False,height=False)
    # textbox1 use to put text which you need to transform.
    t1 = Text(window, width=32,height=15)
    t1.grid(row=1,column=1)
    # this button use to transform text to Arabic without dots.
    b1 = Button(window,text="submit",width=8, height=2, command=lambda: transform())
    b1.grid(row=1, column=2)
    # textbox2 is use to print and show text after transform.
    t2 = Text(window, width=32,height=15)
    t2.grid(row=1,column=3)
    # buttton use to paste the content which you want to transform.
    b2 = Button(window,text="paste",width=8, height=2, command=lambda: pasteText())
    b2.grid(row=2, column=1)
    # butto that copy text after transform.
    b3 = Button(window,text="copy",width=8, height=2, command=lambda: copyText())
    b3.grid(row=2, column=3)
    # butto that clear text from textbox1 and textbox2.
    b3 = Button(window,text="reset",width=8, height=2, command=lambda: reset())
    b3.grid(row=2, column=2)

    window.mainloop()
