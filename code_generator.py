#X4119999999999X0000239999X0000120000239999X8JH3741925R
#potion_amount, strength, enemy_health,health, level, enemy_strength, potion_effectiveness

code = ""
formatting_number = 1
variables = [9,999999,1,999999,1,1,999999]
for v in variables:
    if len(str(v)) > formatting_number:
        formatting_number = len(str(v))
for v in variables:
    code += str(v).zfill(formatting_number)
code = str(int(code) * formatting_number)
code = str(int(code) * 2)
new_code = ""
for i in range(int(len(code)/2)):
    if int(code[2*i:2*i+2]) < 91 and int(code[2*i:2*i+2]) > 64:
        new_code += chr(int(code[2*i:2*i+2]))
    else:
        new_code += code[2*i:2*i+2]
if len(code)%2==1:
    new_code+=code[-1]
print("code is X4" + new_code + str(hash("a")%9+1) + chr(hash("b")%26+65) + chr(hash("c")%26+65) + "".join(str(hash(str(i))%10)for i in range(formatting_number)) + str(hash("d")%9+1) + chr(hash("e")%26+65)+"\n")