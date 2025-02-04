class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.__disponible = True  # Attribut privé initialisé à True par défaut

    def vérification(self):
        # Vérifie si le livre est disponible
        return self.__disponible

    def emprunter(self):
        # Emprunte le livre s'il est disponible
        if self.vérification():  # Vérifie la disponibilité sans accéder directement à l'attribut
            self.__disponible = False
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        # Rend le livre s'il a été emprunté
        if not self.vérification():  # Vérifie si le livre a été emprunté sans accéder directement à l'attribut
            self.__disponible = True
            print(f"Le livre '{self.titre}' a été rendu.")
        else:
            print(f"Le livre '{self.titre}' n'a pas besoin d'être rendu, il est déjà disponible.")
