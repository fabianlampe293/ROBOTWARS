class Robot:
    def __init__(self, name, x, y, movement_rate, attack_damage, attack_range, hp):
        self.name = name
        self.x = x
        self.y = y
        self.movement_rate = movement_rate
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.hp = hp
        self.max_hp = hp
        self.energy = movement_rate

    def reset_energy(self):
        self.energy = self.movement_rate

    def move(self, target_x, target_y, obstacles):
        distance = abs(target_x - self.x) + abs(target_y - self.y)
        if distance > self.energy:
            print("Nicht genug Energie, um sich zu bewegen!")
            return False  # Bewegung fehlgeschlagen

        # Prüfen, ob Ziel durch ein Hindernis blockiert ist
        if (target_x, target_y) in obstacles:
            print("Das Ziel ist blockiert!")
            return False  # Bewegung fehlgeschlagen

        # Bewegung durchführen
        self.x = target_x
        self.y = target_y
        self.energy -= distance
        return True  # Bewegung erfolgreich
