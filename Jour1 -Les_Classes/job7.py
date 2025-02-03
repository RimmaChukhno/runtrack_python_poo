class Personnage:
    def __init__(self, x, y):
        """
        Constructeur de la classe Personnage.
        Initialise la position du personnage sur le plateau de jeu.
        
        :param x: Position horizontale (index de colonne)
        :param y: Position verticale (index de ligne)
        """
        self.x = x
        self.y = y

    def gauche(self):
        """
        Déplace le personnage d'une case vers la gauche.
        """
        self.x -= 1

    def droite(self):
        """
        Déplace le personnage d'une case vers la droite.
        """
        self.x += 1

    def bas(self):
        """
        Déplace le personnage d'une case vers le bas.
        """
        self.y += 1

    def haut(self):
        """
        Déplace le personnage d'une case vers le haut.
        """
        self.y -= 1

    def position(self):
        """
        Renvoie la position actuelle du personnage sous forme de tuple (x, y).
        
        :return: Tuple (x, y)
        """
        return (self.x, self.y)


# # Exemple d'utilisation
# if __name__ == "__main__":
#     # Création d'un personnage à la position (2, 3)
#     joueur = Personnage(2, 3)
    
#     # Affichage de la position initiale
#     print("Position initiale:", joueur.position())  # (2, 3)
    
#     # Déplacement vers la droite
#     joueur.droite()
#     print("Après déplacement à droite:", joueur.position())  # (3, 3)
    
#     # Déplacement vers le bas
#     joueur.bas()
#     print("Après déplacement en bas:", joueur.position())  # (3, 4)
    
#     # Déplacement vers la gauche
#     joueur.gauche()
#     print("Après déplacement à gauche:", joueur.position())  # (2, 4)
    
#     # Déplacement vers le haut
#     joueur.haut()
#     print("Après déplacement en haut:", joueur.position())  # (2, 3)