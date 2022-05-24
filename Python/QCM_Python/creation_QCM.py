# Logiciel de gestion de QCM
# Programme création de QCM
# Créé par le groupe 1
# Audas Arthur, Ballot Bastient, Durand Hugo, Héron Julie


############################################################################
#Importation des bibliothèques et programmes associés
import tkinter as tk    #Pour l'interface graphique
import mariadb



############################################################################
# Création des classes

class Question:
    def __init__(self, enonce="", rep1="", rep2="", rep3="", repjuste="" ):  # Définition des objetss de la classe
        self.enonce = enonce
        self.rep1 = rep1
        self.rep2= rep2
        self.rep3 = rep3
        self.repjuste = repjuste
    #permet d'afficher avec print
    def __str__(self):
        return "enonce=%s ; rep1=%s ; rep2=%s ; rep3=%s ; repJuste=%s" % (self.enonce, self.rep1, self.rep2, self.rep3, self.repjuste)


#############
class Nom_QCM:

    def __init__(self, connexion) -> None:
        # Propriété de l'objet application
        self.__nom = ''
        self.__connexion = connexion


    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        if isinstance(nom, str): 
            self.__nom = nom

    def ajouter_un_QCM(self, nom_qcm):
        try:
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO Registre_QCM (`nom`) VALUES (?);',(nom_qcm,))
            self.__connexion.commit()
            return 'Le QCM a bien été ajoutée'
        except mariadb.Error as e:     
            return f'Erreur lors de l\'ajout {e} '


#################
class question:

    def __init__(self, connexion) -> None:
        # Propriété de l'objet application
        self.__nom = ''
        self.__editeur = ''
        self.__version = "22.04"
        self.__connexion = connexion


    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        if isinstance(nom, str): 
            self.__nom = nom

    def get_editeur(self):
        return self.__editeur

    def set_editeur(self, editeur):
        if isinstance(editeur, str): 
            self.__editeur = editeur

    def get_version(self):
        return self.__version

    def set_version(self, version):
        if isinstance(version, str): 
            self.__version = version
    
    # • Permettre l’ajout d’une application
    def ajouter_une_question(self, liste_donnees):
        try:
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO question ( `intitule`, `rep_A`, `rep_B`, `rep_C`, `rep_Correcte`)  VALUES (?, ?, ?,?,?);',(liste_donnees[0], liste_donnees[1], liste_donnees[2], liste_donnees[3], liste_donnees[4],))
            self.__connexion.commit()
            return 'La question a bien été ajoutée'
        except mariadb.Error as e:     
            return f'Erreur lors de l\'ajout {e} '
        
n=1 #compteur du nombre de question


############################################################################
#fenetre de saisie du nom du QCM

Fen0 = tk.Tk() #Création de la fênetre, des entrées, etc
Fen0.title(u"Nom du QCM" )
Af0 = tk.Label(Fen0, text= u"Ecrire le nom de votre QCM." )
Af1 = tk.Label(Fen0, text= u"" )
Ent0 = tk.Entry(Fen0)

def ma_commande_nom_qcm():  
    nom_qcm = Ent0.get()
    if nom_qcm == "": 
        Af1.configure(text= u"Vous n'avez pas mis de nom" )                     # On précise le problème à l'utilisateur.
    else:       
        Af1.configure(text= u"Le nom est bien enregistré" )
        Fen0.destroy()
        
        #Enregistrement sur Mysql
        Nom_QCM.ajouter_un_QCM('',nom_qcm)
        
        
Bout0 = tk.Button(Fen0,text=u"Valider", command=ma_commande_nom_qcm)

Af0.pack()           
Ent0.pack()
Af1.pack()
Bout0.pack()

Fen0.mainloop()

############################################################################
#fenetre de saisie des questions

Fen1 = tk.Tk() #Création de la fênetre, des entrées, etc
Fen1.title(u"Création question" )

Af1 = tk.Label(Fen1, text= u"Ecrire une question." )
Af2 = tk.Label(Fen1, text="Ecrire la réponse A." )
Af3 = tk.Label(Fen1, text="Ecrire la réponse B." )
Af4 = tk.Label(Fen1, text="Ecrire la réponse C." )
Af5 = tk.Label(Fen1, text="Ecrire la réponse juste (A, B ou C)." )
Af6 = tk.Label(Fen1, text="" )

Ent1 = tk.Entry(Fen1)
Ent2 = tk.Entry(Fen1)
Ent3 = tk.Entry(Fen1)
Ent4 = tk.Entry(Fen1)
Ent5 = tk.Entry(Fen1)

#on stocke les questions dans une liste
listOfQuestions = []
Q1 = Question() # Pour faciliter l'écriture on renomme la classe


def ma_commande1():  # On crée une commande qui à pour but de vérifier si toutes les entrées possèdent un texte.
    enonce=Ent1.get()    # On renomme les textes entrés pur faciliter l'utilisation de ceux-ci et meiux les reconnaitre.
    rep1=Ent2.get()
    rep2=Ent3.get()
    rep3=Ent4.get()
    repjuste=Ent5.get()
    if enonce=="" or rep1=="" or rep2=="" or rep3=="" or repjuste=="":              # On intègre une condition permettant de vérifier si les entrées sont vides.
        Bout2.pack_forget ()                                                            # Ainsi le bouton disparaitra.
        Af6.configure(text= u"Vous n'avez pas rempli toutes les cases" )                     # On précise le problème à l'utilisateur.
    else:
        global n        # On intègre le compteur de question à la commande
        
        Question_entiere = [enonce, rep1, rep2, rep3, repjuste]
        
        Q1.enonce = enonce   # On enregistre le texte entré dans l'objet correspondant au texte, ici l'objet énoncé, !!!!! dans la classe correspondant à la question. !!!!!!
        Ent1.delete (0,tk.END)  # On supprime le texte contenue dans l'entrée pour pouvoir entrer un nouveau texte
        Q1.rep1 = rep1
        Ent2.delete (0,tk.END)
        Q1.rep2 = rep2
        Ent3.delete (0,tk.END)
        Q1.rep3 = rep3
        Ent4.delete (0,tk.END)
        Q1.repjuste = repjuste
        Ent5.delete (0,tk.END)
        
        n=n+1                   # Le compteur augmente à chaque fois que l'on appuie sur le bouton.
        
        Af1.configure(text= u"Ecrire une question "+ str(n)+'.')                         # On met à jour le numéro de la question, de l'énoncé ....
        Af2.configure(text= u"Ecrire la réponse A, de la question "+ str(n)+'.')
        Af3.configure(text= u"Ecrire la réponse B, de la question "+ str(n)+'.')
        Af4.configure(text= u"Ecrire la réponse C, de la question "+ str(n)+'.')
        Af5.configure(text= u"Ecrire la réponse juste (A, B ou C), de la question "+ str(n)+'.')
        
        Bout2.pack()
        
        #Enregistrement des valeurs en local
        Q = Question(Q1.enonce, Q1.rep1, Q1.rep2, Q1.rep3, Q1.repjuste)
        listOfQuestions.append(Q)
        Bout1.pack ()           # Si les entrées possédent un texte le bouton apparaitra.
        Af6.configure(text= u"" )

        #Enregistrement sur Mysql
        question.ajouter_une_question(Question_entiere)
        

    
def ma_commande2():
    enonce=Ent1.get()       # On renomme les textes entrés pour faciliter l'utilisation de ceux-ci et meiux les reconnaitre.
    Q1.enonce=enonce         # On enregistre le texte entré dans l'objet correspondant au texte, ici l'objet énoncé, !!!!! dans la classe correspondant à la question. !!!!!!
    rep1=Ent2.get()         #De même
    Q1.rep1=rep1
    rep2=Ent3.get()         #De même
    Q1.rep2=rep2
    rep3=Ent4.get()         #De même
    Q1.rep3= rep3
    repjuste=Ent5.get()     #De même
    Q1.repjuste=repjuste
    
    if enonce=="" or rep1=="" or rep2=="" or rep3=="" or repjuste=="":                                                      # Ainsi le bouton disparaitra.
        Af6.configure(text= u"Vous n'avez pas rempli toutes les cases" ) 
    
    else:
        #Enregistrement des valeurs en local
        Q = Question(Q1.enonce, Q1.rep1, Q1.rep2, Q1.rep3, Q1.repjuste)
        listOfQuestions.append(Q)
        #Enregistrement sur Mysql
        Question_entiere = [enonce, rep1, rep2, rep3, repjuste]
        question.ajouter_une_question(Question_entiere)
        #Fermeture de la fenetre
        Fen1.destroy()


Bout1 = tk.Button(Fen1,text=u"Question suivante", command=ma_commande1)                     # Création des boutons
Bout2 = tk.Button(Fen1,text=u"Enregistrer", command=ma_commande2)

Af1.pack()              # Affichage des différents bidules.
Ent1.pack()
Af2.pack()
Ent2.pack()
Af3.pack()
Ent3.pack()
Af4.pack()
Ent4.pack()
Af5.pack()
Ent5.pack()
Af6.pack()
Bout1.pack()

Bout2.pack_forget()

Fen1.mainloop()

#affiche les questions sauvegardees dans la liste
for index in range(len(listOfQuestions)):
    print(listOfQuestions[index])
    
    
    
    
    
    
    
    