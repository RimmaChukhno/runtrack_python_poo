class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()  # Initialisation du niveau

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            self.__level = self.__student_eval()  # Mise à jour du niveau après ajout de crédits
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Informations de l'étudiant :")
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__numero_etudiant}")
        print(f"Niveau = {self.__level}")
        print(f"Le nombre de crédits est de  {self.__credits} points")

# Instanciation de l'objet Student représentant John Doe
john_doe = Student( "John", "Doe", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(30)
john_doe.add_credits(25)
john_doe.add_credits(35)

# Affichage des informations de l'étudiant
john_doe.student_info()