
from tkinter import *
from tkinter import filedialog
def Savefile():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
def clear():
    entry.delete(1.0,END)

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
        entry.delete(1.0,END)
        entry.insert(INSERT,content)


root=Tk()
#wrapper=LabelFrame(root,text='Notepad')
#wrapper.pack(fill='both',expand='yes',padx=10,pady=10)
root.title("Notepad.........")
root.geometry('500x600')
root.resizable(False,False)




b1=Button(root,text="Save",command=Savefile)
b1.place(x=10,y=10)#(side=tk.LEFT,padx=30)
b2=Button(root,text="Clear",command=clear)
b2.place(x=70,y=10)
b2=Button(root,text="Open file",command=open_file)
b2.place(x=120,y=10)


entry=Text(root,height=33,width=58,wrap=WORD)
entry.place(x=10,y=50)




root.mainloop()
