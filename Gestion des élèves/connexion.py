#importation des bibliothèques
from subprocess import call  #pour transiter entre les fenetres
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


#connexion à la fenêtre
def Seconnecter():
    nom=txtnomutilisateur.get()
    mdp=txtmdp.get()
    if(nom=="" and mdp==""):
        messagebox.showerror('',"Entrez les informations correctes")
    elif(nom=="admin" and mdp=="admin"):
        messagebox.showinfo('',"Infos utilisateurs correctes")
        txtnomutilisateur.delete('0','end')
        txtmdp.delete('0','end')
        root.destroy()
        call(['python', 'principal.py'])
    else:
        messagebox.showwarning('',"Identifiants Invalides")
        txtnomutilisateur.delete('0','end')
        txtmdp.delete('0','end')



#definition de la fenetre
root = Tk()
root.title("CONNEXION DE L'UTILISATEUR")  #definition du titre
root.geometry("400x300+450+200")  #fenetre de 400 de largeur et 300 de hauteur aux coordonnées k(450,200)
root.resizable(False,False)   #fenetre non reductible
root.configure(bg="#091821")   #Couleur

#Ajout de la bande superieure portant le titre
titre=Label(root,borderwidth=3,relief=SUNKEN,text="FORMULAIRE DE CONNEXION", font=("Times New Roman", 20), bg="#091821",fg="white")
titre.place(x=0,y=0,width=400)

#nom utilisateur
lblnomutilisateur=Label(root,text="Nom utilisateur :", font=("Arial",15),bg="#091821",fg="white")
lblnomutilisateur.place(x=5,y=100,width=150)

txtnomutilisateur=Entry(root,bd=4,font=("Arial",12))
txtnomutilisateur.place(x=160,y=100,width=200, height=30)

#mot de passe
lblmdp=Label(root,text="Mot de passe :", font=("Arial",15),bg="#091821",fg="white")
lblmdp.place(x=5,y=150,width=150)

txtmdp=Entry(root,bd=4,font=("Arial",18, "bold"),show="•")
txtmdp.place(x=160,y=150,width=200, height=30)

#Bouton enregistrer
btnenregistrer = Button(root,text="Connexion",bg="red",fg="white",font=("Arial",10),command=Seconnecter)
btnenregistrer.place(x=160, y=200, width=200)






#boucle
root.mainloop()