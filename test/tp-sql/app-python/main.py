# Logiciel de gestion de QCM
# Programme principal
# Créé par le groupe 1
# Audas Arthur, Ballot Bastient, Durand Hugo, Héron Julie

############################################################################
#Importation des bibliothèques et programmes associés

import tkinter as tk
import creation_QCM as crea
import lancement_QCM as lance


################################################################################
#fenetre du menu

#Création de la fênetre
Fen1 = tk.Tk() 
Fen1.title(u"Menu Principal" )

#Création du choix
def commande_choix_creation():
    Fen1.destroy()
    crea #lance le programme création
    
#Création du choix
def commande_choix_modification():  
    Fen1.destroy()
    lance #Lance le programme modification
    

#Création des boutons
Bout1 = tk.Button(Fen1,text=u"Créer un nouveau QCM", command = commande_choix_creation)                     # Création des boutons
Bout2 = tk.Button(Fen1,text=u"Modifier un QCM", command = commande_choix_modification)

#Affichage des boutton sur la fênetre
Bout1.pack()
Bout2.pack()

Fen1.mainloop()











