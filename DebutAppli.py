import tkinter as tk
import random
from tkinter import messagebox as mb

def ouvertureBlague(monTitre):
    with open(monTitre, encoding='utf-8') as fic:
        for ligne in fic:
            print(ligne)

def ouvertureBlague(fichier):
    msg=""
    with open (fichier,encoding="utf-8",mode='r') as fic:
        for ligne in fic:
            msg+= ligne
    mb.showinfo(fichier,msg)


def compteBlague(blague) :
    nb=0
    with open (blague, encoding = 'utf-8') as l :
        for ligne in l:
            if ligne[0:2] == '**':
                nb += 1
    return nb

def trouver(monTitre):
    rep=input("recherche blague:")
    chaines = [""] # Texte Ã  rechercher
    msg3=""
    zone = False
    fichier = open(monTitre)
    for ligne in fichier:
        for chaine in chaines:
         if rep in ligne:
             print(ligne)



def rechercheBlague(blagues, num_cherche):
    """renvoie une blague numero num dans le fichier nomÃ© blagues
       paramÃ¨tre : nom fichier
                   numero blague
       ptype : chaine de caractÃ¨re
               entier
       sortie : la blague
       stype : chaine de caractÃ¨re """
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



def Mineur():
    fen1.destroy()
    fen4=tk.Tk()
    fen4.title("Quel âge avez- vous ?")
    fen4.geometry("600x200")
    fen4.resizable(width=False,height=False)
    boutAl1 = tk.Button(fen4,text="Aléatoire", command= lambda: mb.showinfo("titre", rechercheBlagueAlea("ToutesLesBlagues-18.txt")))
    boutB = tk.Button(text="Blondes",command=lambda : newWindow3("Blondes"))
    boutB.grid(row=2,column=2)
    boutS = tk.Button(text="Scientifiques",command=lambda : newWindow3("Scientifiques"))
    boutS.grid(row=2,column=4)
    boutA = tk.Button(text="Animaux",command=lambda : newWindow3("Animaux"))
    boutA.grid(row=3,column=2)
    boutTT = tk.Button(text="Toc Toc",command=lambda : newWindow3("TocToc"))
    boutTT.grid(row=3,column=4)
    boutD = tk.Button(text="Devinettes",command=lambda : newWindow3("Devinettes"))
    boutD.grid(row=4,column=4)
    boutF=tk.Button(text="Fermer",command=fen4.destroy)
    boutF.grid(row=5,column=3)
    boutAl = tk.Button(text="Aléatoire",  command= lambda: mb.showinfo("titre", rechercheBlagueAlea("ToutesLesBlagues-18.txt")))
    boutAl.grid(row=4,column=2)
    tk.Label(text="Choisissez votre catégorie de blagues à  afficher").grid(row=4,column=1)


def Majeur():
    fen1.destroy()
    fen2=tk.Tk()
    fen2.title("Categories")
    fen2.geometry("600x200")
    fen2.resizable(width=False,height=False)
    boutB = tk.Button(text="Blondes",command=lambda : newWindow3("Blondes"))
    boutB.grid(row=2,column=2)
    boutS = tk.Button(text="Scientifiques",command=lambda : newWindow3("Scientifiques"))
    boutS.grid(row=2,column=4)
    boutA = tk.Button(text="Animaux",command=lambda : newWindow3("Animaux"))
    boutA.grid(row=3,column=2)
    boutTT = tk.Button(text="Toc Toc",command=lambda : newWindow3("TocToc"))
    boutTT.grid(row=3,column=4)
    boutD = tk.Button(text="Devinettes",command=lambda : newWindow3("Devinettes"))
    boutD.grid(row=4,column=3)
    boutB2 = tk.Button(text="Beaufs",command=lambda : newWindow3("Beaufs"))
    boutB2.grid(row=5,column=2)
    boutM = tk.Button(text="Malades",command=lambda : newWindow3("Malades"))
    boutM.grid(row=5,column=4)
    boutR = tk.Button(text="Raciste",command=lambda : newWindow3("Racistes"))
    boutR.grid(row=6,column=2)
    boutS2 = tk.Button(text="Sexuelles",command=lambda : newWindow3("Sexuelles"))
    boutS2.grid(row=6,column=4)
    boutF=tk.Button(text="Fermer",command=fen2.destroy)
    boutF.grid(row=6,column=3)
    tk.Label(text="Choisissez votre catégorie de blague :").grid(row=1,column=1)
    boutAl = tk.Button(text="Aléatoire",  command= lambda: mb.showinfo("titre", rechercheBlagueAlea("ToutesLesBlagues+18.txt")))
    boutAl.grid(row=5,column=1)

def newWindow3(monTitre):
    fen3=tk.Tk()
    fen3.title(monTitre)
    fen3.geometry("450x175")
    fen3.resizable(width=False,height=False)
    boutFen3_1 = tk.Button(fen3,text="AlÃ©atoire" ,command= lambda: mb.showinfo("titre", rechercheBlagueAlea(monTitre+".txt")))
    boutFen3_1.grid(row=1,column=1)
    boutFen3_2 = tk.Button(fen3,text="Blagues les mieux notÃ©es")
    boutFen3_2.grid(row=1,column=3)
    boutFen3_3 = tk.Button(fen3,text="Toutes les blagues", command = lambda : ouvertureBlague(monTitre+".txt"))
    boutFen3_3.grid(row=2,column=1)
    boutFen3_4 = tk.Button(fen3,text="Rechercher blagues",command = lambda : trouver(monTitre+".txt"))
    boutFen3_4.grid(row=2,column=3)
    boutFen3_5 = tk.Button(fen3,text="Fermer",command=fen3.destroy)
    boutFen3_5.grid(row=3,column=2)


    fen3.mainloop()


fen1=tk.Tk()
fen1.title("Quel âge avez-vous ?")
fen1.geometry("350x200")
fen1.resizable(width=False,height=False)

tk.Label(text="Quel âge avez vous ?").grid(row=1,column=1)
boutMi=tk.Button(text="-18",width=10,height=5,command=Mineur,bg="green")
boutMi.grid(row=5,column=1 ,padx=30, pady=30)
boutMa=tk.Button(text="+18",width=10,height=5,command=Majeur,bg ="red")
boutMa.grid(row=5,column=2 ,padx=30, pady=30)


fen1.mainloop()
