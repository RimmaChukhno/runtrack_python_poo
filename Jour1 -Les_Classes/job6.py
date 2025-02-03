class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom):
        self.prenom = nom

# Instanciation de l'objet Animal
mon_animal = Animal()

# Affichage de l'âge initial
print("L'age initial de l'animal :", mon_animal.age)

# Faire vieillir l'animal
mon_animal.vieillir()

# Affichage de l'âge mis à jour
print("L'age apres vieillissement :", mon_animal.age)

# Nommer l'animal
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
print("L'animal se nomme ", mon_animal.prenom)
