class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir > 5

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est trop bas pour démarrer.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Toyota", "Corolla", 2020, 15000)

print(f"Marque: {ma_voiture.get_marque()}")
print(f"Modèle: {ma_voiture.get_modele()}")
print(f"Année: {ma_voiture.get_annee()}")
print(f"Kilométrage: {ma_voiture.get_kilometrage()}")
print(f"Réservoir: {ma_voiture.get_reservoir()}")

ma_voiture.demarrer()  # Dès que le réservoir est plein, la machine démarre.
ma_voiture.arreter()   # La voiture s'arrête