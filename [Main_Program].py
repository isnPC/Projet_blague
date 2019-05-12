import tkinter as tk
import random
from tkinter import messagebox as mb

def ouvertureBlague(monTitre):
    """affiche une balgue du fichier correspondant
    paramètre : nom fichier
    ptype : chaine de caractère
    sortie : la blague
    stype : chaine de caractère """
    with open(monTitre, encoding='utf-8') as fic:
        for ligne in fic:
            print(ligne)

def ouvertureToutesBlagues(fichier):
    """affiche ce que comporte un fichier en entier correspondant
    paramètre : nom fichier
    ptype : chaine de caractère
    sortie : les blague
    stype : chaine de caractère """
    msg=""
    with open (fichier,encoding="utf-8",mode='r') as fic:
        for ligne in fic:
            msg+= ligne
    mb.showinfo(fichier,msg)


def compteBlague(blague):
    """compte le nombre de blagues dans le fichier
    paramètre : les blagues du fichier
    ptype : chaine de caractère
    sortie : le nombre de blague du fichier
    stype : entier """
    nb=0
    with open (blague, encoding = 'utf-8') as l :
        for ligne in l:
            if ligne[0:2] == '**':
                nb += 1
    return nb



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
    """choisit une blague au hasard parmis différentes proposées
    paramètre : nom fichier
    ptype : chaine de caractère
    sortie : la blague
    stype : chaine de caractère """
    nbTotalBlague=compteBlague(blagues)
    numBlagueAlea=random.randint(1,nbTotalBlague)
    blagueAlea = rechercheBlague(blagues, numBlagueAlea)
    return blagueAlea


def ajouterBlague(fichier):
    """ajoute une blague au fichier
       paramètre : nom fichier
       ptype : chaine de caractères
    """
    maBlague = open(fichier,"a")
    #les blagues sont numérotées selon le nombres de blagues dans le fichier
    maBlague.write("\n**"+str(compteBlague(fichier)+1)+'\n')
    Blague = input("entrez votre blague:")
    print(Blague)
    maBlague.write(Blague+'\n')
    maBlague.close()


def Mineur():
    #fenêtre affichant les boutons pour une personne ayant mois de 18 ans
    fen1.destroy()
    fen4=tk.Tk()
    fen4.title("catégories")
    fen4.geometry("600x200")
    fen4.resizable(width=False,height=False)
    boutB = tk.Button(text="Blondes",command=lambda : newWindow3("Blondes"),bg ="gold")
    boutB.grid(row=2,column=2)
    boutS = tk.Button(text="Scientifiques",command=lambda : newWindow3("Scientifiques"),bg ="gold")
    boutS.grid(row=2,column=4)
    boutA = tk.Button(text="Animaux",command=lambda : newWindow3("Animaux"),bg ="light sky blue")
    boutA.grid(row=3,column=2)
    boutTT = tk.Button(text="Toc Toc",command=lambda : newWindow3("TocToc"),bg ="light sky blue")
    boutTT.grid(row=3,column=4)
    boutD = tk.Button(text="Devinettes",command=lambda : newWindow3("Devinettes"),bg ="peach puff")
    boutD.grid(row=4,column=4)
    boutF=tk.Button(text="Fermer",command=fen4.destroy,bg ="red")
    boutF.grid(row=5,column=3)
    boutAl = tk.Button(text="Aléatoire",  command= lambda: mb.showinfo("titre", rechercheBlagueAlea("ToutesLesBlagues-18.txt")),bg ="peach puff")
    boutAl.grid(row=4,column=2)
    tk.Label(text="Choisissez votre catégorie de blagues à afficher").grid(row=4,column=1)


def Majeur():
    #fenêtre affichant les boutons pour une personne ayant plus de 18 ans
    fen1.destroy()
    fen2=tk.Tk()
    fen2.title("Categories")
    fen2.geometry("600x200")
    fen2.resizable(width=False,height=False)
    boutB = tk.Button(text="Blondes",command=lambda : newWindow3("Blondes"),bg ="gold")
    boutB.grid(row=2,column=2)
    boutS = tk.Button(text="Scientifiques",command=lambda : newWindow3("Scientifiques"),bg ="gold")
    boutS.grid(row=2,column=4)
    boutA = tk.Button(text="Animaux",command=lambda : newWindow3("Animaux"),bg ="light sky blue")
    boutA.grid(row=3,column=2)
    boutTT = tk.Button(text="Toc Toc",command=lambda : newWindow3("TocToc"),bg ="light sky blue")
    boutTT.grid(row=3,column=4)
    boutD = tk.Button(text="Devinettes",command=lambda : newWindow3("Devinettes"),bg ="peach puff")
    boutD.grid(row=4,column=3)
    boutB2 = tk.Button(text="Beaufs",command=lambda : newWindow3("Beaufs"),bg ="light sky blue")
    boutB2.grid(row=5,column=2)
    boutM = tk.Button(text="Malades",command=lambda : newWindow3("Malades"),bg ="light sky blue")
    boutM.grid(row=5,column=4)
    boutR = tk.Button(text="Raciste",command=lambda : newWindow3("Racistes"),bg ="gold")
    boutR.grid(row=6,column=2)
    boutS2 = tk.Button(text="Sexuelles",command=lambda : newWindow3("Sexuelles"),bg ="gold")
    boutS2.grid(row=6,column=4)
    boutF=tk.Button(text="Fermer",command=fen2.destroy,bg ="red")
    boutF.grid(row=6,column=3)
    tk.Label(text="Choisissez votre catégorie de blague :").grid(row=1,column=1)
    boutAl = tk.Button(text="Aléatoire",  command= lambda: mb.showinfo("titre", rechercheBlagueAlea("ToutesLesBlagues+18.txt")),bg ="darkorchid1")
    boutAl.grid(row=5,column=1)

def newWindow3(monTitre):
    #fenêtre affichant les boutons pour une personne ayant plus de 18 ans
    fen3=tk.Tk()
    fen3.title(monTitre)
    fen3.geometry("450x175")
    fen3.resizable(width=False,height=False)
    boutFen3_1 = tk.Button(fen3,text="Aléatoire", command = lambda: mb.showinfo("titre", rechercheBlagueAlea(monTitre+".txt")),bg ="darkorchid1")
    boutFen3_1.grid(row=1,column=1)
    boutFen3_2 = tk.Button(fen3,text="Ajouter une blague", command = lambda: ajouterBlague(monTitre+".txt"),bg ="lightpink1")
    boutFen3_2.grid(row=1,column=3)
    boutFen3_3 = tk.Button(fen3,text="Toutes les blagues", command = lambda : ouvertureToutesBlagues(monTitre+".txt"),bg ="plum1")
    boutFen3_3.grid(row=2,column=1)
    boutFen3_4 = tk.Button(fen3,text="Rechercher blagues",bg ="salmon1")
    boutFen3_4.grid(row=2,column=3)
    boutFen3_5 = tk.Button(fen3,text="Fermer",command=fen3.destroy,bg ="red")
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
