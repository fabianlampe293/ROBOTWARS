from Grafiken import AsciiArt

ascii_art = AsciiArt()


def start_game():
    while True:
        ascii_art.display_art_a()
        ascii_art.display_art_b()
        print("Möchtest du das Spiel starten?")
        antwort = input("Ja oder Nein: ").lower()
        if antwort == "ja":
            print("Das Spiel beginnt:")
            break
        elif antwort == "nein":
            print("Spiel wird beendet.")
            exit()
        else:
            print("Ungültige Eingabe. Starte die Eingabe erneut.")


roboname1 = input("Gib deinen Robotornamen ein: ")
roboname2 = input("Gib deinen Robotornamen ein: ")
start_game()
import random
from Roboter import Robot


def draw_field(robots, items, obstacles, width=15, height=10):
    print("   " + " ".join(f"{x:2}" for x in range(width)))  # X-Koordinaten
    field = [['[ ]' for _ in range(width)] for _ in range(height)]

    for robot in robots:
        field[robot.y][robot.x] = f'[{robot.name[0]}]'

    for item in items:
        field[item[1]][item[0]] = '[I]'  # Items mit "I" darstellen

    for obstacle in obstacles:
        field[obstacle[1]][obstacle[0]] = '[X]'  # Hindernisse mit "X" darstellen

    for y, row in enumerate(field):
        print(f"{y:2} " + ''.join(row))  # Y-Koordinaten


def spawn_point(width=15, height=10):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return x, y


def create_robot(name):
    print(f"{name}, verteile deine Attributpunkte:")
    points = 10
    movement_rate = attack_damage = attack_range = health = 1

    while points > 0:
        print(f"Punkte übrig: {points}")
        print(f"1. MovementRate: {movement_rate}, 2. AttackDamage: {attack_damage}, 3. AttackRange: {attack_range}, 4. Health: {health}")
        choice = input("Wähle ein Attribut (1-4): ")

        if choice == '1':
            movement_rate += 1
        elif choice == '2':
            attack_damage += 1
        elif choice == '3':
            attack_range += 1
        elif choice == '4':
            health += 1
        else:
            print("Ungültige Auswahl.")
            continue

        points -= 1

    x, y = spawn_point()
    return Robot(name, x, y, movement_rate, attack_damage, attack_range, health)

"""def count_rounds(count):
    count=0
    if control_robots():
        count+=1
"""
def apply_item_effect(robot, item):
        print(f"{robot.name} hat ein Item aufgesammelt!")
        robot.attack_damage += 1
        robot.energy += 2
        if robot.hp < robot.max_hp:
            robot.hp += 1
            print(f"{robot.name} wurde um 1 HP geheilt!")
        print(f"{robot.name}: AttackDamage: {robot.attack_damage}, Energie: {robot.energy}, HP: {robot.hp}")


def control_robots(robot1, robot2):
    items = [(5, 5), (10, 3)]
    obstacles = [(7, 5), (8, 5)]

    while robot1.hp > 0 and robot2.hp > 0:
        robots = sorted([robot1, robot2], key=lambda r: r.movement_rate, reverse=True)

        for robot in robots:
            if robot.hp <= 0:
                continue

            robot.reset_energy()
            draw_field(robots, items, obstacles)

            while robot.energy > 0:
                print(f"{robot.name}: Energie: {robot.energy}, HP: {robot.hp}")
                action = input(f"{robot.name}, wähle Aktion (move, attack): ").lower()

                if action == "move":
                    try:
                        target_x, target_y = map(int, input("Zielkoordinaten (x y): ").split())
                        if 0 <= target_x < 15 and 0 <= target_y < 10:
                            robot.move(target_x, target_y, obstacles)

                            # Prüfen, ob das Feld ein Item enthält
                            if (target_x, target_y) in items:
                                items.remove((target_x, target_y))
                                apply_item_effect(robot, (target_x, target_y))
                        else:
                            print("Ziel außerhalb des Spielfelds.")
                    except ValueError:
                        print("Ungültige Eingabe. Gib Koordinaten als 'x y' ein.")
                elif action == "attack":
                    target = robot2 if robot == robot1 else robot1
                    robot.attack(target, obstacles)
                else:
                    print("Ungültige Aktion.")

                if robot.energy <= 0:
                    print(f"{robot.name} hat keine Energie mehr für diesen Zug.")

        if robot1.hp <= 0:
            print(f"{robot2.name} hat gewonnen!")
            ascii_art.display_art_c()
            break
        elif robot2.hp <= 0:
            print(f"{robot1.name} hat gewonnen!")
            ascii_art.display_art_c()
            break


print("Roboter erstellen:")
robo1 = create_robot(roboname1)
robo2 = create_robot(roboname2)
control_robots(robo1, robo2)
