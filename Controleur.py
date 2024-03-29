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
    
    def nouvelleFormeDeveloppee(self):
        """ Ajoute une nouvelle forme développée initialement vide.
        Retourne une fonction permettant d'ajouter les points de contrôle. """
        formeDeveloppee = Modele.FormeDeveloppee()  # Assurez-vous que FormeDeveloppee est définie dans Modele
        self.ajouterCourbe(formeDeveloppee)
        return formeDeveloppee.ajouterControle
    
    def nouvelleCalculMatriciel(self):
        calculMatriciel = Modele.CalculMatriciel()
        self.ajouterCourbe(calculMatriciel)
        return calculMatriciel.ajouterControle
    
    def nouvelleAlgorithmeDeDeCasteljau(self):
        algorithmeDeDeCasteljau = Modele.AlgorithmeDeDeCasteljau()
        self.ajouterCourbe(algorithmeDeDeCasteljau)
        return algorithmeDeDeCasteljau.ajouterControle



