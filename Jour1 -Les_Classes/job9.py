
class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}€, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC()}€"

    def ModifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def ModifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def ObtenirNom(self):
        return self.nom

    def ObtenirPrixHT(self):
        return self.prixHT

    def ObtenirTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Laptop", 800, 20)
produit2 = Produit("Smartphone", 400, 20)
produit3 = Produit("Tablette", 300, 10)

# Affichage des informations initiales des produits
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Modification du nom et du prix des produits
produit1.ModifierNom("Laptop Gaming")
produit1.ModifierPrixHT(1000)

produit2.ModifierNom("Smartphone Pro")
produit2.ModifierPrixHT(500)

produit3.ModifierNom("Tablette Lite")
produit3.ModifierPrixHT(250)

# Affichage des nouvelles informations des produits
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())