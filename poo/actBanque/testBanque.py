import compte as c
import banque as b
import json as j
import fenVirement

# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Add a Treeview widget
tree= ttk.Treeview(win, column=("c1", "c2","c3"), show= 'headings')
tree.column("# 1",anchor=CENTER)
tree.heading("# 1", text= "ID")
tree.column("# 2", anchor= CENTER)
tree.heading("# 2", text= "Nom")
tree.column("# 3", anchor= CENTER)
tree.heading("# 3", text="Solde")



bank = b.Banque()

bank.createCompte("Ruffin")
bank.createCompte("Boyard")
bank.createCompte("Panot")
bank.createCompte("Martinez")

bank.getCompteByNom("Ruffin").credit(250)
bank.getCompteByNom("Boyard").credit(360)
bank.getCompteByNom("Panot").credit(4825)
bank.getCompteByNom("Martinez").credit(587)

gTab = bank.getTab()
for i in range(len(gTab)):
    tree.insert('', 'end',text= "1",values=(i, gTab[i][0],gTab[i][1]))
# Insert the data in Treeview widget

tree.pack()

labl_1 = Label(win, text="FullName",width=20,font=("bold", 10))  
labl_1.place(x=80,y=280)  
  
entry_1 = Entry(win)  
entry_1.place(x=240,y=280)  


labl_2 = Label(win, text="Credit",width=20,font=("bold", 10))  
labl_2.place(x=80,y=300)  
  
entry_2 = Entry(win)  
entry_2.place(x=240,y=300)  

def helloCallBack():
    tree.insert('', 'end',text= "1",values=("1", entry_1.get(), entry_2.get()))
    msg=messagebox.showinfo( "Information", "Ajoute avec succès")

def handler(e):
    tree.insert('', 'end',text= "1",values=("1", entry_1.get(), entry_2.get()))
    msg=messagebox.showinfo( "Information", "Ajoute avec succès")
def virement():
    fenVirement.open(bank, bank.getCompteByNom(tree.focus().values[1]))

B = Button(win, text ="Ajouter", command = helloCallBack)

B.place(x=500,y=300)

B2 = Button(win, text ="Virement", command = virement)

B2.place(x=500,y=280)

win.bind('<Return>', handler)


win.mainloop()
print(j.dumps(bank.getTab()))