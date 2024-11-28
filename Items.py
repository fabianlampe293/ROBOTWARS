class item:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def apply_effects(self, robot):
        robot.attack_damage += 1
        robot.energy += 2
        robot.hp = min(robot.hp + 1, 3)  # Maximal auf 3 HP begrenzen
        print(f"{robot.name} hat ein Item aufgenommen! AttackDamage +1, Energie +2, HP +1.")

