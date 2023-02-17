import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

### initialisation de l'heure
heure = datetime.now().replace(microsecond=0)

### initialisation de l'alarme
alarme = None

### fonction pour afficher l'heure
def afficher_heure():
    global heure, alarme
    heure_actuelle = datetime.now().replace(microsecond=0)
    if heure_actuelle != heure:
        heure = heure_actuelle
        label_heure.config(text=heure.strftime('%H:%M:%S'))
        if heure == alarme:
            label_alarme.config(text="Réveil !")
    root.after(1000, afficher_heure)

### fonction pour régler l'heure
def regler_heure():
    nouvelle_heure = entree_heure.get()
    nouvelle_minute = entree_minute.get()
    nouvelle_seconde = entree_seconde.get()
    try:
        nouvelle_heure = int(nouvelle_heure)
        nouvelle_minute = int(nouvelle_minute)
        nouvelle_seconde = int(nouvelle_seconde)
        nouvelle_heure = max(0, min(23, nouvelle_heure))
        nouvelle_minute = max(0, min(59, nouvelle_minute))
        nouvelle_seconde = max(0, min(59, nouvelle_seconde))
        heure_globale = datetime.now().replace(hour=nouvelle_heure, minute=nouvelle_minute, second=nouvelle_seconde, microsecond=0)
        global heure
        heure = heure_globale
        label_heure.config(text=heure.strftime('%H:%M:%S'))
    except ValueError:
        pass

### fonction pour régler l'alarme
def regler_alarme():
    nouvelle_heure = entree_alarme_heure.get()
    nouvelle_minute = entree_alarme_minute.get()
    nouvelle_seconde = entree_alarme_seconde.get()
    try:
        nouvelle_heure = int(nouvelle_heure)
        nouvelle_minute = int(nouvelle_minute)
        nouvelle_seconde = int(nouvelle_seconde)
        nouvelle_heure = max(0, min(23, nouvelle_heure))
        nouvelle_minute = max(0, min(59, nouvelle_minute))
        nouvelle_seconde = max(0, min(59, nouvelle_seconde))
        alarme_globale = datetime.now().replace(hour=nouvelle_heure, minute=nouvelle_minute, second=nouvelle_seconde, microsecond=0)
        global alarme
        alarme = alarme_globale
        label_alarme.config(text=alarme.strftime('%H:%M:%S'))
    except ValueError:
        pass

#### création de la fenêtre
root = tk.Tk()
root.title("Horloge")

##### création du label pour l'heure
label_heure = ttk.Label(root, text=heure.strftime('%H:%M:%S'), font=("TkDefaultFont", 50))
label_heure.pack(pady=20)

### création des champs pour régler l'heure
entree_heure = ttk.Entry(root, width=2, font=("TkDefaultFont", 20))
entree_heure.insert(0, heure.hour)
entree_heure.pack(side=tk.LEFT)
label_separateur1 = ttk.Label(root, text=":", font=("TkDefaultFont", 20))
label_separateur1.pack(side=tk.LEFT)
entree_minute = ttk.Entry(root, width=2, font=("TkDefaultFont", 20))
entree_minute.insert(0, heure.minute)
entree_minute.pack(side=tk.LEFT)
label_separateur2 = ttk.Label(root, text=":", font=("TkDefaultFont", 20))
label_separateur2.pack(side=tk.LEFT)
entree_seconde = ttk.Entry(root, width=2, font=("TkDefaultFont", 20))
entree_seconde.insert(0, heure.second)
entree_seconde.pack(side=tk.LEFT)
bouton_regler_heure = ttk.Button(root, text="Régler l'heure", command=regler_heure)
bouton_regler_heure.pack(side=tk.LEFT, padx=10)

#### création du label pour l'alarme
label_alarme = ttk.Label(root, text="", font=("TkDefaultFont", 30))
label_alarme.pack(pady=20)

#### création des champs pour régler l'alarme
entree_alarme_heure = ttk.Entry(root, width=2, font=("TkDefaultFont", 20))
entree_alarme_heure.pack(side=tk.LEFT)
label_separateur3 = ttk.Label(root, text=":", font=("TkDefaultFont", 20))
label_separateur3.pack(side=tk.LEFT)
entree_alarme_minute = ttk.Entry(root, width=2, font=("TkDefaultFont", 20))
entree_alarme_minute.pack(side=tk.LEFT)
label_separateur4 = ttk.Label(root, text=":", font=("TkDefaultFont", 20))
label_separateur4.pack(side=tk.LEFT)
entree_alarme_seconde = ttk.Entry(root, width=2, font=("TkDefaultFont", 20))
entree_alarme_seconde.pack(side=tk.LEFT)
bouton_regler_alarme = ttk.Button(root, text="Régler l'alarme", command=regler_alarme)
bouton_regler_alarme.pack(side=tk.LEFT, padx=10)

#### appel de la fonction pour afficher l'heure
afficher_heure()

### appel de la fonction pour vérifier l'alarme
def verifier_alarme():
    global alarme
    heure_actuelle = datetime.now().time()
    if alarme is not None and heure_actuelle >= alarme:
        message = f"ALARME !!! Il est {heure_actuelle.strftime('%H:%M:%S')}"
        label_alarme.configure(text=message, foreground="red")
    else:
        label_alarme.configure(foreground="black")
    # appel de cette fonction toutes les secondes
    root.after(1000, verifier_alarme)

### boucle principale de la fenêtre
root.mainloop()
