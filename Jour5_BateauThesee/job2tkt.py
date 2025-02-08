import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk  # Для работы с изображениями
import random
import os

# Classe Part
class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"

# Classe Ship
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mat": Part("Mat", "Bois"),
            "Coque": Part("Coque", "Bois"),
            "Voile": Part("Voile", "Bois"),
            "Rames": Part("Rames", "Bois"),
            "Porte": Part("Porte", "Bois"),
            "Fenêtre": Part("Fenêtre", "Bois"),
            "Pont": Part("Pont", "Bois"),
            "Helice": Part("Helice", "Bois"),
            "Canot": Part("Canot", "Bois"),
            "Cabine": Part("Cabine", "Bois")
        }
        self.history = []  # Инициализация истории

    # Функция для проверки выигрыша
    def check_win(self):
        # Проверим, если все части заменены на металл или стекло
        all_replaced = all(part.material in ["Acier", "Verre"] for part in self.__parts.values())
        if all_replaced:
            messagebox.showinfo("Félicitations", "Vous avez gagné ! Votre navire est entièrement modernisé !")
            self.reset_game()

    # Функция для сброса игры
    def reset_game(self):
        # Возвращаем все части обратно на древесину
        for part in self.__parts.values():
            part.change_material("Bois")
        self.history.clear()  # Очищаем историю
        self.update_state()

    def display_state(self):
        state = f"{self.name}:\n"
        for part_name, part in self.__parts.items():
            state += str(part) + "\n"
        return state

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            self.history.append(f"Pièce remplacée: {part_name} -> {new_part}")
        else:
            messagebox.showerror("Erreur", f"Pièce {part_name} non trouvée.")

    # Changer le matériau d'une pièce
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            # Записываем изменение в историю
            with open('history.txt', 'a') as mat_hist:
                mat_hist.write(f"Modification materiel : {part_name} => {new_material}\n")
            
            # Изменяем материал части
            self.__parts[part_name].change_material(new_material)
            
            # Проверяем, не выиграл ли игрок
            self.check_win()
        else:
            print(f"Erreur: {part_name} n'existe pas dans le bateau.")

    def get_parts(self):
        return self.__parts

# Classe RacingShip
class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        return f"Vitesse maximale: {self.max_speed} nœuds"

# Interface graphique avec Tkinter
class ShipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Le bateau de Thésée")
        self.ship = RacingShip("Flash", 50)

        # Charger l'image du bateau
        self.load_ship_image()

        self.create_widgets()

    def load_ship_image(self):
        # Chemin vers l'image (assurez-vous que le fichier existe)
        image_path = "ship.png"  # Remplacez par le chemin de votre image
        if not os.path.exists(image_path):
            messagebox.showerror("Erreur", f"Image {image_path} introuvable.")
            return

        # Ouvrir l'image avec PIL et la redimensionner
        self.ship_image = Image.open(image_path)
        self.ship_image = self.ship_image.resize((200, 100), Image.Resampling.LANCZOS)  # Redimensionner l'image
        self.ship_photo = ImageTk.PhotoImage(self.ship_image)

    def create_widgets(self):
        # Frame principale
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(padx=20, pady=20)

        # Ajouter l'image du bateau en haut
        self.image_label = tk.Label(self.main_frame, image=self.ship_photo, bg="#f0f0f0")
        self.image_label.pack(pady=10)

        # Titre
        self.title_label = tk.Label(self.main_frame, text="Le bateau de Thésée", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Заголовок "État du bateau" с подчеркиванием и состоянием корабля
        self.state_title_label = tk.Label(
            self.main_frame, 
            text=f"État du bateau\n{self.ship.display_state()}",  # Объединяем заголовок и состояние
            justify=tk.LEFT, 
            bg="#f0f0f0", 
            font=("Helvetica", 12, "underline")  # Только заголовок подчеркнут
        )
        self.state_title_label.pack(pady=5)

        # Boutons pour interagir avec le bateau
        button_style = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "white", "borderwidth": 0, "padx": 10, "pady": 5}

        self.replace_button = tk.Button(self.main_frame, text="Remplacer une pièce", command=self.replace_part, **button_style)
        self.replace_button.pack(pady=5)

        self.change_material_button = tk.Button(self.main_frame, text="Changer le matériau d'une pièce", command=self.change_material, **button_style)
        self.change_material_button.pack(pady=5)

        self.display_speed_button = tk.Button(self.main_frame, text="Afficher la vitesse maximale", command=self.display_speed, **button_style)
        self.display_speed_button.pack(pady=5)

        self.history_button = tk.Button(self.main_frame, text="Afficher l'historique", command=self.display_history, **button_style)
        self.history_button.pack(pady=5)

        self.random_event_button = tk.Button(self.main_frame, text="Simuler un événement aléatoire", command=self.random_event, **button_style)
        self.random_event_button.pack(pady=5)

    def replace_part(self):
        part_name = simpledialog.askstring("Remplacer une pièce", "Entrez le nom de la pièce à remplacer:")
        if part_name:
            new_part_name = simpledialog.askstring("Remplacer une pièce", "Entrez le nom de la nouvelle pièce:")
            new_part_material = simpledialog.askstring("Remplacer une pièce", "Entrez le matériau de la nouvelle pièce:")
            if new_part_name and new_part_material:
                new_part = Part(new_part_name, new_part_material)
                self.ship.replace_part(part_name, new_part)
                self.update_state()

    def change_material(self):
        part_name = simpledialog.askstring("Changer le matériau", "Entrez le nom de la pièce:")
        if part_name:
            new_material = simpledialog.askstring("Changer le matériau", "Entrez le nouveau matériau:")
            if new_material:
                self.ship.change_part(part_name, new_material)
                self.update_state()

    def display_speed(self):
        messagebox.showinfo("Vitesse maximale", self.ship.display_speed())

    def display_history(self):
        history = "\n".join(self.ship.history) if self.ship.history else "Aucune modification enregistrée."
        messagebox.showinfo("Historique des modifications", history)

    def random_event(self):
        events = [
            "Une tempête a endommagé le mât!",
            "La coque a été usée par les vagues.",
            "La voile a été déchirée par le vent."
        ]
        event = random.choice(events)
        part_name = event.split()[2]  # Extrait le nom de la pièce concernée
        new_material = "Endommagé"
        self.ship.change_part(part_name, new_material)
        self.ship.history.append(f"Événement aléatoire: {event}")
        self.update_state()
        messagebox.showinfo("Événement aléatoire", event)

    # def update_state(self):
    #     self.state_title_label.config(text=self.ship.display_state())

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = ShipApp(root)
    root.mainloop()