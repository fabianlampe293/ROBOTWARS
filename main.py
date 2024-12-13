from Grafiken import AsciiArt

ascii_art = AsciiArt()
ascii_art.display_art_a()
ascii_art.display_art_b()
roboname1 = input("Gib deinen Robotornamen ein: ")
roboname2 = input("Gib deinen Robotornamen ein: ")


def start_game():
    while True:
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


start_game()
import random
from Roboter import Robot


def draw_field(robots, items, obstacles, width=15, height=10):
    print("   " + " ".join(f"{x:2}" for x in range(width)))
    field = [['[ ]' for _ in range(width)] for _ in range(height)]

    for robot in robots:
        field[robot.y][robot.x] = f'[{robot.name[0]}]'

    for item in items:
        field[item[1]][item[0]] = '[I]'

    for obstacle in obstacles:
        field[obstacle[1]][obstacle[0]] = '[X]'

    for y, row in enumerate(field):
        print(f"{y:2} " + ''.join(row))


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


def apply_item_effect(robot, item):
        print(f"{robot.name} hat ein Item aufgesammelt!")
        robot.attack_damage += 1
        robot.energy += 2
        if robot.hp < robot.max_hp:
            robot.hp += 1
            print(f"{robot.name} wurde um 1 HP geheilt!")
        print(f"{robot.name}: AttackDamage: {robot.attack_damage}, Energie: {robot.energy}, HP: {robot.hp}")

def generate_obstacles():
    number_of_obstacles = 15
    felder = [(x, y) for x in range(15) for y in range(10)]
    return random.sample(felder, number_of_obstacles)

def generate_items():
    number_of_items = 4
    felder = [(x, y) for x in range(15) for y in range(10)]
    return random.sample(felder, number_of_items)

def control_robots(robot1, robot2):
    obstacles = generate_obstacles()
    items = generate_items()

    robots = [robot1, robot2]
    current_turn = 0

    while robot1.hp > 0 and robot2.hp > 0:
        current_robot = robots[current_turn]
        other_robot = robots[1 - current_turn]

        if current_robot.hp <= 0:
            current_turn = 1 - current_turn
            continue

        current_robot.reset_energy()
        draw_field(robots, items, obstacles)

        print(f"{current_robot.name} ist am Zug!")
        print(f"{current_robot.name}: Energie: {current_robot.energy}, HP: {current_robot.hp}")
        action = input(f"{current_robot.name}, wähle Aktion (move, attack): ").lower()

        if action == "move":
            try:
                target_x, target_y = map(int, input("Zielkoordinaten (x y): ").split())
                if 0 <= target_x < 15 and 0 <= target_y < 10:
                    current_robot.move(target_x, target_y, obstacles)

                    if (target_x, target_y) in items:
                        items.remove((target_x, target_y))
                        apply_item_effect(current_robot, (target_x, target_y))
                else:
                    print("Ziel außerhalb des Spielfelds.")
            except ValueError:
                print("Ungültige Eingabe. Gib Koordinaten als 'x y' ein.")
        elif action == "attack":
            current_robot.attack(other_robot, obstacles)
        else:
            print("Ungültige Aktion.")

        if current_robot.energy <= 0:
            print(f"{current_robot.name} hat keine Energie mehr für diesen Zug.")

        if robot1.hp <= 0:
            print(f"{robot2.name} hat gewonnen!")
            ascii_art.display_art_c()
            break
        elif robot2.hp <= 0:
            print(f"{robot1.name} hat gewonnen!")
            ascii_art.display_art_c()
            break

        current_turn = 1 - current_turn
items = [(x, y) for x, y in random.sample([(x, y) for x in range(15) for y in range(10)], 4)]
obstacals = [(x, y) for x, y in random.sample([(x, y) for x in range(15) for y in range(10)], 8)]

robo1 = create_robot(roboname1)
robo2 = create_robot(roboname2)
control_robots(robo1, robo2)
