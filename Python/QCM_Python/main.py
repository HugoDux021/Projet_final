# Logiciel de gestion de QCM
# Programme principal
# Créé par le groupe 1
# Audas Arthur, Ballot Bastien, Durand Hugo, Héron Julie

############################################################################
#Importation des bibliothèques et programmes associés

import tkinter as tk

################################################################################
#fenetre du menu

#Création de la fênetre
Fen = tk.Tk() 
Fen.title(u"Menu Principal" )

#Création du choix 1
def commande_choix_creation():
    Fen.destroy()
    import creation_QCM #lance le programme création

    
#Création du choix 2
def commande_choix_modification():  
    Fen.destroy()
    import lancement_QCM #Lance le programme modification
    
#Espace pour le coté graphique
Af1 = tk.Label(Fen, text= u"" )
Af2 = tk.Label(Fen, text= u"" )
Af3 = tk.Label(Fen, text= u"" )

#Création des boutons
Bout1 = tk.Button(Fen,text=u"Créer un nouveau QCM", command = commande_choix_creation)                     # Création des boutons
Bout2 = tk.Button(Fen,text=u"Jouer à un QCM", command = commande_choix_modification)

#Affichage des boutton sur la fênetre
Af1.pack()
Bout1.pack()
Af2.pack()
Bout2.pack()
Af3.pack()

#Maintient de la fenetre
Fen.mainloop()











