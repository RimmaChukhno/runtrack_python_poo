class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte Bancaire : {self.__numero_compte}")
        print(f"Titulaire: {self.__prenom} {self.__nom}")
        print(f"Solde: {self.__solde} €")
        print(f"Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde} €")

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Le montant du versement doit être positif.")

    def retrait(self, montant):
        if montant > 0:
            if self.__solde - montant >= 0 or self.__decouvert:
                self.__solde -= montant
                print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
            else:
                print("Opération impossible : solde insuffisant.")
        else:
            print("Le montant du retrait doit être positif.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios appliqués: {agios} €. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if montant > 0:
            if self.__solde - montant >= 0 or self.__decouvert:
                self.__solde -= montant
                compte_destinataire.versement(montant)
                print(f"Virement de {montant} € effectué vers le compte n°{compte_destinataire.__numero_compte}.")
            else:
                print("Opération impossible : solde insuffisant.")
        else:
            print("Le montant du virement doit être positif.")


# Création de deux comptes bancaires
compte1 = CompteBancaire(123456, "Dupont", "Jean", 1000)
compte2 = CompteBancaire(654321, "Martin", "Alice", -200, decouvert=True)

# Affichage des détails des comptes
compte1.afficher()
compte2.afficher()

# Opérations sur le compte 1
compte1.versement(500)
compte1.retrait(200)
compte1.afficherSolde()

# Opérations sur le compte 2
compte2.agios(0.05)  # Appliquer des agios de 5%
compte2.afficherSolde()

# Virement du compte 1 vers le compte 2
compte1.virement(compte2, 300)

# Affichage des soldes après virement
compte1.afficherSolde()
compte2.afficherSolde()