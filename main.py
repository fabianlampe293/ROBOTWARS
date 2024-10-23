'''from Roboter import Robot
class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.hp = 3
        self.potions = 2

# ASCII Art and Welcome Messages
a =
__        __   _                            _          
\\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___    
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\   
  \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |  
 __\\_/\\_/_\\___|_|\\___\\___/|_| |_| |_|\\___| _\\__\\___/_  
|  _ \\ / _ \\| __ ) / _ \\  \\ \\      / / \\  |  _ \\/ ___| 
| |_) | | | |  _ \\| | | |  \\ \\ /\\ / / _ \\ | |_) \\___ \\ 
|  _ <| |_| | |_) | |_| |   \\ V  V / ___ \\|  _ < ___) |
|_| \\_\\\\___/|____/ \\___/     \\_/\\_/_/   \\_\\_| \\_\\____/ 


b =
   _____             _____
  |_____|___________|_____|
  |_____| / _____ \\ |_____|
  |_____|/ /\\___/\\ \\|_____|
 /|====|__/_/___\\_\\__|====|\\
 ||====|  _/_\\_/_\\_  |====||
 \\|====| | \\ ... / | |====|/
       |__\\ `---' /__|
        |==\\_____/==|
        |===|===|===|
        |===|+-+|===|
        >|||<   >|||<
        |---|   |---|
        || ||   || ||
        || ||   || ||
        >= =<   >= =<
        |===|   |===|
        >---//   \\---<
        ||#|     |#||
        ||-|\\   /|-||
        ||+||   ||+||
        ||-|/   \\|-||
        ||_|\\   /|_||   
     ___|/-\\/   \\/-\\|___
    //________\\ /________\\


print(a)
print(b)

robo_Name1 = input("Gib deinen Robotornamen ein: ")
robo_Name2 = input("Gib deinen Robotornamen ein: ")
print("Herzlich Willkommen: ", robo_Name1, robo_Name2)

print("Möchtest du das Spiel starten?")
Antwort = input("Ja oder Nein: ")
if Antwort.lower() == "ja":
    print("Das Spiel beginnt:")
else:
    print(a, b)
'''
#from Grafiken import ArtDisplay

class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.hp = 3
        self.potions = 2

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
        if (self.x == other_robot.x and abs(self.y - other_robot.y) == 1) or \
           (self.y == other_robot.y and abs(self.x - other_robot.x) == 1):
            other_robot.hp -= 1
            return True
        return False

    def healing(self):
        if self.potions > 0:
            self.hp += 1
            self.potions -= 1

def draw_field(robots, width=15, height=10):
    field = [['.' for _ in range(width)] for _ in range(height)]

    for robot in robots:
        field[robot.y][robot.x] = robot.name[0]

    for row in field:
        print(' '.join(row))

robot1 = Robot("Player1", 0, 0)
robot2 = Robot("Player2", 1, 0)

def control_robots(robot1, robot2):
    while robot1.hp > 0 and robot2.hp > 0:
        draw_field([robot1, robot2])

        move1 = input(f"{robot1.name}, gib eine Richtung ein (up, down, left, right) oder 'attack' oder 'heal': ")
        if move1 in ['up', 'down', 'left', 'right']:
            robot1.move(move1)
        elif move1 == 'attack':
            if robot1.attack(robot2):
                print(f"{robot1.name} hat {robot2.name} getroffen!")
            else:
                print(f"{robot1.name} hat daneben geschossen!")
        if move1 == 'heal':
            if robot1.potions > 0:
                if robot1.hp < 3:
                    robot1.healing()
                    print(f"{robot1.name} hat sich geheilt!")
                else:
                     print(f"{robot1.name} hat zu viel Leben.")
            else:
                if robot1.potions == 0:
                    print("Du hast keine Tränke mehr")
                    move1 = input(
                        f"{robot1.name}, gib eine Richtung ein (up, down, left, right) oder 'attack' oder 'heal': ")
                    if move1 in ['up', 'down', 'left', 'right']:
                        robot1.move(move1)
                    elif move1 == 'attack':
                        if robot1.attack(robot2):
                            print(f"{robot1.name} hat {robot2.name} getroffen!")
                        else:
                            print(f"{robot1.name} hat daneben geschossen!")
                    if move1 == 'heal':
                        if robot1.potions > 0:
                            if robot1.hp < 3:
                                robot1.healing()
                                print(f"{robot1.name} hat sich geheilt!")
                            else:
                                print(f"{robot1.name} hat zu viel Leben.")
                        else:
                            if robot1.potions == 0:
                                print("Du hast keine Tränke mehr")

        move2 = input(f"{robot2.name}, gib eine Richtung ein (up, down, left, right) oder 'attack' oder 'heal': ")
        if move2 in ['up', 'down', 'left', 'right']:
            robot2.move(move2)
        elif move2 == 'attack':
            if robot2.attack(robot1):
                print(f"{robot2.name} hat {robot1.name} getroffen!")
            else:
                print(f"{robot2.name} hat daneben geschossen!")
        if move2 == 'heal':
            if robot2.potions >0:
                if robot2.hp < 3:
                    robot2.healing()
                    print(f"{robot2.name} hat sich geheilt!")
                else:
                    print(f"{robot2.name} hat zu viel Leben.")
            else:
                if robot2.potions == 0:
                    print("Du hast keine Tränke mehr")
                    if move2 in ['up', 'down', 'left', 'right']:
                        robot2.move(move2)
                    elif move2 == 'attack':
                        if robot2.attack(robot1):
                            print(f"{robot2.name} hat {robot1.name} getroffen!")
                        else:
                            print(f"{robot2.name} hat daneben geschossen!")
                    if move2 == 'heal':
                        if robot2.potions > 0:
                            if robot2.hp < 3:
                                robot2.healing()
                                print(f"{robot2.name} hat sich geheilt!")
                            else:
                                print(f"{robot2.name} hat zu viel Leben.")
                        else:
                            if robot2.potions == 0:
                                print("Du hast keine Tränke mehr")
                                move2 = input(
                                    f"{robot2.name}, gib eine Richtung ein (up, down, left, right) oder 'attack' oder 'heal': ")
                                if move2 in ['up', 'down', 'left', 'right']:
                                    robot2.move(move2)
                                elif move2 == 'attack':
                                    if robot2.attack(robot1):
                                        print(f"{robot2.name} hat {robot1.name} getroffen!")
                                    else:
                                        print(f"{robot2.name} hat daneben geschossen!")
                                if move2 == 'heal':
                                    if robot2.potions > 0:
                                        if robot2.hp < 3:
                                            robot2.healing()
                                            print(f"{robot2.name} hat sich geheilt!")
                                        else:
                                            print(f"{robot2.name} hat zu viel Leben.")
                                    else:
                                        if robot2.potions == 0:
                                            print("Du hast keine Tränke mehr")
                                            if move2 in ['up', 'down', 'left', 'right']:
                                                robot2.move(move2)
                                            elif move2 == 'attack':
                                                if robot2.attack(robot1):
                                                    print(f"{robot2.name} hat {robot1.name} getroffen!")
                                                else:
                                                    print(f"{robot2.name} hat daneben geschossen!")
                                            if move2 == 'heal':
                                                if robot2.potions > 0:
                                                    if robot2.hp < 3:
                                                        robot2.healing()
                                                        print(f"{robot2.name} hat sich geheilt!")
                                                    else:
                                                        print(f"{robot2.name} hat zu viel Leben.")
                                                else:
                                                    if robot2.potions == 0:
                                                        print("Du hast keine Tränke mehr")





        print(f"{robot1.name}: Position ({robot1.x}, {robot1.y}), HP: {robot1.hp},Potions: {robot1.potions}")
        print(f"{robot2.name}: Position ({robot2.x}, {robot2.y}), HP: {robot2.hp}, Potions: {robot2.potions}")
    if robot1.hp==0:
        print("""""")
control_robots(robot1, robot2)