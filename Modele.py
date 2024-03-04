import numpy as np


class Courbe(object):
    """ Classe generique definissant une courbe. """
    
    def __init__(self):
        self.controles = []

    def dessinerControles(self, dessinerControle):
        """ Dessine les points de controle de la courbe. """
        for controle in self.controles:
            dessinerControle(controle)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Methode a redefinir dans les classes derivees. """
        pass

    def ajouterControle(self, point):
        """ Ajoute un point de controle. """
        print(point)
        self.controles.append(point)

class Horizontale(Courbe):
    """ Definit une horizontale. Derive de Courbe. """                  
                
    def ajouterControle(self, point):
        """ Ajoute un point de controle a l'horizontale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        if len(self.controles) == 2 :
            x1 = self.controles[0][0]
            x2 = self.controles[1][0]
            y = self.controles[0][1]
            xMin = min(x1,x2)
            xMax = max(x1, x2)
            for x in range(xMin, xMax):
                dessinerPoint((x, y))    
                
class FormeDeveloppee(Courbe):
    """ Classe pour dessiner une courbe de Bézier en utilisant la forme développée. """

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe de Bézier en utilisant la forme développée. """
        if len(self.controles) == 4:
            for t in self.generate_t_values():
                x, y = self.calculate_bezier_point(t)
                dessinerPoint((x, y))

    def calculate_bezier_point(self, t):
        """ Calcule un point sur la courbe de Bézier pour une valeur de t donnée. """
        P0, P1, P2, P3 = self.controles
        x = (1-t)**3 * P0[0] + 3*t*(1-t)**2 * P1[0] + 3*t**2*(1-t) * P2[0] + t**3 * P3[0]
        y = (1-t)**3 * P0[1] + 3*t*(1-t)**2 * P1[1] + 3*t**2*(1-t) * P2[1] + t**3 * P3[1]
        return x, y

    def generate_t_values(self, num_points=100):
        """ Génère une liste de valeurs de t pour tracer la courbe. """
        return [i / (num_points - 1) for i in range(num_points)]
    
class CalculMatriciel(Courbe):
    """Classe pour dessiner une courbe de Bézier en utilisant le calcul matriciel."""

    def __init__(self):
        super().__init__()

    def dessinerPoints(self, dessinerPoint):
        """Dessine la courbe de Bézier en utilisant le calcul matriciel."""
        if len(self.controles) == 4:
            # Matrice de calcul pour une courbe de Bézier cubique
            matrice = np.array([[-1, 3, -3, 1],
                                [3, -6, 3, 0],
                                [-3, 3, 0, 0],
                                [1, 0, 0, 0]])
            # Points de contrôle
            points = np.array(self.controles)
            # Dessine les points de la courbe
            for t in np.linspace(0, 1, 100):
                vecteurT = np.array([t**3, t**2, t, 1])
                point = vecteurT.dot(matrice).dot(points)
                dessinerPoint((int(point[0]), int(point[1])))
                

                



                
                
           

