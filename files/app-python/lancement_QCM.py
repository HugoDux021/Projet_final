# Logiciel de gestion de QCM
# Programme création de QCM
# Créé par le groupe 1
# Audas Arthur, Ballot Bastien, Durand Hugo, Héron Julie

############################################################################
#Importation des bibliothèques et programmes associés
import tkinter as tk
from tkinter import ttk
import mariadb
import config
import connect_db as db


############################################################################
#Connexion à la base de données Maria_db

bdd = db.ConnectDb(config.config)
connexion = bdd.connect()
cursor = connexion.cursor()


############################################################################
#Récupération des données:
    
#QCM existants
cursor.execute('SELECT nom FROM QCM;')
liste_qcm = cursor.fetchall()



#Questions pour un QCM donné
def Choix_QCM():
    global nom_qcm
    nom_qcm = menu_deroul.get()    
    cursor.execute("SELECT ID FROM QCM WHERE nom = ? ", (nom_qcm,))
    global id_qcm
    id_qcm = cursor.fetchall()
    cursor.execute("SELECT * FROM question WHERE QCM_id = ? ", (id_qcm[0][0],))
    global liste_question
    liste_question = cursor.fetchall()
    print(liste_question)
    Fen0.destroy()
    

def validation_choix(l):
    tex1 = tk.Label(Fen0, text=f'Le fichier {menu_deroul.get()} à bien été séléctionné.', fg='green')
    tex1.pack()
    Bout1.pack()



# Création de la fenetre
Fen0 = tk.Tk()
Fen0.title(u"Liste des QCM disponibles")
AF0 = tk.Label(Fen0, text=u'Veuillez choisir le QCM')

# Fenetere deroulante
# Sert à choisir le QCM
menu_deroul = ttk.Combobox(Fen0, values = liste_qcm)
#menu_deroul.current(0)
menu_deroul.bind("<<ComboboxSelected>>", validation_choix)

#bouton de validation
Bout1 = tk.Button(Fen0,text=u"Valider", command=Choix_QCM) 
 
# Affichage sur la fenetre
AF0.pack()
menu_deroul.pack()
Fen0.mainloop()

############################################################################
#Lancement du QCM


#partie affichage de la fenetre du jeu
Fen1 = tk.Tk()
Fen1.title(u"Projet Final" )

Af1 = tk.Label(Fen1, text= u"Bonjour, vous allez maintenant pouvoir commencer le QCM. Etes-vous prêt ?" )          #Présentation
Af2 = tk.Label(Fen1, text="" )                #Enoncé
Af3 = tk.Label(Fen1, text="" )                #Rép1
Af4 = tk.Label(Fen1, text="" )                #Rép2
Af5 = tk.Label(Fen1, text="" )                #Rép3
Af6 = tk.Label(Fen1, text="Quelle est votre réponse ?" )
Af7 = tk.Label(Fen1, text="" )        # On l'utilisisera pour dire bonne ou mauvaise réponse.
Ent1 = tk.Entry(Fen1)            #Le joueur y rentrera sa réponse

n=0             #Compteur du nombre de click sur le bout1
k=1             #Compteur des questions

def ma_commande12():
    global n
    global k
    #verification que l'index ne sorte pas de la liste
    if k-1<len(liste_question):
        question_actuelle = liste_question[k-1]
        n=n+1           # Le compteur de click augmentera à chaque click, ou à chaque fois que la commande est éxecutée !
        if n==1:        # APrès le premier click :
            Af1.configure ( text=u"Veuillez répondre en entrant la lettre correspondant à votre choix." )
            Bout1.configure(text=u"Ok" )
        elif n==2:          # Après le deuxième click le jeu commence.
            Af1.pack_forget()               #L'affichage 1 ne sera plus utile.
            Af2.pack()                  # On affiche l'énoncé des questions.
            Af3.pack()
            Af4.pack()
            Af5.pack()
            Af6.pack()
            Ent1.pack()                 # On affiche l'endroit où le joueur rentrera sa réponse
            Af2.configure ( text=u"Question "+str(k) + " : " + question_actuelle[1])
            Af3.configure ( text=u"Réponse A : " + question_actuelle[2])
            Af4.configure ( text=u"Réponse B : " + question_actuelle[3])
            Af5.configure ( text=u"Réponse C : " + question_actuelle[4])
            Bout1.pack_forget()
            Bout3.pack()     # Le bouton 3 vérifiera la justesse de la réponse
        else:               # A chaque fois que le joueur clickera sur le bouton 3, la réponse du joueur sera vérifiée.
            repjoueur = Ent1.get()        #On enregistre la réponse sous un autre nom qui nous permettra de mieux la reconnaitre.
            repjoueur = repjoueur.upper()        # Ce que rentre le joueur est mis en majuscule.
            if repjoueur == question_actuelle[5]:
                Af7.pack()
                Af7.configure(text=u"Bonne réponse ! vous pouvez passer la question suivante" )
                Bout2.pack()        # LE bouton permettant de passer à la question suivante apparait.
            else :
                Af7.pack()
                Af7.configure(text=u"Mauvaise réponse ! Vous avez répondu " + repjoueur + u" alors que la bonne réponse était la " + question_actuelle[5])
                Bout2.pack()
                
                
def ma_commande22 (): # Commande pour paser à la question suivante.
    global k
    k=k+1               #On augmente le compteur de question.
    #verification que l'index ne sorte pas de la liste
    if k-1<len(liste_question):
        question_actuelle = liste_question[k-1]
        Ent1.delete(0,tk.END)
        Af2.configure ( text=u"Question "+str(k) + " : " + question_actuelle[1])
        Af3.configure ( text=u"Réponse A : " + question_actuelle[2])
        Af4.configure ( text=u"Réponse B : " + question_actuelle[3])
        Af5.configure ( text=u"Réponse C : " + question_actuelle[4])
        Bout2.pack_forget()             #Le bouton disparait.
    else:
        #fin des questions on ferme la fenetre
        Fen1.destroy()
        
Bout1 = tk.Button(Fen1,text=u"Oui",command=ma_commande12)
Bout2 = tk.Button(Fen1,text=u"Question Suivante",command=ma_commande22)
Bout3 = tk.Button(Fen1,text=u"Valider",command=ma_commande12)

Af1.pack()
Af2.pack_forget()
Af3.pack_forget()
Af4.pack_forget()
Af5.pack_forget()
Af6.pack_forget()
Ent1.pack_forget()
Bout1.pack()
Af7.pack_forget()
Bout2.pack_forget()
Bout3.pack_forget()

Fen1.mainloop()