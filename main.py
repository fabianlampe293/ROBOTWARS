from Grafiken import AsciiArt

ascii_art = AsciiArt()

while True:
    ascii_art.display_art_a()
    ascii_art.display_art_b()

    roboname1 = input("Gib deinen Robotornamen ein: ")
    roboname2 = input("Gib deinen Robotornamen ein: ")
    print("Herzlich Willkommen: ", roboname1, roboname2)

    print("Möchtest du das Spiel starten?")
    antwort = input("Ja oder Nein: ").lower()
    if antwort == "ja":
        print("Das Spiel beginnt:")
        break
    else:
        print("Starte die Eingabe erneut.")

from Roboter import Robot

def draw_field(robots, width=15, height=10):
    field = [['[ ]' for _ in range(width)] for _ in range(height)]

    for robot in robots:
        field[robot.y][robot.x] = f'[{robot.name[0]}]'

    for row in field:
        print(''.join(row))


robot1 = Robot(roboname1, 0, 0)
robot2 = Robot(roboname2, 1, 0)


def control_robots(robot1, robot2):
    while robot1.hp > 0 and robot2.hp > 0:
        draw_field([robot1, robot2])

        move1 = input(f"{robot1.name}, gib eine Richtung ein (up, down, left, right) oder 'attack', 'heal', 'shield': ")
        if move1 in ['up', 'down', 'left', 'right']:
            robot1.move(move1)
        elif move1 == 'attack':
            robot1.attack(robot2)
        elif move1 == 'shield':
            robot1.shielding()
        elif move1 == 'heal':
            if robot1.potions > 0:
                if robot1.hp < 3:
                    robot1.healing()
                    print(f"{robot1.name} hat sich geheilt!")
                else:
                    print(f"{robot1.name} hat zu viel Leben.")
            else:
                print("Du hast keine Tränke mehr")

        move2 = input(f"{robot2.name}, gib eine Richtung ein (up, down, left, right) oder 'attack', 'heal', 'shield': ")
        if move2 in ['up', 'down', 'left', 'right']:
            robot2.move(move2)
        elif move2 == 'attack':
            robot2.attack(robot1)
        elif move2 == 'shield':
            robot2.shielding()
        elif move2 == 'heal':
            if robot2.potions > 0:
                if robot2.hp < 3:
                    robot2.healing()
                    print(f"{robot2.name} hat sich geheilt!")
                else:
                    print(f"{robot2.name} hat zu viel Leben.")
            else:
                print("Du hast keine Tränke mehr")


        print(f"{robot1.name}: Position ({robot1.x}, {robot1.y}), HP: {robot1.hp},Potions: {robot1.potions},Shield:{robot1.shield_active}")
        print(f"{robot2.name}: Position ({robot2.x}, {robot2.y}), HP: {robot2.hp}, Potions: {robot2.potions},Shield:{robot2.shield_active}")
    if robot1.hp==0 :
        print("Player 2 hat gewonnen!!!")
        ascii_art.display_art_c()
    else:
        print("Player 1 hat gewonnen!!!")
        ascii_art.display_art_c()


control_robots(robot1, robot2)