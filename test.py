class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.hp = 5
        self.energy = 3
        self.shield = 2
        self.attack_power = 1
        self.range = 2
        self.damage_zone = 1
        self.accuracy = 1
        self.movement = 1
        self.shield_active = False

    def move(self, direction):
        if direction == 'up' and self.y > 0:
            self.y -= self.movement
        elif direction == 'down' and self.y < 9:
            self.y += self.movement
        elif direction == 'left' and self.x > 0:
            self.x -= self.movement
        elif direction == 'right' and self.x < 14:
            self.x += self.movement

    def attack(self, other_robot):
        if abs(self.x - other_robot.x) <= self.range and abs(self.y - other_robot.y) <= self.range:
            if other_robot.shield_active:
                print(f"{other_robot.name} hat den Angriff mit dem Schild blockiert!")
                other_robot.shield_active = False  # Deactivate the shield after blocking an attack
            else:
                other_robot.hp -= self.attack_power
            return True
        return False

    def healing(self):
        if self.energy > 0:
            self.hp += 1
            self.energy -= 1

    def shielding(self):
        if self.shield > 0 and not self.shield_active:
            self.shield_active = True
            self.shield -= 1
            print(f"{self.name} hat das Schild aktiviert!")

def draw_field(robots, width=15, height=10):
    field = [['[ ]' for _ in range(width)] for _ in range(height)]

    for robot in robots:
        field[robot.y][robot.x] = f'[{robot.name[0]}]'

    for row in field:
        print(''.join(row))

robot1 = Robot("Robo1", 0, 0)
robot2 = Robot("Robo2", 1, 0)

def control_robots(robot1, robot2):
    while robot1.hp > 0 and robot2.hp > 0:
        draw_field([robot1, robot2])

        # Robot 1's turn
        move1 = input(f"{robot1.name}, gib eine Richtung ein (up, down, left, right) oder 'attack', 'heal', 'shield': ")
        if move1 in ['up', 'down', 'left', 'right']:
            robot1.move(move1)
        elif move1 == 'attack':
            if robot1.attack(robot2):
                print(f"{robot1.name} hat {robot2.name} getroffen!")
            else:
                print(f"{robot1.name} hat daneben geschossen!")
        elif move1 == 'shield':
            robot1.shielding()
        elif move1 == 'heal':
            if robot1.energy > 0:
                if robot1.hp < 5:
                    robot1.healing()
                    print(f"{robot1.name} hat sich geheilt!")
                else:
                    print(f"{robot1.name} hat zu viel Leben.")
            else:
                print("Du hast keine Energie mehr")

        # Robot 2's turn
        draw_field([robot1, robot2])
        move2 = input(f"{robot2.name}, gib eine Richtung ein (up, down, left, right) oder 'attack', 'heal', 'shield': ")
        if move2 in ['up', 'down', 'left', 'right']:
            robot2.move(move2)
        elif move2 == 'attack':
            if robot2.attack(robot1):
                print(f"{robot2.name} hat {robot1.name} getroffen!")
            else:
                print(f"{robot2.name} hat daneben geschossen!")
        elif move2 == 'shield':
            robot2.shielding()
        elif move2 == 'heal':
            if robot2.energy > 0:
                if robot2.hp < 5:
                    robot2.healing()
                    print(f"{robot2.name} hat sich geheilt!")
                else:
                    print(f"{robot2.name} hat zu viel Leben.")
            else:
                print("Du hast keine Energie mehr")

control_robots(robot1, robot2)
