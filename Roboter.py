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
        if (target_x, target_y) in obstacles:
            print(f"{self.name}: Bewegung blockiert durch ein Hindernis.")
            return
        if abs(target_x - self.x) + abs(target_y - self.y) > self.energy:
            print(f"{self.name}: Ziel zu weit entfernt. Nicht genug Energie!")
            return
        if 0 <= target_x < 15 and 0 <= target_y < 10:
            self.energy -= abs(target_x - self.x) + abs(target_y - self.y)
            self.x = target_x
            self.y = target_y
            print(f"{self.name} bewegt sich zu ({self.x}, {self.y}).")
        else:
            print(f"{self.name}: Ziel außerhalb des Spielfelds.")

    def attack(self, target, obstacles):
        distance = abs(self.x - target.x) + abs(self.y - target.y)
        if distance > self.attack_range:
            print(f"{self.name}: Ziel außer Reichweite.")
            return
        if (target.x, target.y) in obstacles:
            print(f"{self.name}: Ziel durch ein Hindernis blockiert.")
            return
        target.hp -= self.attack_damage
        print(f"{self.name} greift {target.name} an und verursacht {self.attack_damage} Schaden!")
        if target.hp <= 0:
            print(f"{target.name} wurde besiegt!")

    def apply_item_effect(self):
        print(f"{self.name} hat ein Item aufgesammelt!")
        self.attack_damage += 1
        self.energy += 2
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name}: 1 HP geheilt!")
        print(f"{self.name}: AttackDamage: {self.attack_damage}, Energie: {self.energy}, HP: {self.hp}")
