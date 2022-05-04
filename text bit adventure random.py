#total number of bits are 64
storage = []

def write_byte(number, location):
    global storage
    #number 0-255
    #location: 0-7
    full = []
    for i in range(8):
        if 7 - len(bin(number)[2:]) < i:
            full.append(str(bin(number)[2:])[i-(8-len(str(bin(number)[2:])))])
        else:
            full.append(0)
    old = storage
    storage = []
    for i in range(8):
        for x in range(8):
            if not i == location:
                try:
                    storage.append(old[x+8*i])
                except:
                    storage.append(0)
            else:
                storage.append(int(full[x]))

def write_bit(location, bool=None):
    global storage
    #location: 0-63
    old = storage
    storage = []
    for i in range(64):
        if not i == location:
            try:
                storage.append(old[i])
            except:
                storage.append(0)
        else:
            if len(old) > location:
                if bool == None:
                    if old[i] == 0:
                        storage.append(1)
                    else:
                        storage.append(0)
                else:
                    if bool == False or bool == 0 or bool == None:
                        storage.append(0)
                    else:
                        storage.append(1)
            else:
                if bool == False or bool == 0:
                    storage.append(0)
                else:
                    storage.append(1)

def read_byte(location):
    global storage
    #location: 0-7
    #output 0-255
    output = ""

    for i in range(8):
        output += str(storage[i+8*location])
    return int(output, 2) 

def read_bit(location):
    global storage
    #location: 0-63
    #output: bool

    try:
        return storage[location]
    except:
        return 0

print("\x1B[2J")

print("\nhint, if you want to beat the game, only upgrade your strength by 1 and don't use any cheat codes!\n")

if (input("do you have a secret code? \n: ")+" ")[0] == "y":
    write_bit(63, 1)
    write_bit(61, True)
else:
    write_bit(63, False)
    write_bit(61, 0)

print("\x1B[2J")

write_byte(0, 6)
write_bit(62, 1)
write_byte(1, 5)
write_bit(56,0)

if read_bit(63) == 1:
    for c in input("what is the code?: ")[:4]:
        write_byte(int(bin(int.from_bytes(c.encode(), 'big')), 2), read_byte(6))
        write_byte(read_byte(6) + 1, 6)
else:
    print("psst, one code is \"poti\"! (enter to continue)")
    input("")

if read_bit(63) == 1 and read_byte(6) != 0:
    if read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "2":                
        if read_byte(6) == 4:
            write_byte(2, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["2", "l", "v", "l"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    elif read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "3":
        if read_byte(6) == 4:
            write_byte(3, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["3", "=", "0", "3"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    elif read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "e":
        if read_byte(6) == 3:
            write_byte(4, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["e", "x", "p"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    elif read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "l":
        if read_byte(6) == 4:
            write_byte(5, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["l", "v", "l", "5"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    elif read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "t":
        if read_byte(6) == 4:
            write_byte(255, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["t", "n", "t", "y"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    elif read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "B":
        if read_byte(6) == 4:
            write_byte(254, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["B", "0", "$", "$"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    elif read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "p":
        if read_byte(6) == 4:
            write_byte(253, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["p", "o", "t", "i"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    elif read_byte(0).to_bytes((read_byte(0).bit_length() + 7) // 8, 'big').decode() == "\x1b":
        if read_byte(6) == 4:
            write_byte(251, 5)
            write_bit(56,1)
            for i in range(read_byte(6)):
                if not read_byte(i).to_bytes((read_byte(i).bit_length() + 7) // 8, 'big').decode() == ["\x1b","[","A", "\x1b"][i]:
                    write_bit(62, 0)
                    write_byte(1, 5)
                    write_bit(56,0)
        else:
            write_bit(62, 0)
    else:
        write_bit(62, 0)
else:
    write_bit(62, 0)

if read_bit(62) == 0 and read_bit(61) == 1:
    print("invalid code (enter to continue)")
    input("")

print("\x1B[2J")

if read_bit(56) == 1:
    print("cheat enabled\n")

#game start

write_byte(read_byte(5), 0)
write_bit(62, 0)


#can be changed
write_byte(5, 4)
write_byte(2, 2)
write_byte(2, 5)


#advanced cheat codes
if read_byte(0) == 255:
    #tnty
    write_byte(1, 0)
    write_byte(20, 4)
    write_byte(20, 2)

if read_byte(0) == 254:
    #B0$$
    write_byte(5, 0)
    write_byte(20, 4)
    write_byte(20, 2)

if read_byte(0) == 253:
    #poti
    write_byte(1, 0)
    write_byte(100, 5)

if read_byte(0) == 251:
    #konami
    write_bit(56,0)
    print("you are a real gamer.\ntrue ending time!")
    write_byte(5, 0)
    write_byte(255, 4)
    write_byte(255, 2)
    write_byte(255, 5)

write_byte(read_byte(4), 3)

if read_byte(0) == 1:
    print(f"level {read_byte(0)} (enter to continue)")
    input("")
    print("\x1B[2J")

    write_bit(61, 1)
    write_bit(58, 1)
    write_bit(59, 0)
    write_bit(60, 0)

    #0: enemy strength, 1: enemy health, 2: player strength stat, 3: player health, 4: player health stat, 5: potion amount, (6: action, 7: bools and temporary variables)
    write_byte(2, 0)
    write_byte(5, 1)

    #enemy healed?
    write_bit(57, 0)

    print("you encounter a small rodent!")
    print(f"enemy health is {read_byte(1)}")

    while read_byte(1) > 0:
        if read_bit(60) == 1 and read_bit(59) == 1:
            write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        else:
            write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        while (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p" and read_byte(5) == 0) or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "a" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "p" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "d") or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1):
            print("\x1B[2J")
            if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
                print("no more potions!")
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1 and read_bit(58) == 1):
                print("too exausted")
                write_bit(58, 0)
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "s" or read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "l") and read_bit(61) == 1:
                print(f"player stats: \npotion amount: {read_byte(5)} \ncurrent health: {read_byte(3)} \nmax health: {read_byte(4)} \nstrength: {read_byte(2)} \n\nenemy stats: \nhealth: {read_byte(1)} \nstrength: {read_byte(0)} \n")
                write_bit(61, 0)
            else:
                print("invalid action")
            
            if read_bit(61) == 0 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 0:
                write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            else:
                write_byte(int(bin(int.from_bytes((input("do you potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        print("\x1B[2J")
        
        if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a":
            print(f"you attack! \n you do {read_byte(2)} damage!")
            if read_byte(1)-read_byte(2) < 1:
                write_byte(0, 1)
                print(f"enemy health is now {read_byte(1)}")
            else:
                write_byte(read_byte(1)-read_byte(2), 1)
                print(f"enemy health is now {read_byte(1)}")
            write_bit(63, 0)
            if read_bit(60) == 1:
                write_bit(59, 1)
            if read_bit(60) == 0:
                write_bit(60, 1)

        elif read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
            if 5 + read_byte(3) > read_byte(4):
                print(f"you restore {read_byte(4)-read_byte(3)} health!")
                write_byte(read_byte(4), 3)
            else:
                print(f"you restore 5 health!")
                write_byte(read_byte(3)+5, 3)
            write_byte(read_byte(5)-1, 5)
            if read_byte(5) == 1:
                print(f"you have {read_byte(5)} potion left!")
            else:
                print(f"you have {read_byte(5)} potions left")
            write_bit(63, 0)
            write_bit(60, 0)
            write_bit(59, 0)
        else:
            print("you defend!")
            #defended bool
            write_bit(63, 1)
            write_bit(60, 0)
            write_bit(59, 0)

        print()
        write_bit(61, 1)
        write_bit(58, 1)

        if read_byte(1) > 0:
            #1 in 3 chance it heals
            #hard code max health
            if next((int(0+3*(abs(hash(str(hash(str(hash(str(storage.count(1))))+str(i+1))))) % 10**13)/ 10**13) for i in range(2**6))) == 0 and read_byte(1) != 5 and read_bit(57) == 0:
                write_bit(57, 1)
                print("enemy heals!")
                if 2 + read_byte(1) > 5:
                    print(f"enemy restores {5-read_byte(1)} health.")
                    write_byte(5, 1)
                else:
                    print(f"enemy restores 2 health.")
                    write_byte(read_byte(1)+2, 1)
                print(f"enemy has {read_byte(1)} health.\n")
            else:
                write_bit(57, 0)
                print("enemy attacks!")
                if read_bit(63) == 1:
                    print(f"enemy does {int(read_byte(0)/2)} damage!")
                    if read_byte(3)-int(read_byte(0)/2) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-int(read_byte(0)/2), 3)
                else:
                    print(f"enemy does {read_byte(0)} damage!")
                    if read_byte(3)-read_byte(0) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-read_byte(0), 3)

            print(f"you have {read_byte(3)} health remaining!\n")
            if read_byte(3) < 1:
                print("you die!")
                write_bit(62, 1)
                break

    if read_bit(62) == 0:
        print("\x1B[2J")
        print("the rodent was defeated! \n")
        write_byte(2, 0)
        write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
        while read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "h" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "m" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "s":
            print("\x1B[2J")
            print("invalid option\n")
            write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
        if read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "h" or read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "m":
            print("\x1B[2J")
            write_byte(read_byte(4)+1, 4)
            print("max health increased by 1!")
        else:
            print("\x1B[2J")
            write_byte(read_byte(2)+1, 2)
            print("strength increased by 1!")
        write_byte(read_byte(4), 3)
        print(f"\nyou found {read_byte(0)} potions!\n")
        write_byte(read_byte(5)+read_byte(0), 5)
#copy this template
if read_byte(0) == 2 and read_bit(62) == 0:
    print(f"level {read_byte(0)} (enter to continue)")
    input("")
    print("\x1B[2J")

    write_bit(61, 1)
    write_bit(58, 1)
    write_bit(59, 0)
    write_bit(60, 0)

    #0: enemy strength, 1: enemy health, 2: player strength stat, 3: player health, 4: player health stat, 5: potion amount, (6: action, 7: bools and temporary variables)
    write_byte(3, 0)
    write_byte(4, 1)

    #enemy healed?
    write_bit(57, 0)

    print("you encounter a evil ghoul!")
    print(f"enemy health is {read_byte(1)}")

    while read_byte(1) > 0:
        if read_bit(60) == 1 and read_bit(59) == 1:
            write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        else:
            write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        while (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p" and read_byte(5) == 0) or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "a" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "p" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "d") or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1):
            print("\x1B[2J")
            if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
                print("no more potions!")
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1 and read_bit(58) == 1):
                print("too exausted")
                write_bit(58, 0)
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "s" or read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "l") and read_bit(61) == 1:
                print(f"player stats: \npotion amount: {read_byte(5)} \ncurrent health: {read_byte(3)} \nmax health: {read_byte(4)} \nstrength: {read_byte(2)} \n\nenemy stats: \nhealth: {read_byte(1)} \nstrength: {read_byte(0)} \n")
                write_bit(61, 0)
            else:
                print("invalid action")
            
            if read_bit(61) == 0 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 0:
                write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            else:
                write_byte(int(bin(int.from_bytes((input("do you potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        print("\x1B[2J")
        
        if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a":
            print(f"you attack! \n you do {read_byte(2)} damage!")
            if read_byte(1)-read_byte(2) < 1:
                write_byte(0, 1)
                print(f"enemy health is now {read_byte(1)}")
            else:
                write_byte(read_byte(1)-read_byte(2), 1)
                print(f"enemy health is now {read_byte(1)}")
            write_bit(63, 0)
            if read_bit(60) == 1:
                write_bit(59, 1)
            if read_bit(60) == 0:
                write_bit(60, 1)

        elif read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
            if 5 + read_byte(3) > read_byte(4):
                print(f"you restore {read_byte(4)-read_byte(3)} health!")
                write_byte(read_byte(4), 3)
            else:
                print(f"you restore 5 health!")
                write_byte(read_byte(3)+5, 3)
            write_byte(read_byte(5)-1, 5)
            if read_byte(5) == 1:
                print(f"you have {read_byte(5)} potion left!")
            else:
                print(f"you have {read_byte(5)} potions left")
            write_bit(63, 0)
            write_bit(60, 0)
            write_bit(59, 0)
        else:
            print("you defend!")
            #defended bool
            write_bit(63, 1)
            write_bit(60, 0)
            write_bit(59, 0)

        print()
        write_bit(61, 1)
        write_bit(58, 1)

        if read_byte(1) > 0:
            #1 in 5 chance it heals
            #hard code max health
            if next((int(0+3*(abs(hash(str(hash(str(hash(str(storage.count(1))))+str(i+1))))) % 10**13)/ 10**13) for i in range(2**6))) == 0 and read_byte(1) != 4 and read_bit(57) == 0:
                write_bit(57, 1)
                print("enemy heals!")
                if 2 + read_byte(1) > 4:
                    print(f"enemy restores {4-read_byte(1)} health.")
                    write_byte(4, 1)
                else:
                    print(f"enemy restores 2 health.")
                    write_byte(read_byte(1)+2, 1)
                print(f"enemy has {read_byte(1)} health.\n")
            else:
                write_bit(57, 0)
                print("enemy attacks!")
                if read_bit(63) == 1:
                    print(f"enemy does {int(read_byte(0)/2)} damage!")
                    if read_byte(3)-int(read_byte(0)/2) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-int(read_byte(0)/2), 3)
                else:
                    print(f"enemy does {read_byte(0)} damage!")
                    if read_byte(3)-read_byte(0) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-read_byte(0), 3)

            print(f"you have {read_byte(3)} health remaining!\n")
            if read_byte(3) < 1:
                print("you die!")
                write_bit(62, 1)
                break
                
    if read_bit(62) == 0:
        print("\x1B[2J")
        print("the ghoul was defeated! \n")
        write_byte(3, 0)
        write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
        while read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "h" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "m" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "s":
            print("\x1B[2J")
            print("invalid option\n")
            write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
        if read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "h" or read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "m":
            print("\x1B[2J")
            write_byte(read_byte(4)+1, 4)
            print("max health increased by 1!")
        else:
            print("\x1B[2J")
            write_byte(read_byte(2)+1, 2)
            print("strength increased by 1!")
        write_byte(read_byte(4), 3)
        print(f"\nyou found {read_byte(0)} potions!\n")
        write_byte(read_byte(5)+read_byte(0), 5)

if read_byte(0) == 3 and read_bit(62) == 0:
    print(f"level {read_byte(0)} (enter to continue)")
    input("")
    print("\x1B[2J")

    write_bit(61, 1)
    write_bit(58, 1)
    write_bit(59, 0)
    write_bit(60, 0)

    #0: enemy strength, 1: enemy health
    write_byte(2, 0)
    write_byte(10, 1)

    #enemy healed?
    write_bit(57, 0)

    print("you encounter an evil lake monster!")
    print(f"enemy health is {read_byte(1)}")

    while read_byte(1) > 0:
        if read_bit(60) == 1 and read_bit(59) == 1:
            write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        else:
            write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        while (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p" and read_byte(5) == 0) or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "a" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "p" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "d") or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1):
            print("\x1B[2J")
            if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
                print("no more potions!")
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1 and read_bit(58) == 1):
                print("too exausted")
                write_bit(58, 0)
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "s" or read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "l") and read_bit(61) == 1:
                print(f"player stats: \npotion amount: {read_byte(5)} \ncurrent health: {read_byte(3)} \nmax health: {read_byte(4)} \nstrength: {read_byte(2)} \n\nenemy stats: \nhealth: {read_byte(1)} \nstrength: {read_byte(0)} \n")
                write_bit(61, 0)
            else:
                print("invalid action")
            
            if read_bit(61) == 0 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 0:
                write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            else:
                write_byte(int(bin(int.from_bytes((input("do you potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        print("\x1B[2J")
        
        if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a":
            print(f"you attack! \n you do {read_byte(2)} damage!")
            if read_byte(1)-read_byte(2) < 1:
                write_byte(0, 1)
                print(f"enemy health is now {read_byte(1)}")
            else:
                write_byte(read_byte(1)-read_byte(2), 1)
                print(f"enemy health is now {read_byte(1)}")
            write_bit(63, 0)
            if read_bit(60) == 1:
                write_bit(59, 1)
            if read_bit(60) == 0:
                write_bit(60, 1)

        elif read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
            if 5 + read_byte(3) > read_byte(4):
                print(f"you restore {read_byte(4)-read_byte(3)} health!")
                write_byte(read_byte(4), 3)
            else:
                print(f"you restore 5 health!")
                write_byte(read_byte(3)+5, 3)
            write_byte(read_byte(5)-1, 5)
            if read_byte(5) == 1:
                print(f"you have {read_byte(5)} potion left!")
            else:
                print(f"you have {read_byte(5)} potions left")
            write_bit(63, 0)
            write_bit(60, 0)
            write_bit(59, 0)
        else:
            print("you defend!")
            #defended bool
            write_bit(63, 1)
            write_bit(60, 0)
            write_bit(59, 0)

        print()
        write_bit(61, 1)
        write_bit(58, 1)

        if read_byte(1) > 0:
            #1 in 5 chance it heals
            #hard code max health
            if next((int(0+3*(abs(hash(str(hash(str(hash(str(storage.count(1))))+str(i+1))))) % 10**13)/ 10**13) for i in range(2**6))) == 0 and read_byte(1) != 10 and read_bit(57) == 0:
                write_bit(57, 1)
                print("enemy heals!")
                if 2 + read_byte(1) > 10:
                    print(f"enemy restores {10-read_byte(1)} health.")
                    write_byte(10, 1)
                else:
                    print(f"enemy restores 2 health.")
                    write_byte(read_byte(1)+2, 1)
                print(f"enemy has {read_byte(1)} health.\n")
            else:
                write_bit(57, 0)
                print("enemy attacks!")
                if read_bit(63) == 1:
                    print(f"enemy does {int(read_byte(0)/2)} damage!")
                    if read_byte(3)-int(read_byte(0)/2) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-int(read_byte(0)/2), 3)
                else:
                    print(f"enemy does {read_byte(0)} damage!")
                    if read_byte(3)-read_byte(0) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-read_byte(0), 3)
            print(f"you have {read_byte(3)} health remaining!\n")
            if read_byte(3) < 1:
                print("you die!")
                write_bit(62, 1)
                break
                

    if read_bit(62) == 0:
        print("\x1B[2J")
        print("the lake monster was defeated! \n")
        write_byte(4, 0)
        write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
        while read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "h" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "m" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "s":
            print("\x1B[2J")
            print("invalid option\n")
            write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
        if read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "h" or read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "m":
            print("\x1B[2J")
            write_byte(read_byte(4)+1, 4)
            print("max health increased by 1!")
        else:
            print("\x1B[2J")
            write_byte(read_byte(2)+1, 2)
            print("strength increased by 1!")
        write_byte(read_byte(4), 3)
        print(f"\nyou found {read_byte(0)} potions!\n")
        write_byte(read_byte(5)+read_byte(0), 5)

if read_byte(0) == 4 and read_bit(62) == 0:
    print(f"level {read_byte(0)} (enter to continue)")
    input("")
    print("\x1B[2J")
    print("you find an XP orb!\n")

    write_byte(5, 0)
    write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
    while read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "h" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "m" and read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() != "s":
        print("\x1B[2J")
        print("invalid option\n")
        write_byte(int(bin(int.from_bytes((input("would you like to increase your max health or strength? \n: ") + " ")[0].encode(), 'big')), 2), 1)
    if read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "h" or read_byte(1).to_bytes((read_byte(1).bit_length() + 7) // 8, 'big').decode() == "m":
        print("\x1B[2J")
        write_byte(read_byte(4)+1, 4)
        print("max health increased by 1!")
    else:
        print("\x1B[2J")
        write_byte(read_byte(2)+1, 2)
        print("strength increased by 1!")

if read_byte(0) == 5 and read_bit(62) == 0:
    print("\nBOSS\n")
    print(f"level {read_byte(0)} (enter to continue)")
    input("")
    print("\x1B[2J")

    write_bit(61, 1)
    write_bit(58, 1)
    write_bit(59, 0)
    write_bit(60, 0)

    #0: enemy strength, 1: enemy health
    write_byte(3, 0)
    write_byte(20, 1)

    #enemy healed?
    write_bit(57, 0)

    print("you encounter a massive evil duck!")
    print(f"enemy health is {read_byte(1)}")

    while read_byte(1) > 0:
        if read_bit(60) == 1 and read_bit(59) == 1:
            write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        else:
            write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        while (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p" and read_byte(5) == 0) or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "a" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "p" and read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() != "d") or (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1):
            print("\x1B[2J")
            if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
                print("no more potions!")
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a" and read_bit(60) == 1 and read_bit(59) == 1 and read_bit(58) == 1):
                print("too exausted")
                write_bit(58, 0)
            elif (read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "s" or read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "l") and read_bit(61) == 1:
                print(f"player stats: \npotion amount: {read_byte(5)} \ncurrent health: {read_byte(3)} \nmax health: {read_byte(4)} \nstrength: {read_byte(2)} \n\nenemy stats: \nhealth: {read_byte(1)} \nstrength: {read_byte(0)} \n")
                write_bit(61, 0)
            else:
                print("invalid action")
            
            if read_bit(61) == 0 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 1:
                write_byte(int(bin(int.from_bytes((input("do you attack, potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            elif read_bit(61) == 1 and read_bit(58) == 0:
                write_byte(int(bin(int.from_bytes((input("do you potion, defend or look at stats? \n: ")+" ")[0].encode(), 'big')), 2), 6)
            else:
                write_byte(int(bin(int.from_bytes((input("do you potion or defend? \n: ")+" ")[0].encode(), 'big')), 2), 6)
        print("\x1B[2J")
        
        if read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "a":
            print(f"you attack! \n you do {read_byte(2)} damage!")
            if read_byte(1)-read_byte(2) < 1:
                write_byte(0, 1)
                print(f"enemy health is now {read_byte(1)}")
            else:
                write_byte(read_byte(1)-read_byte(2), 1)
                print(f"enemy health is now {read_byte(1)}")
            write_bit(63, 0)
            if read_bit(60) == 1:
                write_bit(59, 1)
            if read_bit(60) == 0:
                write_bit(60, 1)

        elif read_byte(6).to_bytes((read_byte(6).bit_length() + 7) // 8, 'big').decode() == "p":
            if 5 + read_byte(3) > read_byte(4):
                print(f"you restore {read_byte(4)-read_byte(3)} health!")
                write_byte(read_byte(4), 3)
            else:
                print(f"you restore 5 health!")
                write_byte(read_byte(3)+5, 3)
            write_byte(read_byte(5)-1, 5)
            if read_byte(5) == 1:
                print(f"you have {read_byte(5)} potion left!")
            else:
                print(f"you have {read_byte(5)} potions left")
            write_bit(63, 0)
            write_bit(60, 0)
            write_bit(59, 0)
        else:
            print("you defend!")
            #defended bool
            write_bit(63, 1)
            write_bit(60, 0)
            write_bit(59, 0)

        print()
        write_bit(61, 1)
        write_bit(58, 1)

        if read_byte(1) > 0:
            #1 in 5 chance it heals
            #hard code max health
            if next((int(0+3*(abs(hash(str(hash(str(hash(str(storage.count(1))))+str(i+1))))) % 10**13)/ 10**13) for i in range(2**6))) == 0 and read_byte(1) != 20 and read_bit(57) == 0:
                write_bit(57, 1)
                print("enemy heals!")
                if 2 + read_byte(1) > 20:
                    print(f"enemy restores {20-read_byte(1)} health.")
                    write_byte(20, 1)
                else:
                    print(f"enemy restores 2 health.")
                    write_byte(read_byte(1)+2, 1)
                print(f"enemy has {read_byte(1)} health.\n")
            else:
                write_bit(57, 0)
                print("enemy attacks!")
                if read_bit(63) == 1:
                    print(f"enemy does {int(read_byte(0)/2)} damage!")
                    if read_byte(3)-int(read_byte(0)/2) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-int(read_byte(0)/2), 3)
                else:
                    print(f"enemy does {read_byte(0)} damage!")
                    if read_byte(3)-read_byte(0) < 1:
                        write_byte(0, 3)
                    else:
                        write_byte(read_byte(3)-read_byte(0), 3)
            print(f"you have {read_byte(3)} health remaining!\n")
            if read_byte(3) < 1:
                print("you die!")
                write_bit(62, 1)
                break
                    

    if read_bit(62) == 0:
        print("\x1B[2J")
        if read_bit(56) == 1:
            print("great, now try beat it without cheats!\n")
        else:
            print("the huge evil duck was defeated and peace was restored to the land!\n")

print("\nEND\n")
pass