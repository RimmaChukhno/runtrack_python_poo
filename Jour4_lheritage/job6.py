# Classe de base Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Model = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix} €")

    def demarrer(self):
        print("Attention, je roule")


# Classe Voiture qui hérite de Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4  # Attribut spécifique à la Voiture

    def informationsVehicule(self):
        super().informationsVehicule()  # Appel de la méthode de la classe parente
        print(f"Nombre de portes = {self.portes}")

    def demarrer(self):
        print(" La voiture démarre.")


# Classe Moto qui hérite de Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2  # Attribut spécifique à la Moto

    def informationsVehicule(self):
        super().informationsVehicule()  # Appel de la méthode de la classe parente
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self):
        print(" La moto démarre.")


# Instanciation d'une Voiture
ma_voiture = Voiture(marque="Mercedes", modele="Classe A", annee = 2020, prix = 18500)
ma_voiture.informationsVehicule()  # Affiche les informations de la voiture
ma_voiture.demarrer()  # Démarre la voiture

# Instanciation d'une Moto
ma_moto = Moto(marque="Yamaha", modele="1200 Vmax", annee = 1987, prix = 4500)
ma_moto.informationsVehicule()  # Affiche les informations de la moto
ma_moto.demarrer()  # Démarre la moto