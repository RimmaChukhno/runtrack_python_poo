class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé
        self.__largeur = largeur    # Attribut privé

    # Accesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthode pour afficher les dimensions du rectangle
    def afficher(self):
        print(f"Rectangle: longueur = {self.__longueur}, largeur = {self.__largeur}")

# Création d'un rectangle avec longueur 10 et largeur 5
rectangle = Rectangle(10, 5)
rectangle.afficher()

# Changer/Modification des valeurs
rectangle.set_longueur(15)
rectangle.set_largeur(8)
rectangle.afficher()  # Vérifier que les modifications
