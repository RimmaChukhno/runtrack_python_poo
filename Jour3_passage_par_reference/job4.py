# class Joueur:
#     def __init__(self, nom, numéro, position):
#         self.nom = nom
#         self.numéro = numéro
#         self.position = position
#         self.nombre_buts_marqués = 0
#         self.passes_décisives_effectuées = 0
#         self.cartons_jaunes_reçus = 0
#         self.cartons_rouges_reçus = 0

#     def marquerUnBut(self):
#         self.nombre_buts_marqués += 1

#     def effectuerUnePasseDecisive(self):
#         self.passes_décisives_effectuées += 1

#     def recevoirUnCartonJaune(self):
#         self.cartons_jaunes_reçus += 1

#     def recevoirUnCartonRouge(self):
#         self.cartons_rouges_reçus += 1

#     def afficherStatistiques(self):
#         print(f"Statistiques de {self.nom} (Numéro {self.numéro}, {self.position}):")
#         print(f"  Buts marqués: {self.nombre_buts_marqués}")
#         print(f"  Passes décisives: {self.passes_décisives_effectuées}")
#         print(f"  Cartons jaunes: {self.cartons_jaunes_reçus}")
#         print(f"  Cartons rouges: {self.cartons_rouges_reçus}")
#         print()

# class Equipe:
#     def __init__(self, nom):
#         self.nom = nom
#         self.joueurs = []

#     def ajouterJoueur(self, joueur):
#         self.joueurs.append(joueur)

#     def AfficherStatistiquesJoueurs(self):
#         print(f"Statistiques des joueurs de l'équipe {self.nom}:")
#         for joueur in self.joueurs:
#             joueur.afficherStatistiques()

#     def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
#         for joueur in self.joueurs:
#             if joueur.nom == nom_joueur:
#                 if action == "but":
#                     joueur.marquerUnBut()
#                 elif action == "passe":
#                     joueur.effectuerUnePasseDecisive()
#                 elif action == "jaune":
#                     joueur.recevoirUnCartonJaune()
#                 elif action == "rouge":
#                     joueur.recevoirUnCartonRouge()
#                 break

# # Création des joueurs
# joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
# joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
# joueur3 = Joueur("Neymar Jr", 11, "Attaquant")
# joueur4 = Joueur("Sergio Ramos", 4, "Défenseur")
# joueur5 = Joueur("Manuel Neuer", 1, "Gardien")

# # Création des équipes
# equipe1 = Equipe("Paris Saint-Germain")
# equipe2 = Equipe("Real Madrid")

# # Ajout des joueurs aux équipes
# equipe1.ajouterJoueur(joueur1)
# equipe1.ajouterJoueur(joueur3)
# equipe1.ajouterJoueur(joueur5)

# equipe2.ajouterJoueur(joueur2)
# equipe2.ajouterJoueur(joueur4)

# # Affichage des statistiques initiales
# equipe1.AfficherStatistiquesJoueurs()
# equipe2.AfficherStatistiquesJoueurs()

# # Simulation d'un match
# equipe1.mettreAJourStatistiquesJoueur("Lionel Messi", "but")
# equipe1.mettreAJourStatistiquesJoueur("Neymar Jr", "passe")
# equipe2.mettreAJourStatistiquesJoueur("Cristiano Ronaldo", "but")
# equipe2.mettreAJourStatistiquesJoueur("Sergio Ramos", "jaune")
# equipe1.mettreAJourStatistiquesJoueur("Manuel Neuer", "rouge")

# # Affichage des statistiques après le match
# print("\nStatistiques après le match:\n")
# equipe1.AfficherStatistiquesJoueurs()
# equipe2.AfficherStatistiquesJoueurs()

class Joueur:
    def __init__(self, nom, numero, position, buts=0, passes_decisives=0, jaunes=0, rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = jaunes
        self.cartons_rouges = rouges

    def marquerUnBut(self):
        self.buts += 1
        print(f"{self.nom} a marqué un but !")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive !")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune.")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge.")

    def afficherStatistiques(self):
        print(f"--- Statistiques de {self.nom} ---")
        print(f"Numéro: {self.numero}, Position: {self.position}")
        print(f"Buts: {self.buts}, Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        print(f"{joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"--- Statistiques des joueurs de l'équipe {self.nom} ---")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges
                print(f"Statistiques de {joueur.nom} mises à jour.")
                break
        else:
            print(f"Joueur {nom_joueur} non trouvé dans l'équipe {self.nom}.")


# Création des joueurs
joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar Jr", 11, "Milieu offensif")

# Création de l'équipe
equipe = Equipe("Dream Team")

# Ajout des joueurs à l'équipe
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

# Affichage des statistiques initiales
equipe.afficherStatistiquesJoueurs()

# Simulation d'un match
print("\n--- Début du match ---\n")
joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()
joueur1.marquerUnBut()
joueur3.recevoirUnCartonRouge()

# Mise à jour et affichage des statistiques après le match
print("\n--- Statistiques après le match ---\n")
equipe.afficherStatistiquesJoueurs()
