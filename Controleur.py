import Modele

class ControleurCourbes(object):
    """ Gere un ensemble de courbes. """
    def __init__(self):
        self.courbes = []

    def ajouterCourbe(self, courbe):
        """ Ajoute une courbe supplementaire. 
        Fonction interne. Utiliser plutot nouvelleDroite... """
        self.courbes.append(courbe) 

    def dessiner(self, dessinerControle, dessinerPoint):
        """ Dessine les courbes. """
        # dessine les point de la courbe
        for courbe in self.courbes:
            courbe.dessinerPoints(dessinerPoint)
        # dessine les point de controle
        for courbe in self.courbes:
            courbe.dessinerControles(dessinerControle)
    
    def nouvelleHorizontale(self):
        """ Ajoute une nouvelle horizontale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        horizontale = Modele.Horizontale()
        self.ajouterCourbe(horizontale)
        return horizontale.ajouterControle
