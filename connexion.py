#importation des bibliothèques
from subprocess import call  #pour transiter entre les fenetres
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


#definition de la fenetre
root = Tk()
root.title("CONNEXION DE L'UTILISATEUR")  #definition du titre
root.geometry("400x300+450+200")  #fenetre de 400 de largeur et 300 de hauteur aux coordonnées k(450,200)
root.resizable(False,False)   #fenetre non reductible
root.configure(bg="#091821")   #Couleur

#Ajout de la bande superieure portant le titre
titre=Label(root,borderwidth=3,relief=SUNKEN,text="FORMULAIRE DE CONNEXION", font=("Times New Roman", 20), bg="#091821",fg="white")
titre.place(x=0,y=0,width=400)

lblnomutilisateur=Label(root,text="Nom utilisateur :", font=("Arial",15),bg="#091821",fg="white")
lblnomutilisateur.place(x=5,y=100,width=150)

txtnomutilisateur=Entry(root,bd=4,font=("Arial",12))
txtnomutilisateur.place(x=160,y=100,width=200, height=30)

#mot de passe
lblmdp=Label(root,text="Mot de passe :", font=("Arial",15),bg="#091821",fg="white")
lblmdp.place(x=5,y=150,width=150)

txtmdp=Entry(root,bd=4,font=("Arial",22, "bold"),show=".")
txtmdp.place(x=160,y=150,width=200, height=30)






#boucle
root.mainloop()