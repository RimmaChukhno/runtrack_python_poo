import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        paquet = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
        random.shuffle(paquet)
        return paquet

    def calculer_points(self, main):
        points = 0
        as_count = 0
        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                points += 10
            elif carte.valeur == 'As':
                points += 11
                as_count += 1
            else:
                points += int(carte.valeur)
        while points > 21 and as_count:
            points -= 10
            as_count -= 1
        return points

    def distribuer_carte(self):
        return self.paquet.pop()

    def jouer(self):
        joueur_main = [self.distribuer_carte(), self.distribuer_carte()]
        croupier_main = [self.distribuer_carte(), self.distribuer_carte()]

        print("Votre main:")
        for carte in joueur_main:
            print(carte)
        print(f"Total: {self.calculer_points(joueur_main)}")

        while True:
            choix = input("Voulez-vous prendre une carte ? (o/n): ").lower()
            if choix == 'o':
                joueur_main.append(self.distribuer_carte())
                print("Votre main:")
                for carte in joueur_main:
                    print(carte)
                total = self.calculer_points(joueur_main)
                print(f"Total: {total}")
                if total > 21:
                    print("Vous avez dépassé 21. Vous avez perdu!")
                    return
            else:
                break

        while self.calculer_points(croupier_main) < 17:
            croupier_main.append(self.distribuer_carte())

        print("\nMain du croupier:")
        for carte in croupier_main:
            print(carte)
        total_croupier = self.calculer_points(croupier_main)
        print(f"Total du croupier: {total_croupier}")

        total_joueur = self.calculer_points(joueur_main)

        if total_croupier > 21:
            print("Le croupier a dépassé 21. Vous avez gagné!")
        elif total_joueur > total_croupier:
            print("Vous avez gagné!")
        elif total_joueur < total_croupier:
            print("Le croupier a gagné.")
        else:
            print("Égalité.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()