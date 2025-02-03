class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnees du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Valeur de x : {self.x}")

    def afficherY(self):
        print(f"Valeur de y : {self.y}")

    def changerX(self, new_x):
        self.x = new_x

    def changerY(self, new_y):
        self.y = new_y

# Exemple d'utilisation :
p = Point(3, 5)
p.afficherLesPoints()
p.changerX(10)
p.changerY(15)
p.afficherLesPoints()
