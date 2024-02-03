# PROGRAMMINO PER ANAS - RICONOSCI UN'IMMAGINE
# Le immagini le ho trovate su pixabay e su clipart-library-com
# Ho trovato i suoni su https://www.soundjay.com/ e su https://www.soundgator.com/
# Ho composto la musica iniziale con MuseScore 3

#################################
#                               #  
# Autore: Paolo Maria Guardiani #
#                               # 
#################################                      


from tkinter import ttk  # questa linea è importantissima https://docs.python.org/3/library/tkinter.ttk.html
from tkinter import *
from tkinter.ttk import *
import pygame
from pygame import mixer

root = Tk()
root.title("RICONOSCI LE IMMAGINI")
# root.iconbitmap(r'immagini/logo_di_paolo.ico')
root.geometry("700x700")

# Inizializiamo lo stile   (thanks to: https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame)
s = ttk.Style()

# Initialize Pygame
pygame.mixer.init()
# thanks to: https://youtu.be/pcdB2s2y4Qc
sound_error = mixer.Sound('suoni/sound_error.wav')
sound_click = mixer.Sound('suoni/sound_click.wav')
sound_star = mixer.Sound('suoni/sound_star.wav')
# musica di sottofondo:
mixer.music.load('suoni/musica_iniziale.wav')
mixer.music.play()


def attiva_gioco():
    e["state"] = NORMAL
    punteggio['state'] = NORMAL
    btn_indietro["state"] = NORMAL
    btn_controlla["state"] = NORMAL
    btn_avanti["state"] = NORMAL
    e.focus()  # porto il focus sulla entry
    e.delete(0, END)


def animali():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/animali/cane.png",
        "immagini/animali/gatto.png",
        "immagini/animali/mucca.png",
        "immagini/animali/oca.png",
        "immagini/animali/zebra.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "cane",
        "gatto",
        "mucca",
        "oca",
        "zebra"
    ]


def insetti():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/insetti/ape.png",
        "immagini/insetti/bruco.png",
        "immagini/insetti/coccinella.png",
        "immagini/insetti/farfalla.png",
        "immagini/insetti/formica.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "ape",
        "bruco",
        "coccinella",
        "farfalla",
        "formica"
    ]


def frutta():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/frutta/ananas.png",
        "immagini/frutta/banana.png",
        "immagini/frutta/ciliegia.png",
        "immagini/frutta/mela.png",
        "immagini/frutta/pera.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "ananas",
        "banana",
        "ciliegia",
        "mela",
        "pera"
    ]


def verdura():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/verdura/carote.png",
        "immagini/verdura/insalata.png",
        "immagini/verdura/limone.png",
        "immagini/verdura/patate.png",
        "immagini/verdura/pomodoro.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "carote",
        "insalata",
        "limone",
        "patate",
        "pomodoro"
    ]


def cibo():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/cibo/budino.png",
        "immagini/cibo/pane.png",
        "immagini/cibo/pasta.png",
        "immagini/cibo/salame.png",
        "immagini/cibo/torta.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "budino",
        "pane",
        "pasta",
        "salame",
        "torta"
    ]


def natura():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/natura/erba.png",
        "immagini/natura/mare.png",
        "immagini/natura/pigna.png",
        "immagini/natura/pino.png",
        "immagini/natura/rosa.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "erba",
        "mare",
        "pigna",
        "pino",
        "rosa"
    ]


def corpo():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/corpo/dito.png",
        "immagini/corpo/mano.png",
        "immagini/corpo/naso.png",
        "immagini/corpo/occhio.png",
        "immagini/corpo/orecchio.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "dito",
        "mano",
        "naso",
        "occhio",
        "orecchio"
    ]


def abbigliamento():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/abbigliamento/cappello.png",
        "immagini/abbigliamento/maglia.png",
        "immagini/abbigliamento/orologio.png",
        "immagini/abbigliamento/pantaloni.png",
        "immagini/abbigliamento/scarpe.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "cappello",
        "maglia",
        "orologio",
        "pantaloni",
        "scarpe"
    ]


def oggetti():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/oggetti/lampada.png",
        "immagini/oggetti/ombrello.png",
        "immagini/oggetti/pentola.png",
        "immagini/oggetti/sapone.png",
        "immagini/oggetti/spazzolino.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "lampada",
        "ombrello",
        "pentola",
        "sapone",
        "spazzolino"
    ]


def mezzi():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/mezzi/aereo.png",
        "immagini/mezzi/barca.png",
        "immagini/mezzi/bicicletta.png",
        "immagini/mezzi/macchina.png",
        "immagini/mezzi/treno.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "aereo",
        "barca",
        "bicicletta",
        "macchina",
        "treno"
    ]


def scuola():
    global counter
    counter = 1
    global lista_immagini
    global lista_parole

    attiva_gioco()

    lista_immagini = [
        "immagini/scuola/banco.png",
        "immagini/scuola/gomma.png",
        "immagini/scuola/matita.png",
        "immagini/scuola/palla.png",
        "immagini/scuola/zaino.png"
    ]

    img = PhotoImage(file=lista_immagini[0])
    image_label.configure(image=img)
    image_label.image = img

    lista_parole = [
        "banco",
        "gomma",
        "matita",
        "palla",
        "zaino"
    ]


def immagine_indietro():
    global counter
    global lista_immagini
    counter -= 1
    e.focus()  # porto il focus nuovamente sulla entry

    sound_click.play()

    if counter == -1 or counter == 0:
        counter = 5
    if counter == 1:
        img1 = PhotoImage(file=lista_immagini[0])
        image_label.configure(image=img1)
        image_label.image = img1
        e.delete(0, END)
    elif counter == 2:
        img2 = PhotoImage(file=lista_immagini[1])
        image_label.configure(image=img2)
        image_label.image = img2
        e.delete(0, END)
    elif counter == 3:
        img3 = PhotoImage(file=lista_immagini[2])
        image_label.configure(image=img3)
        image_label.image = img3
        e.delete(0, END)
    elif counter == 4:
        img4 = PhotoImage(file=lista_immagini[3])
        image_label.configure(image=img4)
        image_label.image = img4
        e.delete(0, END)
    elif counter == 5:
        img5 = PhotoImage(file=lista_immagini[4])
        image_label.configure(image=img5)
        image_label.image = img5
        e.delete(0, END)
    btn_controlla["state"] = NORMAL
    e["state"] = NORMAL


# *args is a wildcard argument that tells the program that
# anything could be sent to this function
# thanks to: https://youtu.be/NiQdsK3H57Y
def controlla(*args):
    global punti
    e.focus()  # porto il focus nuovamente sulla entry

    if counter == 1 and e.get().lower() == lista_parole[0]:
        punti += 1
        punteggio.config(text="PUNTEGGIO: " + str(punti))
        btn_controlla["state"] = DISABLED
        immagine_avanti()
    elif counter == 2 and e.get().lower() == lista_parole[1]:
        punti += 1
        punteggio.config(text="PUNTEGGIO: " + str(punti))
        btn_controlla["state"] = DISABLED
        immagine_avanti()
    elif counter == 3 and e.get().lower() == lista_parole[2]:
        punti += 1
        punteggio.config(text="PUNTEGGIO: " + str(punti))
        btn_controlla["state"] = DISABLED
        immagine_avanti()
    elif counter == 4 and e.get().lower() == lista_parole[3]:
        punti += 1
        punteggio.config(text="PUNTEGGIO: " + str(punti))
        btn_controlla["state"] = DISABLED
        immagine_avanti()
    elif counter == 5 and e.get().lower() == lista_parole[4]:
        punti += 1
        punteggio.config(text="PUNTEGGIO: " + str(punti))
        btn_controlla["state"] = DISABLED
        immagine_avanti()
    else:
        sound_error.play()
        punti -= 1
        punteggio.config(text="PUNTEGGIO: " + str(punti))

    if punti == 2:
        image_stella1.grid(row=3, column=0, padx=20)
        sound_star.play()
    if punti == 4:
        image_stella2.grid(row=3, column=1, padx=20)
        sound_star.play()
    if punti == 6:
        image_stella3.grid(row=3, column=2, padx=20)
        sound_star.play()
    if punti == 8:
        image_stella4.grid(row=3, column=3, padx=20)
        sound_star.play()
    if punti == 10:
        image_stella5.grid(row=3, column=4, padx=20)
        sound_star.play()
        mixer.music.load('suoni/musica_iniziale.wav')
        mixer.music.play()


def immagine_avanti():
    global counter
    counter += 1
    e.focus()  # porto il focus nuovamente sulla entry
    sound_click.play()

    if counter == 6:
        counter = 1
    if counter == 1:
        img1 = PhotoImage(file=lista_immagini[0])
        image_label.configure(image=img1)
        image_label.image = img1
        e.delete(0, END)
    elif counter == 2:
        img2 = PhotoImage(file=lista_immagini[1])
        image_label.configure(image=img2)
        image_label.image = img2
        e.delete(0, END)
    elif counter == 3:
        img3 = PhotoImage(file=lista_immagini[2])
        image_label.configure(image=img3)
        image_label.image = img3
        e.delete(0, END)
    elif counter == 4:
        img4 = PhotoImage(file=lista_immagini[3])
        image_label.configure(image=img4)
        image_label.image = img4
        e.delete(0, END)
    elif counter == 5:
        img5 = PhotoImage(file=lista_immagini[4])
        image_label.configure(image=img5)
        image_label.image = img5
        e.delete(0, END)

    btn_controlla["state"] = NORMAL
    e["state"] = NORMAL


# Creo il menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
argomenti_menu = Menu(my_menu)
my_menu.add_cascade(label="ARGOMENTI", menu=argomenti_menu)
argomenti_menu.add_command(label="ANIMALI", command=animali)
argomenti_menu.add_command(label="INSETTI", command=insetti)
argomenti_menu.add_command(label="NATURA", command=natura)
argomenti_menu.add_separator()
argomenti_menu.add_command(label="FRUTTA", command=frutta)
argomenti_menu.add_command(label="VERDURA", command=verdura)
argomenti_menu.add_command(label="CIBO", command=cibo)
argomenti_menu.add_separator()
argomenti_menu.add_command(label="CORPO UMANO", command=corpo)
argomenti_menu.add_command(label="ABBIGLIAMENTO", command=abbigliamento)
argomenti_menu.add_separator()
argomenti_menu.add_command(label="OGGETTI", command=oggetti)
argomenti_menu.add_command(label="MEZZI DI TRASPORTO", command=mezzi)
argomenti_menu.add_command(label="A SCUOLA", command=scuola)
argomenti_menu.add_separator()
argomenti_menu.add_command(label="ESCI", command=root.quit)

lista_immagini = [
    "immagini/banana.png",
    "immagini/budino.png",
    "immagini/elefante.png",
    "immagini/papera.png",
    "immagini/tavolo.png"
]

lista_parole = []

# l'idea è quella di sorteggiare un argomento iniziale in modo casuale
# lista_funzioni = [
#     frutta()
# ]


counter = 0
punti = 0

# l'idea è quella di sorteggiare un argomento iniziale in modo casuale
# sorteggia_funzione()


frame1 = Frame(root)

img = PhotoImage(file="immagini/macchina_da_scrivere.png")
image_label = Label(frame1, image=img)
image_label.grid(row=0, column=0, columnspan=5, sticky="ew")

frame1.pack()

frame2 = Frame(root)
e = Entry(frame2, font=("Helvetica", 24), width=22)  # width si riferisce al numero di caratteri
e.insert(3, "SCEGLI UN ARGOMENTO")
e['state'] = DISABLED
e.bind('<Return>', controlla)  # thanks to: https://youtu.be/NiQdsK3H57Y
e.grid(row=0, column=0, columnspan=2, padx=10, pady=15)
punteggio = Label(frame2, text="PUNTEGGIO: ", font=("Helvetica", 24), relief="sunken")
punteggio['state'] = DISABLED
punteggio.grid(row=0, column=3, padx=10, pady=15)
frame2.pack()

frame3 = Frame(root)
btn_controlla = Button(frame3, text="CONTROLLA", command=controlla, state="disabled")
btn_controlla.grid(row=0, column=1, pady=10, padx=20)
btn_indietro = Button(frame3, text="INDIETRO", command=immagine_indietro, state="disabled")
btn_indietro.grid(row=0, column=2, pady=10, padx=20)
btn_avanti = Button(frame3, text="AVANTI", command=immagine_avanti, state="disabled")
btn_avanti.grid(row=0, column=3, pady=10, padx=20)
frame3.pack()

# s.configure('TFrame')
# s.configure('frame4.TFrame', background='blue')
frame4 = Frame(root)
img_stellina = PhotoImage(file="immagini/stellina.png")
image_stella1 = Label(frame4, image=img_stellina)
image_stella1.grid(row=0, column=0, padx=10, pady=10)
image_stella1.grid_forget()
image_stella2 = Label(frame4, image=img_stellina)
image_stella2.grid(row=0, column=1, padx=10, pady=10)
image_stella2.grid_forget()
image_stella3 = Label(frame4, image=img_stellina)
image_stella3.grid(row=0, column=2, padx=20)
image_stella3.grid_forget()
image_stella4 = Label(frame4, image=img_stellina)
image_stella4.grid(row=0, column=3, padx=20)
image_stella4.grid_forget()
image_stella5 = Label(frame4, image=img_stellina)
image_stella5.grid(row=0, column=4, padx=20)
image_stella5.grid_forget()
frame4.pack()

root.mainloop()
