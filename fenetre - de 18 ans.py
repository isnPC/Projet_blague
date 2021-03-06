import random
import tkinter as tk
from tkinter import messagebox as mb



def ouvertureBlague(fichier):
    msg = ""
    with open(fichier, encoding="utf-8", mode='r') as fic:
        for ligne in fic:
            msg += ligne
    mb.showinfo(fichier, msg)

def ouvrir(blagues):
    msg2=""
    with open("blagues.txt", encoding="utf-8",mode='r') as fic:
        for ligne in fic:
            msg2 +=ligne
    mb.showinfo(blagues,msg2)
    

def rechercheBlague(blagues, num):
    """renvoie une blague numero num dans le fichier nomé blagues
       paramètre : nom fichier
                   numero blague
       ptype : chaine de caractère
               entier
       sortie : la blague
       stype : chaine de caractère """
    msg3=""
    zone = False
    with open (blagues, encoding = 'utf-8') as fic :
        for ligne in fic:
            if ligne[0:2] != '**' and zone :
                msg3 = msg3 + ligne
            if ligne[0:2] == '**':
                if int(ligne[2]) == num:
                    zone = True
                else:
                    zone = False
        return msg3        

def aleatoire(monTitre):
    """renvoie un nombre au hasard compris entre 1 et le nombre maximal de blague dans le fichier
        paramètre : nom du fichier
        ptype : chaine de caractère
        sortie : le numéro de la blague tirée au hasard dans le fichier
        stype : entier """
    with open()..................................................
    return random.randint(1,x)

def newWindow1(monTitre):
    fen2 = tk.Tk()
    fen2.title(monTitre)
    fen2.geometry("450x175")
    boutFen2_1 = tk.Button(fen2,text="Aléatoire", command= lambda: mb.showinfo("titre", rechercheBlague(monTitre+".txt",aleatoire())))
    boutFen2_1.grid(row=1,column=1)
    boutFen2_2 = tk.Button(fen2,text="Blagues les mieux notées")
    boutFen2_2.grid(row=1,column=3)
    boutFen2_3 = tk.Button(fen2,text="Toutes les blagues", command= lambda : ouvertureBlague(monTitre+'.txt'))
    boutFen2_3.grid(row=2,column=1)
    boutFen2_4 = tk.Button(fen2,text="Rerchercher une blague")
    boutFen2_4.grid(row=2,column=3)
    boutFen2_5 = tk.Button(fen2,text="Fermer",command=fen2.destroy)
    boutFen2_5.grid(row=3,column=2)
    fen2.mainloop()
    fen2.resizale(width=False, height=False)


    
    
    
fen1 = tk.Tk()
fen1.title("Nos blagues")
fen1.geometry("600x200")
#fen1.resizale(width=False, height=False)
boutB = tk.Button(text="Blondes",command=lambda : newWindow1("blondes"))
boutB.grid(row=2,column=1)
boutS = tk.Button(text="Scientifiques",command=lambda : newWindow1("scientifiques"))
boutS.grid(row=2,column=2)
boutA = tk.Button(text="Animaux",command=lambda : newWindow1("animaux"))
boutA.grid(row=3,column=1)
boutTT = tk.Button(text="Toc Toc",command=lambda : newWindow1("Toc Toc"))
boutTT.grid(row=3,column=2)
boutD = tk.Button(text="Devinettes",command=lambda : newWindow1("Devinettes"))
boutD.grid(row=4,column=1)
boutT = tk.Button(text="Blagues", command= lambda:  ouvrir("blagues.txt"))
boutT.grid(row=4,column=2)
boutAl = tk.Button(text="Aléatoire", command= lambda: mb.showinfo("titre", rechercheBlague("blagues.txt",)aleatoire()))
boutAl.grid(row=5,column=1)
tk.Label(text="Choisissez votre catégorie de blagues à afficher:").grid(row=1,column=1)

fen1.mainloop()
