# class Livre:
#     def __init__(self, titre, auteur, nombre_pages):
#         self.__titre = titre
#         self.__auteur = auteur
#         self.set_nombre_pages(nombre_pages)  # Utilisation du mutateur pour valider le nombre de pages

#     # Accesseurs (getters)
#     def get_titre(self):
#         return self.__titre

#     def get_auteur(self):
#         return self.__auteur

#     def get_nombre_pages(self):
#         return self.__nombre_pages

#     # Mutateurs (setters)
#     def set_titre(self, titre):
#         self.__titre = titre

#     def set_auteur(self, auteur):
#         self.__auteur = auteur

#     def set_nombre_pages(self, nombre_pages):
#         if isinstance(nombre_pages, int) and nombre_pages > 0:
#             self.__nombre_pages = nombre_pages
#         else:
#             print("Erreur : Le nombre de pages doit être un entier positif.")

#     # Méthode pour afficher les informations du livre
#     def afficher_infos(self):
#         print(f"Titre: {self.__titre}")
#         print(f"Auteur: {self.__auteur}")
#         print(f"Nombre de pages: {self.__nombre_pages}")

# # Exemple d'utilisation
# livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
# livre.afficher_infos()

# # # Modification des attributs
# # livre.set_titre("1984")
# # livre.set_auteur("George Orwell")
# # livre.set_nombre_pages(328)
# # livre.afficher_infos()

# # Tentative de modification avec un nombre de pages invalide
# livre.set_nombre_pages(-100)  # Affiche un message d'erreur
# livre.set_nombre_pages("cent")  # Affiche un message d'erreur
# livre.afficher_infos()  # Les informations restent inchangées


class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = 0
        self.set_nombre_pages(nombre_pages)

    # Accesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : le nombre de pages doit être un nombre entier positif.")

    # Méthode pour afficher les détails du livre
    def afficher_details(self):
        print(f"Titre : {self.__titre}\nAuteur : {self.__auteur}\nNombre de pages : {self.__nombre_pages}")

# Exemple d'utilisation :
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
livre1.afficher_details()

livre1.set_nombre_pages(-50)  # Affiche un message d'erreur
livre1.set_nombre_pages(120)
livre1.afficher_details()
