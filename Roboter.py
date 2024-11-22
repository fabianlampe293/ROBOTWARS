import random
class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.hp = 3
        self.potions = 2
        self.shield = 1
        self.attack_power = 1
        self.shield_active = False
        self.energy = 3
        self.range = 2
        self.accuracy = 1
        self.damage_zone = 2

    def move(self, direction):
        if direction == 'up' and self.y > 0:
            self.y -= 1
        elif direction == 'down' and self.y < 9:
            self.y += 1
        elif direction == 'left' and self.x > 0:
            self.x -= 1
        elif direction == 'right' and self.x < 14:
            self.x += 1

    def attack(self, other_robot):
        if (abs(self.x - other_robot.x) <= self.damage_zone and abs(self.y - other_robot.y) <= self.damage_zone):
            if other_robot.shield_active:
                print(f"{other_robot.name} hat den Angriff mit dem Schild blockiert!")
                other_robot.shield_active = False
            else:
                hit_chance = self.accuracy / (self.accuracy + other_robot.accuracy)
                if random.random() < hit_chance:
                    other_robot.hp -= self.attack_power
                    print(f"{self.name} hat {other_robot.name} getroffen!")
                else:
                    print(f"{self.name} hat daneben geschossen!")
            return True
        return False

    def healing(self):
        if self.potions > 0:
            self.hp += 1
            self.potions -= 1

    def shielding(self):
        if self.shield > 0 and not self.shield_active:
            self.shield_active = True
            self.shield -= 1
            print(f"{self.name} hat das Schild aktiviert!")