class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def ajouter_habitant(self):
        self.__population += 1

    def get_population(self):
        return self.__population

    def get_nom(self):
        return self.__nom


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()  # Ajoute la personne à la population de la ville


# Création des villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage des populations initiales
print(f"Population de la ville de {paris.get_nom()} : {paris.get_population()} habitants")
print(f"Population de la ville de {marseille.get_nom()} : {marseille.get_population()} habitants")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage des populations après l'arrivée des nouvelles personnes
print(f"Mise a jour de la population de la ville de {paris.get_nom()}  {paris.get_population()} habitants")
print(f"Mise a jour de la population de la ville de {marseille.get_nom()}  {marseille.get_population()} habitants")
