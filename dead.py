#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# Rickard Karlsson 2016-09-29
# Gjord med PyCharm 5.0.4 och python 3.5
# Ljudeffekter fr�n http://www.wavsource.com/sfx/sfx.htm


import time
import sys
import tkinter
from PIL import Image, ImageTk
import pygame

gamelevel = 0   # Vilken niv� i spelet man f�r n�rvarande �r p�.
piclist = []    # Lista f�r bilderna som anv�nds
leveltext = []  # Texterna f�r de olika niv�erna
pictureframe = None  # Bildruta
mbox = None          # Textruta

root = tkinter.Tk()

# Rutorna som visar hur mycket ammo man har
ammobox1 = None
ammobox2 = None
ammobox3 = None
ammobox4 = None

# M�ngden ammunition man har
ammochem = 5
ammocar = 3
ammobullets = 5
ammogrenade = 2

# Ljudeffekter
pygame.mixer.init(44100, -16, 2, 1024)
miss_sound = pygame.mixer.Sound("fart.wav")
chemsound = pygame.mixer.Sound("gas.wav")
carsound = pygame.mixer.Sound("crash.wav")
bulletsound = pygame.mixer.Sound("gun.wav")
grenadesound = pygame.mixer.Sound("grenade.wav")
winsound = pygame.mixer.Sound("owin31.wav")


def play_sound(d):  #Uppspelning av ljudeffekter

    if d == 0:
        chemsound.play()
    elif d == 1:
        carsound.play()
    elif d == 2:
        bulletsound.play()
    elif d == 3:
        grenadesound.play()
    else:
        return 0


def load_images():   # Ladda in alla bilder som ska anv�ndas i spelet i en lista.
    global piclist
    try:
        piclist = [
            ImageTk.PhotoImage(Image.open("garland500.png")), #0
            ImageTk.PhotoImage(Image.open("malcolm500.png")), #2
            ImageTk.PhotoImage(Image.open("camus500.png")), #1
            ImageTk.PhotoImage(Image.open("bruce500.png")), #0
            ImageTk.PhotoImage(Image.open("cole500.png")), #3
            ImageTk.PhotoImage(Image.open("mansfield500.png")), #1
            ImageTk.PhotoImage(Image.open("plath500.png")), #0
            ImageTk.PhotoImage(Image.open("kennedy500.png")), #2
            ImageTk.PhotoImage(Image.open("mlk500.png")), #2
            ImageTk.PhotoImage(Image.open("monroe500.png")), #0
            ImageTk.PhotoImage(Image.open("hemingway500.png")) #2
        ]
    except:
        print("N�got gick fel vid inl�sning av bilder.")
        exit_game()


def load_texts():   # Ladda in alla texter som ska anv�ndas i spelet i en lista.
    global leveltext
    try:
        leveltext = ["Judy Garland har kommit tillbaka, och det ser ut som att hon har\n"
                     "blivit k�r i dig. Hon har tuggat i sig sitt lillfinger och vill\n"
                     "mata dig som en f�gel. Vad g�r du?",

                     "Vad �r detta!? Malcolm X kom tillbaka som n�gon sorts eldspruta.\n"
                     "Ta hand om problemet. Kvickt, innan han f�rvandlas till en\n"
                     "drake och anv�nder resterna av dig f�r att g�ra shawarma.",

                     "Albert Camus finns �ter bland oss, men nu som en blodt�rstande vampyr.\n"
                     "Det �r ditt jobb att l�sa problemet.",

                     "Lenny Bruce. Demonbesatt. Han vill ta �ver v�rlden och f�rslava\n"
                     "m�nskligheten. Men det t�nker v�l inte du till�ta?",

                     "Du har ingen aning vad Nat King Cole har blivit, men farlig �r han!\n"
                     "Hans trollska toner lockar till sig folk s� han kan konsumera deras\n"
                     "sj�lar. Stoppa i �ronpropparna innan du g�r till anfall.",

                     "Jayne Mansfield.. wow... nej! Snabbt fram med vapnet!",

                     "Sylvia Plath kom tillbaka med Medusas f�rm�ga. Hon f�rvandlar folk"
                     "till sten med sin blick i en orov�ckande hastighet. Olustiga statyer"
                     "har b�rjat pryda gatorna. Det �r inte okej.",

                     "Kennedy anv�nder sin laserblick f�r att g�ra kebab av allm�nheten."
                     "Det �r.. uh.. inte okej.",

                     "Farligast hittills, Martin Luther King kan skjuta HubbaBubba fr�n\n"
                     "sina pekfingerspetsar! AhhhhhH!!",

                     "Det �r inte Marilyn Monroe l�ngre, det �r en slemdregglande zombie.\n"
                     "Yuck! Tv�tta h�nderna efter�t.",

                     "�h nej! Hemingway har �teruppst�tt, men han fick Hitlers sj�l med sig\n"
                     "p� k�pet! B�st att du fixar detta innan det b�rja dyka upp ov�ntade\n"
                     "koncentrationsl�ger."
        ]
    except:
        print("N�got gick fel vid inl�sning av text.")
        exit_game()


def exit_game():  #Avsluta programmet
    sys.exit(0)


def game_won():  #Det som h�nder n�r man vinner
    global pictureframe
    time.sleep(1)  # V�nta en sekund
    winsound.play()  # Spela upp vinstljudet
    pictureframe.delete('all')
    pictureframe.create_text(200, 150, text='Du vann.')  # Storvinsten


def game_lost():  #Det som h�nder n�r man f�rlorar
    global pictureframe
    global gamelevel
    pictureframe.delete('all')
    pictureframe.create_text(200, 150, text='Du f�rlorade.')
    gamelevel = 0


def correct_weapon(s): #Kollar om r�tt vapen har anv�nts
    global gamelevel

    # Funktionen returnerar True om det �r r�tt vapen, annars False
    # variabeln s �r vapentypen, 0 = kemiska, 1 = kof�ngare, 2 = muskedunder, 3 = plutoniumgranat

    if gamelevel == 0:
        if s == 0:
            return True
        else:
            return False
    elif gamelevel == 1:
        if s == 2:
            return True
        else:
            return False
    elif gamelevel == 2:
        if s == 1:
            return True
        else:
            return False
    elif gamelevel == 3:
        if s == 0:
            return True
        else:
            return False
    elif gamelevel == 4:
        if s == 3:
            return True
        else:
            return False
    elif gamelevel == 5:
        if s == 1:
            return True
        else:
            return False
    elif gamelevel == 6:
        if s == 0:
            return True
        else:
            return False
    elif gamelevel == 7:
        if s == 2:
            return True
        else:
            return False
    elif gamelevel == 8:
        if s == 2:
            return True
        else:
            return False
    elif gamelevel == 9:
        if s == 0:
            return True
        else:
            return False
    elif gamelevel == 10:
        if s == 2:
            return True
        else:
            return False


def load_level(n):  # Laddar in n�sta level
    global mbox
    if n < 11:                              # Om man inte har n�tt sista niv�n...
        show_image(n)                       # visa bilden f�r niv�n,
        mbox.configure(text=leveltext[n])   # och texten.
    elif n == 11:
        game_won()  # Vinst ifall man n�tt sista niv�n


def start_over():  # �terst�ller ursprungsv�rden och laddar om f�rsta niv�n
    global gamelevel
    global ammochem
    global ammocar
    global ammobullets
    global ammogrenade

    ammochem = 5
    ammocar = 3
    ammobullets = 5
    ammogrenade = 2

    update_ammolist()

    gamelevel = 0
    load_level(gamelevel)


def wrong_weapon():  # Det som h�nder n�r man anv�nder fel vapen
    global miss_sound
    miss_sound.play()  # Spela upp ljudet f�r fail
    return 0


def weapon_chem():  # Funktionen f�r n�r man trycker p� knappen f�r kemiska stridsmedel
    global gamelevel
    global ammochem

    if ammochem > 0:  # Kolla om det �r ammo kvar
        ammochem -= 1  # Anv�nder upp en ammo
        update_ammolist()
        if correct_weapon(0):
            play_sound(0)  # Spela upp vapenljudet
            gamelevel += 1
            load_level(gamelevel)  # Ladda n�sta niv�
        else:
            wrong_weapon()
    else:
        game_lost()


def weapon_car():  # Funktionen f�r n�r man trycker p� knappen f�r kof�ngare
    global gamelevel
    global ammocar

    if ammocar > 0:  # Kolla om det �r ammo kvar
        ammocar -= 1  # Anv�nder upp en ammo
        update_ammolist()
        if correct_weapon(1):
            play_sound(1)  # Spela upp vapenljudet
            gamelevel += 1
            load_level(gamelevel)  # Ladda n�sta niv�
        else:
            wrong_weapon()
    else:
        game_lost()


def weapon_bullet():  # Funktionen f�r n�r man trycker p� knappen f�r muskedunder
    global gamelevel
    global ammobullets

    if ammobullets > 0:  # Kolla om det �r ammo kvar
        ammobullets -= 1  # Anv�nder upp en ammo
        update_ammolist()
        if correct_weapon(2):
            play_sound(2)  # Spela upp vapenljudet
            gamelevel += 1
            load_level(gamelevel)  # Ladda n�sta niv�
        else:
            wrong_weapon()
    else:
        game_lost()


def weapon_grenade():  # Funktionen f�r n�r man trycker p� knappen f�r plutoniumgranat
    global gamelevel
    global ammogrenade

    if ammogrenade > 0:  # Kolla om det �r ammo kvar
        ammogrenade -= 1  # Anv�nder upp en ammo
        update_ammolist()
        if correct_weapon(3):  #
            play_sound(3)  # Spela upp vapenljudet
            gamelevel += 1
            load_level(gamelevel)  # Ladda n�sta niv�
        else:
            wrong_weapon()
    else:
        game_lost()


def show_image(x):  # Visar n�sta bild i bildrutan
    global pictureframe
    pictureframe.delete('all')
    pictureframe.create_image(0, 0, image=piclist[x], anchor='nw')


def update_ammolist():  # Uppdaterar grafiskt hur mycket ammunition som �r kvar
    global ammobox1
    global ammobox2
    global ammobox3
    global ammobox4

    ammobox1.configure(text=str(ammochem))
    ammobox2.configure(text=str(ammocar))
    ammobox3.configure(text=str(ammobullets))
    ammobox4.configure(text=str(ammogrenade))


def instructions():
    inst = "V�lkommen till spelet 'K�ndisar som dog p� 60-talet har �teruppst�tt och vill g�ra dig illa.'\n\n" \
           "Instruktioner:\n\nDet enda s�ttet att ta k�l p� dessa od�da �r att g�ra sig av med dom p� samma s�tt " \
           "som\ndom ursprungligen dog. Kemiska stridsmedel �r t.ex. droger och gas. Kof�ngare �r\ntill f�r trafikd�d. "\
           "Muskedundret �r ett skjutvapen. Plutoniumgranater orsakar cancer.\nKlicka p� r�tt vapenknapp f�r att ta d�d "\
           "p� monstret. Du har begr�nsad ammunition\ntill varje vapen, vilket du kan se i statuskolumnen 'ammunition'. " \
           "Om det tar slut\nammunition f�rlorar du spelet. Det finns tillr�ckligt med ammunition f�r att\nanv�nda varje " \
           "vapen fel en g�ng. Klicka p� starta spelet f�r att b�rja.\nLycka till!"
    return inst


def start():
    load_level(0)  # Ladda f�rsta niv�n


def setGUI():
    global pictureframe
    global piclist
    global mbox
    global root

    global ammobox1
    global ammobox2
    global ammobox3
    global ammobox4

    root.title('D�d p� 60-talet')

    pictureframe = tkinter.Canvas(root, bg='white', height=500, width=500)  # Bldrutan
    pictureframe.pack()
    pictureframe.create_text(250, 150, text=instructions())  # Visa instruktionerna

    mbox = tkinter.Label(root, bg='white', justify='left')  # Box f�r speltexterna
    mbox.pack()

    controlframe = tkinter.Frame(root, bg='white', height=500, width=500)  # Kontrollpanelen med alla knappar och ammolista
    controlframe.pack(side='left')

    tkinter.Label(controlframe, text='Ammunition', borderwidth=1, bg='grey').grid(row=1, column=1, ipadx=40, sticky='we')

    # Vapenknappar
    weapon1 = tkinter.Button(controlframe, text='Kemiska stridsmedel', borderwidth=1, bg='grey', command=weapon_chem)
    weapon2 = tkinter.Button(controlframe, text='Kof�ngare', borderwidth=1, bg='grey', command=weapon_car)
    weapon3 = tkinter.Button(controlframe, text='Muskedunder', borderwidth=1, bg='grey', command=weapon_bullet)
    weapon4 = tkinter.Button(controlframe, text='Plutoniumgranat', borderwidth=1, bg='grey', command=weapon_grenade)

    weapon1.grid(row=2,column=0, ipadx=40, sticky='we')
    weapon2.grid(row=3,column=0, sticky='we')
    weapon3.grid(row=4, column=0, sticky='we')
    weapon4.grid(row=5, column=0, sticky='we')

    # Ammunitionstatus
    ammobox1 = tkinter.Label(controlframe, bg='lightgrey')
    ammobox2 = tkinter.Label(controlframe, bg='lightgrey')
    ammobox3 = tkinter.Label(controlframe, bg='lightgrey')
    ammobox4 = tkinter.Label(controlframe, bg='lightgrey')

    ammobox1.grid(row=2, column=1, sticky='wens')
    ammobox2.grid(row=3, column=1, sticky='wens')
    ammobox3.grid(row=4, column=1, sticky='wens')
    ammobox4.grid(row=5, column=1, sticky='wens')

    update_ammolist()

    # Menyknappar
    startbutton = tkinter.Button(controlframe, text='Starta spelet', borderwidth=1, bg='grey', command=start)
    restart_button = tkinter.Button(controlframe, text='B�rja om', borderwidth=1, bg='grey', command=start_over)
    exit_button = tkinter.Button(controlframe, text='Avsluta', borderwidth=1, bg='grey', command=exit_game)

    startbutton.grid(row=3,column=4, ipadx=30, sticky='we')
    restart_button.grid(row=4,column=4, ipadx=40, sticky='we')
    exit_button.grid(row=5,column=4, sticky='we')


def main():
    load_images()
    load_texts()
    setGUI()
    root.mainloop()

if __name__ == "__main__":
    main()
