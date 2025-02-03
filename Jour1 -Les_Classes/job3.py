class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le resultat de l'addition est : {resultat}")

# Exemple d'utilisation
op = Operation(5, 10)
op.addition()  # Affichera : Le résultat de l'addition est : 15
