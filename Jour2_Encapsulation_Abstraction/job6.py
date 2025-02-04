class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats (nom: {prix, quantité})
        self.__statut = "en cours"  # Statut initial de la commande

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix, quantite=1):
        if self.__statut == "en cours":
            if nom_plat in self.__plats_commandes:
                self.__plats_commandes[nom_plat]["quantite"] += quantite
            else:
                self.__plats_commandes[nom_plat] = {"prix": prix, "quantite": quantite}
        else:
            print("La commande n'est plus modifiable.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        self.__statut = "annulée"
        self.__plats_commandes.clear()
        print("La commande a été annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = 0
        for plat, details in self.__plats_commandes.items():
            total += details["prix"] * details["quantite"]
        return total

    # Méthode pour afficher la commande et le total à payer
    def afficher_commande(self):
        if self.__statut == "annulée":
            print("La commande est annulée.")
            return

        print(f"Commande n°{self.__numero_commande} - Statut: {self.__statut}")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat} x{details['quantite']} - {details['prix']} € pièce")
        total = self.__calculer_total()
        print(f"Total à payer: {total} € (TVA incluse: {self.calculer_tva(total)} €)")

    # Méthode pour calculer la TVA (20%)
    def calculer_tva(self, montant):
        return round(montant * 0.20, 2)

    # Getter pour le statut de la commande
    def get_statut(self):
        return self.__statut

    # Setter pour le statut de la commande
    def set_statut(self, nouveau_statut):
        if nouveau_statut in ["en cours", "terminée", "annulée"]:
            self.__statut = nouveau_statut
        else:
            print("Statut invalide.")


# Exemple d'utilisation de la classe Commande
if __name__ == "__main__":
    # Création d'une commande
    commande = Commande(1)

    # Ajout de plats à la commande
    commande.ajouter_plat("Pizza", 10.5, 2)
    commande.ajouter_plat("Salade César", 8.0)
    commande.ajouter_plat("Tiramisu", 6.0)

    # Affichage de la commande
    commande.afficher_commande()

    # Annulation de la commande
    commande.annuler_commande()

    # Tentative d'ajout de plat après annulation
    commande.ajouter_plat("Pâtes Carbonara", 12.0)

    # Changement de statut de la commande
    commande.set_statut("terminée")
    print(f"Statut de la commande: {commande.get_statut()}")