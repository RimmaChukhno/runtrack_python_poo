# Définition de la classe Forme
class Forme:
    def aire(self):
        return 0

# Définition de la classe Rectangle qui hérite de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharge de la méthode aire pour calculer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur

# Création d'une instance de Rectangle et affichage de l'aire
rectangle = Rectangle(5, 10)
print("L'aire du rectangle est :", rectangle.aire())
