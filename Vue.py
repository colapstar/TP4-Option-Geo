import tkinter
from PIL import ImageTk
from PIL import Image
from PIL import ImageDraw

import Controleur

class VueCourbes(object):
    """ Gere l'affichage et la manipulation de courbe avec la bibliotheque Tkinter. """
    def __init__(self, largeur, hauteur):
        self.controleur = Controleur.ControleurCourbes()
        self.largeur = largeur
        self.hauteur = hauteur
        self.canvas = []
        self.image = []
        self.imageDraw = []
        self.imageTk = []
        self.outilsCourant = []

    def callbackButton1(self, event):
        """ Bouton gauche : utilise l'outils courant. """
        if self.outilsCourant :
            self.outilsCourant((event.x, event.y))
        self.majAffichage()
        
    def callbackButton3(self, event):
        """ Bouton droit : termine l'outils courant. """
        self.outilsCourant = []
        self.majAffichage()

    def callbackNouveau(self):
        """ Supprime toutes les courbes. """
        self.controleur = Controleur.ControleurCourbes()
        self.majAffichage()
        
    def callbackHorizontale(self):
        """ Initialise l'outils courant pour ajouter d'une nouvelle horizontale. """
        self.outilsCourant = self.controleur.nouvelleHorizontale()
        
    def callbackFormeDeveloppee(self):
        """ Initialise l'outil courant pour ajouter une nouvelle courbe de Bézier avec la forme développée. """
        self.outilsCourant = self.controleur.nouvelleFormeDeveloppee() 
        
    def callbackCalculMatriciel(self):
        """ Initialise l'outil courant pour ajouter une nouvelle courbe de Bézier utilisant le calcul matriciel. """
        self.outilsCourant = self.controleur.nouvelleCalculMatriciel() 
        
    def callbackAlgorithmeDeDeCasteljau(self):
        """ Initialise l'outil courant pour ajouter une nouvelle courbe de Bézier avec l'algorithme de De Casteljau. """
        self.outilsCourant = self.controleur.nouvelleAlgorithmeDeDeCasteljau()          

    def majAffichage(self):
        """ Met a jour l'affichage.. """
        # efface la zone de dessin
        self.imageDraw.rectangle([0, 0, self.largeur, self.hauteur], fill='lightgrey')
        # dessine les courbes
        fonctionPoint = lambda p : self.imageDraw.point(p, (0,0,0))
        fonctionControle = lambda p : self.imageDraw.rectangle([p[0]-3, p[1]-3, p[0]+3, p[1]+3], fill='blue')
        self.controleur.dessiner(fonctionControle,fonctionPoint)
        # ImageTk : structure pour afficher l'image
        self.imageTk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(self.largeur/2 + 1, self.hauteur/2 + 1, image=self.imageTk)

    def executer(self):
        """ Initialise et lance le programme. """
        # fenetre principale
        fenetre = tkinter.Tk()
        fenetre.title("Trace courbes")
        fenetre.resizable(0,0)
        # menu
        menu = tkinter.Menu(fenetre)
        fenetre.config(menu=menu)
        filemenu = tkinter.Menu(menu)
        menu.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_command(label="Nouveau", command=self.callbackNouveau)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=fenetre.destroy)
        toolsmenu = tkinter.Menu(menu)
        menu.add_cascade(label="Outils", menu=toolsmenu)
        toolsmenu.add_command(label="Ajouter Horizontale", command=self.callbackHorizontale)
        toolsmenu.add_command(label="Ajouter Forme développée", command=self.callbackFormeDeveloppee)
        toolsmenu.add_command(label="Ajouter Calcul matriciel", command=self.callbackCalculMatriciel)
        toolsmenu.add_command(label="Ajouter Algorithme de De Casteljau", command=self.callbackAlgorithmeDeDeCasteljau)
        # Canvas : widget pour le dessin dans la fenetre principale
        self.canvas = tkinter.Canvas(fenetre, width=self.largeur, height=self.hauteur, bg='white')
        self.canvas.bind("<Button-1>", self.callbackButton1)
        self.canvas.bind("<Button-3>", self.callbackButton3)
        self.canvas.pack()
        # Image : structure contenant les donnees de l'image manipule
        self.image = Image.new("RGB", (self.largeur, self.hauteur), 'lightgrey')
        # ImageDraw : structure pour manipuler l'image
        self.imageDraw = ImageDraw.Draw(self.image)
        # met a jour l'affichage 
        self.majAffichage()
        # lance le programme
        fenetre.mainloop()
