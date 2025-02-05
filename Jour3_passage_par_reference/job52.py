# jeu de combat en utilisant la Programmation Orientée Objet (POO)
import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)  # Dégâts aléatoires entre 5 et 15
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts!")
        print(f"{adversaire.nom} a maintenant {adversaire.vie} points de vie.\n")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self): #selectLevel
        print("Choisissez le niveau de difficulté:")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        choix = input("Entrez le numéro du niveau (1, 2 ou 3): ")
        while choix not in ['1', '2', '3']:
            choix = input("Choix invalide. Entrez 1, 2 ou 3: ")
        self.niveau = int(choix)

    def lancerJeu(self):
        if self.niveau is None:
            print("Veuillez d'abord choisir un niveau de difficulté.")
            return

        # Définir les points de vie en fonction du niveau
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 80
        elif self.niveau == 3:
            vie_joueur = 50
            vie_ennemi = 100

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print(f"\nLe jeu commence! Niveau de difficulté: {self.niveau}")
        print(f"{joueur.nom} a {joueur.vie} points de vie.")
        print(f"{ennemi.nom} a {ennemi.vie} points de vie.\n")

        while joueur.est_vivant() and ennemi.est_vivant():
            # Tour du joueur
            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)

            # Vérifier si l'ennemi est mort
            if not ennemi.est_vivant():
                print(f"{ennemi.nom} est mort! {joueur.nom} a gagné!")
                break

            # Tour de l'ennemi
            print(f"C'est au tour de {ennemi.nom} d'attaquer!")
            ennemi.attaquer(joueur)

            # Vérifier si le joueur est mort
            if not joueur.est_vivant():
                print(f"{joueur.nom} est mort! {ennemi.nom} a gagné!")
                break

# Exécution du jeu
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()