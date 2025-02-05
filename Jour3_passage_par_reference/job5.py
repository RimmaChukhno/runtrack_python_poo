#Créez un jeu de combat en utilisant la POO. 
import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        """Inflige des dégâts à l'adversaire."""
        degats = random.randint(5, 15)  # Dégâts aléatoires entre 5 et 15 points
        adversaire.vie -= degats
        adversaire.vie = max(0, adversaire.vie)  # La vie ne peut pas descendre en dessous de 0
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts. Il reste {adversaire.vie} points de vie à {adversaire.nom}.")

    def est_vivant(self):
        """Retourne True si le personnage est encore en vie."""
        return self.vie > 0


class Jeu:
    def __init__(self):
        self.niveau = None

    def choisir_niveau(self):
        """Demande au joueur de choisir un niveau de difficulté."""
        while True:
            try:
                print("Choisissez un niveau de difficulté :")
                print("1. Facile (100 PV chacun)")
                print("2. Moyen (75 PV chacun)")
                print("3. Difficile (50 PV chacun)")
                choix = int(input("Entrez le numéro du niveau : "))
                if choix in [1, 2, 3]:
                    self.niveau = choix
                    break
                else:
                    print("Veuillez entrer un numéro valide (1, 2 ou 3).")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def lancer_jeu(self):
        """Lance la partie avec les paramètres définis par le niveau."""
        points_de_vie = {1: 100, 2: 75, 3: 50}
        vie_initiale = points_de_vie[self.niveau]

        joueur = Personnage("Joueur", vie_initiale)
        ennemi = Personnage("Ennemi", vie_initiale)

        print(f"\nLa partie commence ! Chaque personnage a {vie_initiale} points de vie.\n")

        # Boucle principale du jeu
        while joueur.est_vivant() and ennemi.est_vivant():
            # Tour du joueur
            joueur.attaquer(ennemi)
            if not ennemi.est_vivant():
                print("\nVous avez gagné ! L'ennemi est vaincu.")
                break

            # Tour de l'ennemi
            ennemi.attaquer(joueur)
            if not joueur.est_vivant():
                print("\nVous avez perdu... L'ennemi vous a vaincu.")
                break

        print("Fin de la partie.")

# Exemple d'utilisation
if __name__ == "__main__":
    jeu = Jeu()
    jeu.choisir_niveau()
    jeu.lancer_jeu()
