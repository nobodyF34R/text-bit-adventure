code = input("\x1B[2Jdo you have a code: ").strip().upper()
print("\x1B[2J")
code_used = False
if code and code[:1].lower() != "n":
    valid = True
    if code[:2] != "X4":
        valid = False
    else:
        original = code
        try:
            formatting_number = ""
            for i in range(len(code[:-2])):
                if code[i * -1 - 3].isalpha():
                    break
                else:
                    formatting_number += code[i * -1 - 3]
            code = code[2 : -5 - len(formatting_number)]
            new_code = ""
            for c in code:
                if c.isalpha():
                    new_code += str(ord(c))
                else:
                    new_code += c
            code = int(int(new_code) // 2)
            code = int(int(new_code) // len(formatting_number))
            code = str(code // 2)[::-1]
            variables = [
                int(code[i : i + len(formatting_number)])
                for i in range(0, len(code), len(formatting_number))
            ][::-1]
            variables = [int(str(v)[::-1]) for v in variables]
            pass
            for v in variables:
                if len(str(v)) > len(formatting_number) or v < 1:
                    valid = False
        except:
            valid = False
    if not valid:
        print("invalid code")
    else:
        code_used = True


alive = 1
level = 1
potion_amount = hash(" ") % 4 + 3  # max is 6
potion_effectiveness = hash(" ") % 2 + 2  # max is 3
health = hash(" ") % 5 + 4  # max is 8
strength = hash(" ") % 3 + 2  # max is 4
while alive == 1:
    current_health = health
    enemy_health = hash(str(level)) % 6 + level  # max is level + 5
    enemy_strength = hash(str(level)) % 5 + level  # max is level + 4
    if code_used:
        (
            potion_amount,
            strength,
            enemy_health,
            health,
            level,
            enemy_strength,
            potion_effectiveness,
        ) = (*variables,)
    print("\nlevel", level)
    print("enemy health is", enemy_health)
    print("enemy strength is", enemy_strength)
    print("your health is", health)
    print("your strength is", strength)
    print("potion amount is", potion_amount)
    print("potion effectiveness is", potion_effectiveness, "\n")
    if not code_used:
        code = ""
        formatting_number = 1
        variables = [
            potion_amount,
            strength,
            enemy_health,
            health,
            level,
            enemy_strength,
            potion_effectiveness,
        ]
        for v in variables:
            if len(str(v)) > formatting_number:
                formatting_number = len(str(v))
        for v in variables:
            code += str(v).zfill(formatting_number)
        code = str(int(code) * formatting_number)
        code = str(int(code) * 2)
        new_code = ""
        for i in range(int(len(code) / 2)):
            if int(code[2 * i : 2 * i + 2]) < 91 and int(code[2 * i : 2 * i + 2]) > 64:
                new_code += chr(int(code[2 * i : 2 * i + 2]))
            else:
                new_code += code[2 * i : 2 * i + 2]
        if len(code) % 2 == 1:
            new_code += code[-1]
        print(
            "code is X4"
            + new_code
            + str(hash("a") % 9 + 1)
            + chr(hash("b") % 26 + 65)
            + chr(hash("c") % 26 + 65)
            + "".join(str(hash(str(i)) % 10) for i in range(formatting_number))
            + str(hash("d") % 9 + 1)
            + chr(hash("e") % 26 + 65)
            + "\n"
        )
    else:
        print("code is " + original + "\n")
        code_used = False
    while enemy_health > 0 and alive == 1:
        action = ""
        while not action in ["a", "p", "d"] or action == "p" and potion_amount == 0:
            action = input("actions are attack, potion and defend: ")[:1]
        if action == "p":
            current_health += potion_effectiveness
        if action == "a":
            enemy_health -= strength
        if action == "d":
            current_health -= (enemy_strength) / 2
        else:
            if enemy_health > 0:
                current_health -= enemy_strength
        if current_health <= 0:
            alive = 0
        print("\x1B[2Jenemy health is", enemy_health)
        print("your health is", current_health, "\n")
    if alive == 1:
        level += 1
        potion_amount += level
        upgrade = ""
        while not upgrade in ["1", "2", "3"]:
            upgrade = input(
                "what would you like to upgrade?\n1=health\n2=strength\n3=potion effectiveness\n: "
            )
            print("\x1B[2J")
        if upgrade == "1":
            health += 1
        if upgrade == "2":
            strength += 1
        if upgrade == "3":
            potion_effectiveness += 1
pass