class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"  # Par défaut, la tâche est "à faire"

    def __str__(self):
        return f"{self.titre} - {self.description} ({self.statut})"


class ListeDeTaches:
    def __init__(self):
        self.taches = []  # Liste pour stocker les tâches

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée.")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def afficherListe(self):
        if not self.taches:
            print("Aucune tâche dans la liste.")
        else:
            for tache in self.taches:
                print(tache)

    def filterListe(self, statut):
        filtered_taches = [tache for tache in self.taches if tache.statut == statut]
        if not filtered_taches:
            print(f"Aucune tâche avec le statut '{statut}'.")
        else:
            for tache in filtered_taches:
                print(tache)


# Test du code
if __name__ == "__main__":
    # Création de quelques tâches
    tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
    tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 3 et 4")
    tache3 = Tache("Nettoyer la maison", "Passer l'aspirateur et laver les sols")

    # Création de la liste de tâches
    liste_taches = ListeDeTaches()

    # Ajout des tâches à la liste
    liste_taches.ajouterTache(tache1)
    liste_taches.ajouterTache(tache2)
    liste_taches.ajouterTache(tache3)

    # Affichage de toutes les tâches
    print("\nListe de toutes les tâches :")
    liste_taches.afficherListe()

    # Marquer une tâche comme terminée
    liste_taches.marquerCommeFinie("Faire les courses")

    # Affichage des tâches à faire
    print("\nListe des tâches à faire :")
    liste_taches.filterListe("à faire")

    # Supprimer une tâche
    liste_taches.supprimerTache("Nettoyer la maison")

    # Affichage de toutes les tâches après suppression
    print("\nListe de toutes les tâches après suppression :")
    liste_taches.afficherListe()