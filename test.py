from Roboter import Robot

from Grafiken import AsciiArt
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