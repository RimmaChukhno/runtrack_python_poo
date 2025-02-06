class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé
        self.__largeur = largeur    # Attribut privé

    # Assesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthode pour calculer le périmètre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)  # Appel du constructeur de la classe parente
        self.__hauteur = hauteur             # Attribut privé

    # Assesseur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur pour la hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Méthode pour calculer le volume
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 10)

# Test des méthodes de la classe Rectangle
print("Longueur du rectangle:", rectangle.get_longueur())
print("Largeur du rectangle:", rectangle.get_largeur())
print("Périmètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

# Modification des attributs avec les mutateurs
rectangle.set_longueur(7)
rectangle.set_largeur(3)

# Affichage des nouvelles valeurs
print("\nAprès modification :")
print("Longueur du rectangle:", rectangle.get_longueur())
print("Largeur du rectangle:", rectangle.get_largeur())
print("Périmètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(5, 10, 15)

# Test des méthodes de la classe Parallelepipede
print("\nVolume du parallélépipède:", parallelepipede.volume())