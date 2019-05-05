from tkinter import *
from random import *
import time
import pygame

pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.init()
score_joueur = 0 #Score du joueur ,init a 0

def start():
    print("------ START ------ ")
    global nb_couleur
    resetall()
    tirage(nb_couleur)
    lecture(nb_couleur)

def resetall():
    print("--- RESET DE LA PARTIE ---")
    global choix_joueur
    global nb_couleur
    global score_joueur
    info_score(False)
    actu_texte(tour,1)
    nb_couleur = []
    choix_joueur = []

def clear():
    print("--- CLEAR CHOIX JOUEUR ---")
    global choix_joueur
    choix_joueur = []

def tirage(nb_couleur):
    print("--- TIRAGE D'UNE COULEUR ---")
    nb_couleur.append(randint(0,3))
    print(nb_couleur)

def info_score(info):
    if info:
        global score_joueur
        score_joueur = score_joueur + 1
    else:
        score_joueur = 0
    score.configure(text="Votre score : " + str(score_joueur))

def actu_texte(tour,num):
    tour.configure(text=TOURPOUR[num])
    tour.update()

def flash(nb):
    if nb == 0:
        btn.config(state="active")
        btn.update()
        pygame.mixer.Sound("Rouge.wav").play()
        time.sleep(.500)
        flash_end(0)
    elif nb == 1:
        btn2.config(state="active")
        btn2.update()
        pygame.mixer.Sound("Bleu.wav").play()
        time.sleep(0.500)
        flash_end(1)
    elif nb == 2:
        btn4.config(state="active")
        btn4.update()
        pygame.mixer.Sound("Jaune.wav").play()
        time.sleep(.500)
        flash_end(2)
    else :
        btn3.config(state="active")
        btn3.update()
        pygame.mixer.Sound("Vert.wav").play()
        time.sleep(.500)
        flash_end(3)

def flash_end(nb):
    if nb == 0:
        btn.config(state="normal")
    elif nb == 1:
        btn2.config(state="normal")
    elif nb == 2:
        btn4.config(state="normal")
    else :
        btn3.config(state="normal")

def lecture(L):
    print("---LECTURE DES COULEURS ---")
    actu_texte(tour,2)
    for i in range(len(L)):
        root.update()
        time.sleep(.500)
        flash(L[i])
    global score_joueur
    score_joueur = score_joueur + 1
    print("le score est :" + str(score_joueur))
    score.config(text="Votre score: " + str(score_joueur))
    actu_texte(tour,1)
    print("fin lecture")

def verif(L,CHOIX):
    print("--- VERIFICATION ---")
    i = 0
    for i in range(len(L)):
        if(L[i] != CHOIX[i]):
            print("Dommage, c'est perdu !")
            time.sleep(.500)
            clear()
            resetall()
    print("Gagné, tour suivant !")
    print(choix_joueur)
    clear()
    game()

def click_btn_red():
    global choix_joueur
    choix_joueur.append(0)
    print("Joueur selection : rouge")
    verif_nb_click()

def click_btn_blue():
    global choix_joueur
    choix_joueur.append(1)
    print("Joueur selection : bleu")
    verif_nb_click()

def click_btn_green():
    global choix_joueur
    choix_joueur.append(3)
    print("Joueur selection : vert")
    verif_nb_click()

def click_btn_yellow():
    global choix_joueur
    choix_joueur.append(2)
    print("Joueur selection : jaune")
    verif_nb_click()

def verif_nb_click():
    global nb_couleur
    global choix_joueur
    if(len(nb_couleur) == len(choix_joueur)):
        verif(nb_couleur,choix_joueur)

def game():
    clear()
    time.sleep(.500)
    global nb_couleur
    tirage(nb_couleur)
    lecture(nb_couleur)

choix_joueur = []
nb_couleur = []
COULEUR = ["rouge","bleu","jaune","vert"]
TOURPOUR = ["Clique sur commencer pour jouer","C'est a votre tour de jouer","Patience"]
root=Tk()
root.title("Jeu de Simon")
root.resizable(False, False)
tour = Label(text=str(TOURPOUR[0]),font=10)
tour.grid(row=0,column=0,columnspan=2,sticky="")
btn=Button(root,width=20,height=14,bg="#EE575B",activebackground="red",command=click_btn_red)
btn.grid(row = 1,sticky="e")
btn2=Button(root,width=20,height=14,bg="#61A1CA",activebackground="blue", command=click_btn_blue)
btn2.grid(row=1,column=1,sticky="w")
btn3=Button(root,width=20,height=14 ,bg="#65E265",activebackground="green", command=click_btn_green)
btn3.grid(row=2,column=0,sticky="e")
btn4=Button(root,width=20,height=14,bg="#FFE772",activebackground="yellow", command=click_btn_yellow)
btn4.grid(row=2,column=1,sticky="e")
score = Label(text="Votre score: " + str(score_joueur),font=10)
score.grid(row=3,column=0,sticky="w")
btn_start = Button(root,text="COMMENCER",width=16,height=1,bg="white",font="Helvetica",fg="#7A4A4B",command=start)
btn_start.grid(row=3,column=1)
 
root.mainloop()