class Robot:
    def __init__(self, name, x, y, movement_rate=3, attack_damage=1, attack_range=2, health=3):
        self.name = name
        self.x = x
        self.y = y
        self.hp = health
        self.max_hp = 11
        self.movement_rate = movement_rate
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.energy = movement_rate  # Energie entspricht MovementRate pro Zug

    def move(self, target_x, target_y, obstacles):
        if self.energy <= 0:
            print(f"{self.name} hat keine Energie für eine Bewegung.")
            return False

        distance = abs(self.x - target_x) + abs(self.y - target_y)
        if distance > self.energy or distance > self.movement_rate:
            print(f"{self.name} kann sich nicht so weit bewegen. Maximal {self.movement_rate} Felder erlaubt.")
            return False

        # Prüfen, ob Bewegung über Hindernisse geht
        if any((min(self.x, target_x) <= obs[0] <= max(self.x, target_x) and
                min(self.y, target_y) <= obs[1] <= max(self.y, target_y)) for obs in obstacles):
            print(f"Bewegung von {self.name} blockiert durch Hindernis.")
            return False

        # Bewegung durchführen
        self.energy -= distance
        self.x, self.y = target_x, target_y
        return True

    def attack(self, other_robot, obstacles):
        if self.energy <= 0:
            print(f"{self.name} hat keine Energie für einen Angriff.")
            return False

        if abs(self.x - other_robot.x) <= self.attack_range and abs(self.y - other_robot.y) <= self.attack_range:
            # Prüfen, ob Hindernis im Weg ist
            if not self.line_of_sight(other_robot, obstacles):
                print(f"Angriff von {self.name} blockiert durch ein Hindernis.")
                return False

            other_robot.hp -= self.attack_damage
            print(f"{self.name} greift {other_robot.name} an und fügt {self.attack_damage} Schaden zu!")
            self.energy = 0  # Angriff beendet Zug
            return True
        else:
            print(f"{self.name} ist nicht in Reichweite von {other_robot.name}.")
            return False

    def line_of_sight(self, other_robot, obstacles):
        # Prüft, ob Hindernisse im Weg sind
        for obs in obstacles:
            if (self.x <= obs[0] <= other_robot.x or self.y <= obs[1] <= other_robot.y):
                return False
        return True

    def reset_energy(self):
        self.energy = self.movement_rate  # Energie auffüllen
