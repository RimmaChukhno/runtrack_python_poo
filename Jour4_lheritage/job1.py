class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est {self.age} ans.")

    def bonjour(self):
        print("Bonjour")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J’ai {self.age} ans.")


class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer.")


# Instanciation des classes
personne = Personne()
eleve = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()

# Appel des méthodes
eleve.bonjour()
eleve.allerEnCours()

# Modification de l'âge de l'élève
eleve.modifierAge(15)
eleve.afficherAge()

# Instanciation de la classe Professeur
professeur = Professeur("Mathématiques")
professeur.enseigner()