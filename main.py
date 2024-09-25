'''a=

__        __   _                            _          
\\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___    
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\   
  \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |  
 __\\_/\\_/_\\___|_|\\___\\___/|_| |_| |_|\\___| _\\__\\___/_  
|  _ \\ / _ \\| __ ) / _ \\  \\ \\      / / \\  |  _ \\/ ___| 
| |_) | | | |  _ \\| | | |  \ \\ /\\ / / _ \\ | |_) \___ \\ 
|  _ <| |_| | |_) | |_| |   \\ V  V / ___ \\|  _ < ___) |
|_| \_\\\\___/|____/ \___/     \\_/\\_/_/   \\_\\_| \\_\\____/ 



print(a)

b=
   _____             _____
  |_____|___________|_____|
  |_____| / _____ \\ |_____|
  |_____|/ /\\___/\\ \\|_____|
 /|====|__/_/___\\_\\__|====|\\
 ||====|  _/_\\_/_\\_  |====||
 \|====| | \\ ... / | |====|/
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
        >---/   \\---<
        ||#|     |#||
        ||-|\\   /|-||
        ||+||   ||+||
        ||-|/   \\|-||
        ||_|\\   /|_||   
     ___|/-\\/   \\/-\\|___
    /________\\ /________\\


print(b)
robo_Name=input("Gib deinen Robotornamen ein: ")
print("Herzlich Willkommen: ",robo_Name)

play_field=
  1    2    3    4    5    6    7    8    9    10  11    12   13   14   15  
.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | A
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | B
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | C
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | D
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | E
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | F
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | G
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | H
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | I
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | J
|____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|



print("Möchtest du das Spiel starten?")
Antwort=input("Ja oder Nein: ")
if Antwort.lower() == "ja":
    print(play_field)
else:
    print(a,b)


'''


class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.hp = 3

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


def draw_field(robots, width=15, height=10):
    field = [['.' for _ in range(width)] for _ in range(height)]

    for robot in robots:
        field[robot.y][robot.x] = robot.name[0]

    for row in field:
        print(' '.join(row))


# Beispiel für die Erstellung und Bewegung von Robotern
robot1 = Robot("Alpha", 0, 0)
robot2 = Robot("Beta", 1, 0)


# Funktion zur Steuerung der Roboter durch Benutzereingaben
def control_robots(robot1, robot2):
    while robot1.hp > 0 and robot2.hp > 0:
        draw_field([robot1, robot2])

        # Eingabe für Roboter 1
        move1 = input(f"{robot1.name}, gib eine Richtung ein (up, down, left, right) oder 'attack': ")
        if move1 in ['up', 'down', 'left', 'right']:
            robot1.move(move1)
        elif move1 == 'attack':
            if robot1.attack(robot2):
                print(f"{robot1.name} hat {robot2.name} getroffen!")
            else:
                print(f"{robot1.name} hat daneben geschossen!")

        # Eingabe für Roboter 2
        move2 = input(f"{robot2.name}, gib eine Richtung ein (up, down, left, right) oder 'attack': ")
        if move2 in ['up', 'down', 'left', 'right']:
            robot2.move(move2)
        elif move2 == 'attack':
            if robot2.attack(robot1):
                print(f"{robot2.name} hat {robot1.name} getroffen!")
            else:
                print(f"{robot2.name} hat daneben geschossen!")

        # Status der Roboter anzeigen
        print(f"{robot1.name}: Position ({robot1.x}, {robot1.y}), HP: {robot1.hp}")
        print(f"{robot2.name}: Position ({robot2.x}, {robot2.y}), HP: {robot2.hp}")


# Roboter steuern
control_robots(robot1, robot2)
