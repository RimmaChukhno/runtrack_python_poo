class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"Part: {self.name}, Material: {self.material}"
    
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}
        self.history = []

    def add_part(self, part):
        """Ajoute une pièce au dictionnaire des pièces."""
        self.__parts[part.name] = part
        self.history.append(f"Added part: {part.name} with material {part.material}")

    def display_state(self):
        """Affiche l'état actuel du bateau (liste des pièces)."""
        if not self.__parts:
            print("The ship has no parts.")
        else:
            print(f"Ship: {self.name}")
            for part in self.__parts.values():
                print(f"  - {part}")

    def replace_part(self, part_name, new_part):
        """Remplace une pièce existante par une nouvelle."""
        if part_name in self.__parts:
            old_part = self.__parts[part_name]
            self.__parts[part_name] = new_part
            self.history.append(f"Replaced part: {old_part.name} with {new_part.name}")
        else:
            print(f"Part {part_name} not found.")

    def change_part(self, part_name, new_material):
        """Change directement le matériau d'une pièce existante."""
        if part_name in self.__parts:
            part = self.__parts[part_name]
            old_material = part.material
            part.change_material(new_material)
            self.history.append(f"Changed material of {part_name} from {old_material} to {new_material}")
        else:
            print(f"Part {part_name} not found.")

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"The maximum speed of {self.name} is {self.max_speed} knots.")

def menu():
    ship = RacingShip("Speedster", 40)
    
    while True:
        print("\n--- Ship Management Menu ---")
        print("1. Display ship state")
        print("2. Add a new part")
        print("3. Replace a part")
        print("4. Change part material")
        print("5. Display modification history")
        print("6. Display maximum speed")
        print("7. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            ship.display_state()
        
        elif choice == "2":
            name = input("Enter part name: ")
            material = input("Enter material: ")
            part = Part(name, material)
            ship.add_part(part)
        
        elif choice == "3":
            part_name = input("Enter the name of the part to replace: ")
            new_name = input("Enter new part name: ")
            new_material = input("Enter new material: ")
            new_part = Part(new_name, new_material)
            ship.replace_part(part_name, new_part)
        
        elif choice == "4":
            part_name = input("Enter the name of the part to change material: ")
            new_material = input("Enter new material: ")
            ship.change_part(part_name, new_material)
        
        elif choice == "5":
            print("\n--- Modification History ---")
            for record in ship.history:
                print(record)
        
        elif choice == "6":
            ship.display_speed()
        
        elif choice == "7":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
