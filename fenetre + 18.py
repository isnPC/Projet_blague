import tkinter as tk
import random
from tkinter import messagebox as mb


def compteBlague(blague) :
    nb=0
    with open (blague, encoding = 'utf-8') as l :
        for ligne in l:
            if ligne[0:2] == '**':
                nb += 1
        return nb




def ouvertureBlague(fichier):
    msg=""
    with open(fichier, encoding='utf-8',mode='r') as fic:
        for ligne in fic:
            msg+= ligne
    mb.showinfo(fichier,msg)
    
def ouvrir(Blagues):
    msg2=""
    with open("Blagues.txt", encoding="utf-8",mode='r') as fic:
        for ligne in fic:
            msg2 += ligne
    mb.showinfo(Blagues,msg2)

def rechercheBlague(blagues, num_cherche):
    """renvoie une blague numero num dans le fichier nomé blagues
       paramètre : nom fichier
                   numero blague
       ptype : chaine de caractère
               entier
       sortie : la blague
       stype : chaine de caractère """
    blague = ""
    with open (blagues, encoding = 'utf-8') as fic :
        for ligne in fic:
            if ligne[0:2] == '**':
                if int(ligne[2:]) == num_cherche:
                    break
                
        for ligne in fic:
            if ligne[0:2] != '**':
                blague = blague + ligne
            else:
                break
        return blague

def rechercheBlagueAlea(blagues):
    nbTotalBlague=compteBlague(blagues)
    numBlagueAlea=random.randint(1,nbTotalBlague)
    blagueAlea = rechercheBlague(blagues, numBlagueAlea)
    return blagueAlea
    
    
#compteBlague(monTitre+".txt")
def newWindow2(monTitre):
    fen3=tk.Tk()
    fen3.title(monTitre)
    fen3.geometry("450x175")
    boutFen3_1 = tk.Button(fen3,text="Aléatoire", command= lambda: mb.showinfo("titre", rechercheBlagueAlea(monTitre+".txt")))
    boutFen3_1.grid(row=1,column=1)
    boutFen3_2 = tk.Button(fen3,text="Blagues les mieux notées")
    boutFen3_2.grid(row=1,column=3)
    boutFen3_3 = tk.Button(fen3,text="Toutes les blagues", command = lambda : ouvertureBlague(monTitre+'.txt'))
    boutFen3_3.grid(row=2,column=1)
    boutFen3_4 = tk.Button(fen3,text="Rechercher blague")
    boutFen3_4.grid(row=2,column=3)
    boutFen3_5 = tk.Button(fen3,text="Fermer",command=fen3.destroy)
    boutFen3_5.grid(row=3,column=2)
    
    
    fen3.mainloop()


#creation de la fenetre principale
fen1 = tk.Tk()
fen1.title("nos blagues")
fen1.geometry("600x200")
#fen1.resizable(width=False, height=False)

#creation de la fenetre secondaire


boutB = tk.Button(fen1,text="Blondes",command=lambda : newWindow2("Blondes"))
boutB.grid(row=2,column=2)
boutS = tk.Button(text="Scientifiques",command=lambda : newWindow2("Scientifiques"))
boutS.grid(row=2,column=4)
boutA = tk.Button(text="Animaux",command=lambda : newWindow2("Animaux"))
boutA.grid(row=3,column=2)
boutTT = tk.Button(text="TocToc",command=lambda : newWindow2("Toc Toc"))
boutTT.grid(row=3,column=4)
boutD = tk.Button(text="Devinettes",command=lambda : newWindow2("Devinettes"))
boutD.grid(row=4,column=3)
boutB2 = tk.Button(text="Beaufs",command=lambda : newWindow2("Beaufs"))
boutB2.grid(row=5,column=2)
boutM = tk.Button(text="Malades",command=lambda : newWindow2("Malades"))
boutM.grid(row=5,column=4)
boutR = tk.Button(text="Raciste",command=lambda : newWindow2("Racistes"))
boutR.grid(row=6,column=2)
boutS2 = tk.Button(text="Sexuelles",command=lambda : newWindow2("Sexuelles"))
boutS2.grid(row=6,column=4)
tk.Label(text="Choisissez votre catégorie de blague :").grid(row=1,column=1)
boutT = tk.Button(text="Toutes les blagues",command=lambda : ouvrir("Blagues"))
boutT.grid(row=7,column=3)
boutAl = tk.Button(text="Aléatoire", command= lambda: mb.showinfo("titre", rechercheBlague("blagues.txt",)))
boutAl.grid(row=5,column=1)
fen1.mainloop()



    
