import tkinter as tk
 
laby = [
    "**************P**************",
    "*    *         *         *  *",
    "* ** * ** **** * **** **** **",
    "* *  *  * *  *      * *    **",
    "* * *** *   *********   ** **",
    "* *     ***** *   * **** * **",
    "* **** **  *    * *         *",
    "*    *    ******* ** ****** *",
    "**** ****** *   *      *  ***",
    "*  *    *   *** ******      *",
    "**   ****** *        * **** *",    #parcours du labyrinthe
    "****      *    *****   *    *",
    "** *****  **** *   ****** ***",
    "*        *     * *   *    * *",
    "* ******** ***** * * * **   *",
    "*     *          * * *  *** *",
    "* ********* ******** **     *",
    "*        *    *    *  ***** *",
    "********** ** * ** ****   ***",
    "*          *    *       *   *",
    "*************************** *",
   ]
 
WIDTH = 625     #taille de la fenetre en longeur
HEIGHT = 500    #taille de la fenetre en largeur

fenetre = tk.Tk()                             #Fenetre Principale
fenetre.title('Labyrinthe Adventure Project') #titre en haut de la fenetre
fenetre.geometry('%sx%s'%(WIDTH,HEIGHT))      #Géometrie de la fentre avec la taille en longeur et largeur entré precedament
 
#Canvas Principale et focus.
canvaPrincipale = tk.Canvas(fenetre, width=WIDTH, height=HEIGHT -30, bg='white') #Enlève 30 sur le HEIGHT, pour le bouton Quitter
canvaPrincipale.pack()                                                           #permet de mettre une petite barre en bas pour quitter
canvaPrincipale.focus_set()                                                      #separe la fenetre de jeu et l'espace pour quitter

#Vérification des mouvements (Collision entre le rectangle et les lignes)
def check_mouvement():
    """Détection et vérification des couleurs"""
    #On trouve les coordonnés du rectangle (player) et on cherche si les coordonnés entre en collision avec les rectangles
    les_rectangles = canvaPrincipale.find_overlapping(*canvaPrincipale.coords(dico['player']))       
    #À partir du ID, on récupère la couleurs des rectangles 
    colors = [canvaPrincipale.itemcget(id, 'fill') for id in les_rectangles]    
    #Si une des lignes(du tuple), est de couleur ROUGE, le personnage n'avance pas                                                                                             
    if '#A62216' in colors or '' in colors :                                                     
        return False
    #Sinon,on peut avancer
    return True   
                                                                                     
 
## Touche appuyé, mouvement et appele de check_mouvement
def direction(evt):
    key_str = evt.keysym              #Détecte les touches
    x,y = 0,0                         #Déclaration de variables temporaires x et y en 0
    if key_str == 'Up':               #Si la touche detecter est monter y prend la valeur -10 et le personnage monte du coup
        y = -10
    elif key_str == 'Down':           #Si la touche detecter est decendre y prend la valeur 10 et le personnage descend du coup
        y = 10
    elif key_str == 'Left':           #Si la touche detecter est gauche x prend la valeur -10 et le personnage va a gauche
        x = -10
    elif key_str == 'Right':          #Si la touche detecter est droite x prend la valeur 10 et le personnage va a droite
        x = 10
    else:                             #Autre touche, aucune action
        print('Touche inconnu :-)', key_str)
 
    
    canvaPrincipale.move(dico['player'], x, y)               #Bouge le rectangle (player) en x et y
                                                             #Vérifie si le rectangle touche à une ligne ROUGE
    if not check_mouvement():
        canvaPrincipale.move(dico['player'], (-1)*x, (-1)*y) #S'il touche une ligne rouge, on recule les axes X et Y de -1
 
X,Y = 20,20             #Commence au pixel X et Y du canvaPrincipale pour etre au centre de la fenetre
Z = 20                  #Longueur des mur rouge
 

dico = {}                                #Dictionnaire des lignes et du rectangle 'player'
for nb, lines in enumerate(laby):        #Insere un numero chacune des lignes
    dico[nb] = {}                        #On sauvegarde le numéro de la ligne au dictionnaire
                                         #On créer un dictionnaire, dans le dictionnaire.
    for nnb, lettre in enumerate(lines): #Insere une lettre a chacune des symboles des differentes lignes
        if lettre != 'P':                #Si la lettre n'est pas p alors c'est soit un mur soit le bon chemin
            if lettre == '*':            #Si la lettre est * alors c'est un mur
                color = '#A62216'        #Met les murs en ROUGE
                #crée les murs comme des rectangles de 20 en largeur et 20 en longeur
                rectangle = canvaPrincipale.create_rectangle(X,Y+20,X+Z,Y, fill=color)
            else:
                color = 'white'          #Sinon met les espaces en BLANC
            
        else:
          
           #On crée un rectangle (plus petit), qui sera le joueur
           #Le rectangle sera de couleur BLEU 
            rect_player = canvaPrincipale.create_rectangle(X+5,Y+5,X+15,Y+15, fill='#2721D2')  
           #On sauvegarde le rectangle (joeur) au dico                                                               
            dico['player'] = rect_player  
        #Incrémente de +Z (longueur d'une ligne), l'axe X
        X += Z                                                                                 
    #Remet l'Axe X, à zero (+20)
    X = 20                                                                                    
    #Incrémente de +Z (longueur d'une ligne = +20), l'axe Y
    Y += Z                                                                                     

canvaPerimetre = canvaPrincipale.create_rectangle(
    20,20, 600, 440)                                                      #perimetre en noir qui limite les contours du labyrinthe
    
canvaPrincipale.bind('<Key>', direction)                                  #lie les touche du clavier (le canva) à la fonction direction

btn_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.destroy) #boutton quitter qui commande la fermeture de la fenetre de jeux
btn_quitter.pack()                                         
     
fenetre.mainloop()                                                        #Permet le demarrage des réceptions d'événements associé à la fenêtre
