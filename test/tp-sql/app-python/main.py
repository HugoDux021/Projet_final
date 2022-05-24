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
    

#Création des boutons
Bout1 = tk.Button(Fen,text=u"Créer un nouveau QCM", command = commande_choix_creation)                     # Création des boutons
Bout2 = tk.Button(Fen,text=u"Modifier un QCM", command = commande_choix_modification)

#Affichage des boutton sur la fênetre
Bout1.pack()
Bout2.pack()

Fen.mainloop()











