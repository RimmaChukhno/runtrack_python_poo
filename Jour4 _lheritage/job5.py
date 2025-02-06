import math

# Classe Forme
class Forme:
    def aire(self):
        return 0

# Classe Rectangle qui hérite de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Classe Cercle qui hérite de Forme (math)
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * (self.radius ** 2)

# Test des classes
rectangle = Rectangle(10, 5)
cercle = Cercle(7)

print(f"Aire du rectangle : {rectangle.aire()}")  # Affiche 50
print(f"Aire du cercle : {cercle.aire():.2f}")  # Affiche 153.94 (arrondi à 2 décimales)
