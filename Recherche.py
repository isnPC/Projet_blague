import tkinter as tk
from tkinter import messagebox as mb

rep = input("mot clef?")
chaines = [""] # Texte à rechercher
msg3=""
zone = False
fichier = open("Blondes.txt","r")
for ligne in fichier:
    for chaine in chaines:
        if rep in ligne:
            print(ligne)



        
 
fichier.close()
