# Logiciel de gestion de QCM
# Programme création de QCM
# Créé par le groupe 1
# Audas Arthur, Ballot Bastient, Durand Hugo, Héron Julie

############################################################################
#Importation des bibliothèques et programmes associés

import tkinter as tk    #Pour l'interface graphique

############################################################################
#Lancement du QCM

if len(listOfQuestions)>0 :
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
        if k-1<len(listOfQuestions):
            questionCourante = listOfQuestions[k-1]
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
                Bout1.configure(text=u"Valider ma réponse." )        # Le bouton 1 vérifiera dorénavant la justesse de la réponse
                Af2.configure ( text=u"Question "+str(k) + " : "+questionCourante.enonce            # Affichage des réponses.
                                )
                Af3.configure ( text=u"Réponse A : "+
                                questionCourante.rep1)
                Af4.configure ( text=u"Réponse B : "+
                                questionCourante.rep2)
                Af5.configure ( text=u"Réponse C : "+
                                questionCourante.rep3)
            else:               # A chaque fois que le joueur clickera sur le bouton 1, la réponse du joueur sera vérifiée.
                repjoueur=Ent1.get()        #On enregistre la réponse sous un autre nom qui nous permettra de meux la reconnaitre.
                repjoueur = repjoueur.upper()        # Ce que rentre le joueur est mis en majuscule.
                if repjoueur==questionCourante.repjuste:
                    Af7.pack()
                    Af7.configure(text=u"Bonne réponse ! vous pouvez passer la question suivante" )
                    Bout2.pack()        # LE bouton permettant de passer à la question suivante apparait.
                else :
                    Af7.pack()
                    Af7.configure(text=u"Mauvaise réponse ! Vous avez répondu "+repjoueur+u" alors que la bonne réponse était la "+questionCourante.repjuste)
                    Bout2.pack()
                    
                    
    def ma_commande22 (): # Commande pour paser à la question suivante.
        global k
        k=k+1               #On augmente le compteur de question.
        #verification que l'index ne sorte pas de la liste
        if k-1<len(listOfQuestions):
            questionCourante = listOfQuestions[k-1]
            Ent1.delete(0,END)
            Af2.configure ( text=u"Question "+str(k)+         # On affiche la question suivante.
                                " : " + questionCourante.enonce)
            Af3.configure ( text=u"Réponse A : "
                                 + questionCourante.rep1)
            Af4.configure ( text=u"Réponse B : "
                                 + questionCourante.rep2)
            Af5.configure ( text=u"Réponse C : "
                                 + questionCourante.rep3)
            Bout2.pack_forget()             #Le bouton disparait.
        else:
            #fin des questions on ferme la fenetre
            Fen1.destroy()
            
    Bout1 = tk.Button(Fen1,text=u"Oui",command=ma_commande12)
    Bout2 = tk.Button(Fen1,text=u"Question Suivante",command=ma_commande22)
    
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
    
    Fen1.mainloop()