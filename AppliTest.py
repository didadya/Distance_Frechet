# Appli test (interface graphique)
from tkinter import *

fenetre = Tk()
fenetre.geometry("500x340")

def affichage(tempsExec, dist):
    champ_label1 = Label(fenetre, text="Temps de reponse :")
    champ_label1.grid(row=2, column=0, padx=40, pady=40)
    champ_label2 = Label(fenetre, text=tempsExec)
    champ_label2.grid(row=2, column=1, padx=40, pady=40)
    champ_label3 = Label(fenetre, text="Distance de Frechet :")
    champ_label3.grid(row=3, column=0, padx=40, pady=5)
    champ_label4 = Label(fenetre, text=dist)
    champ_label4.grid(row=3, column=1, padx=40, pady=5)

def discret2Traj():
    affichage(342, 3.34424)
    
def discretCsv():
    test = "test"
   
def continue2Traj():
    test = "test"
   
def continueCsv():
    test = "test"
   

BD1 = Button(fenetre, text ="Discret 2 Traj", width=25, command = discret2Traj)
BD1.grid(row=0, column=0, padx=40, pady=20)

BD2 = Button(fenetre, text ="Discret Csv", width=25, command = discretCsv)
BD2.grid(row=1, column=0, padx=25, pady=5)

BC1 = Button(fenetre, text ="Continue 2 Traj", width=25, command = continue2Traj)
BC1.grid(row=0, column=1, padx=5, pady=5)

BC2 = Button(fenetre, text ="Continue Cvs", width=25, command = continueCsv)
BC2.grid(row=1, column=1, padx=5, pady=5)



fenetre.mainloop()