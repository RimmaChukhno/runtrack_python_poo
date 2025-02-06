class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

class Professeur(Personne):
    def __init__(self, nom, age, matiere):
        super().__init__(nom, age)
        self.matiere = matiere

    def enseigner(self):
        print(f"Le cours de {self.matiere} va commencer.")


# Créer un élève
eleve = Eleve("Jean", 14)

# Redéfinir l'âge de l'élève à 15 ans
eleve.age = 15

# Faire dire bonjour à l'élève
eleve.bonjour()

# Faire dire "Je vais en cours"
eleve.allerEnCours()

# Créer un professeur
professeur = Professeur("M. Dupont", 40, "Mathématiques")

# Faire dire bonjour au professeur
professeur.bonjour()

# Commencer le cours
professeur.enseigner()