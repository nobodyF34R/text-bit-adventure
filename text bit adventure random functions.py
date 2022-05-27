storage=[]
def write_byte(number,location):
 global storage;full=[];[full.append(str(bin(number)[2:])[i-(8-len(str(bin(number)[2:])))])if 7-len(bin(number)[2:])<i else full.append(0)for i in range(8)];old=storage;storage=[]
 for i in range(8):
  for x in range(8):
   if not i==location:
    try:
     storage.append(old[x+8*i])
    except:
     storage.append(0)
   else:
    storage.append(int(full[x]))
def write_bit(location,bool=None):
 global storage;old=storage;storage=[]
 for i in range(64):
  if not i==location:
   try:
    storage.append(old[i])
   except:
    storage.append(0)
  else:
   if len(old)>location:
    storage.append(0)if bool!=True else storage.append(1)
   else:
    storage.append(0)if bool!=True else storage.append(1)
def read_byte(location):
 global storage;return int(''.join([str(storage[i+8*location])for i in range(8)]),2)
def read_bit(location):
 global storage
 try:
  return storage[location]
 except:
  return 0
def level():
 write_bit(57,0);write_bit(58,1);write_bit(59,0);write_bit(60,0);print(f"Enemy health is {read_byte(1)}.")
 while read_byte(1)>0:
  write_byte(int(bin(int.from_bytes((input("Do you potion, defend or look at stats?\n: "if read_bit(60)==1 and read_bit(59)==1 else"Do you attack, potion, defend or look at stats?\n: ")+" ").lower()[0].encode(),'big')),2),6)
  while (read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="p"and read_byte(5)==0)or(read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()!="a"and read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()!="p"and read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()!="d")or(read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="a"and read_bit(60)==1 and read_bit(59)==1):print("\x1B[2JNo more potions!")if read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="p"else print("\x1B[2JToo exausted.")if(read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="a"and read_bit(60)==1 and read_bit(59)==1)else print(f"\x1B[2JPlayer stats:\npotion amount: {read_byte(5)}\ncurrent health: {read_byte(3)}\nmax health: {read_byte(4)}\nstrength: {read_byte(2)}\n\nenemy stats:\nhealth: {read_byte(1)}\nstrength: {read_byte(0)}\n")if(read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="s"or read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="l")else print("\x1B[2JInvalid action.");write_bit(58,0)if read_bit(60)==1 and read_bit(59)==1 else 0;print("Nice.\n")if read_bit(61)==1 and(read_byte(5)==69 or read_byte(3)==69 or read_byte(5)==169 or read_byte(3)==169)and(read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="s"or read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="l")else 0;write_byte(int(bin(int.from_bytes((input("Do you potion, defend or look at stats?\n: "if read_bit(60)==1 and read_bit(59)==1 else"Do you attack, potion, defend or look at stats?\n: ")+" ").lower()[0].encode(),'big')),2),6)
  if read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="a":
   print(f"\x1B[2JYou attack!\nYou do {read_byte(2)} damage!");write_byte(0,1)if read_byte(1)-read_byte(2)<1 else write_byte(read_byte(1)-read_byte(2),1);print(f"Enemy health is now {read_byte(1)}.");write_bit(63,0);write_bit(59,1)if read_bit(60)==1 else 0;write_bit(60,1)if read_bit(60)==0 else 0
  elif read_byte(6).to_bytes((read_byte(6).bit_length()+7)//8,'big').decode()=="p":
   if 5+read_byte(3)>read_byte(4):
    print(f"\x1B[2JYou restore {read_byte(4)-read_byte(3)} health!");write_byte(read_byte(4),3)
   else:
    print(f"\x1B[2JYou restore 5 health!");write_byte(read_byte(3)+5,3)
   write_byte(read_byte(5)-1,5);print(f"You have {read_byte(5)} potion left!"if read_byte(5)==1 else f"You have {read_byte(5)} potions left!");write_bit(63,0);write_bit(60,0);write_bit(59,0);print("Nice.")if read_byte(5)==69 or read_byte(5)==169 and read_bit(61)==1 else 0
  else:
   print("\x1B[2JYou defend!");write_bit(63,1);write_bit(60,0);write_bit(59,0)
  write_bit(58,1)
  if read_byte(1)>0:
   if next((int(3*(abs(hash(str(hash(str(hash(str(sum([read_byte(x)for x in range(8)]))))+str(i+1)))))%10**13)/10**13)for i in range(2**6)))==0 and read_bit(57)==0 and read_bit(60)==1:
    write_bit(57,1);write_byte(255,1)if read_byte(1)+2>255 else write_byte(read_byte(1)+2,1);print(f"\nEnemy heals!\nEnemy gains 2 health.\nEnemy has {read_byte(1)} health remaining!\n")
   else:
    write_bit(57,0);print("\nEnemy attacks!")
    if read_bit(63)==1:
     print(f"Enemy does {int(read_byte(0)/2)} damage!");write_byte(0,3)if read_byte(3)-int(read_byte(0)/2)<1 else write_byte(read_byte(3)-int(read_byte(0)/2),3)
    else:
     print(f"Enemy does {read_byte(0)} damage!");write_byte(0,3)if read_byte(3)-read_byte(0)<1 else write_byte(read_byte(3)-read_byte(0),3)
    print(f"You have {read_byte(3)} health remaining!\n");print("Nice.\n")if read_bit(61)==1 and(read_byte(3)==69 or read_byte(3)==169)else 0
   if read_byte(3)<1:
    print("SECRET ENDING\n\nOh! why hello there!\nit's me,\nthe creator of this game!\nI just wanted to personally congratulate you on getting this ending.\nEven after getting god-like powers, you still laid down your sword and let the world return to its balance.\nYou are amazing and have shown so much dedication and patience to this game and i commend you for that!\nNo matter what they are, you can achieve your dreams!\nDon't let anything stop you!\nAnyways it's my time to go now.\nWith all that said,\ngoodbye player!"if read_byte(2)==255 and read_byte(4)==255 and read_bit(61)==1 else"You die!");write_bit(62,1);break
def exp():
 write_byte(int(bin(int.from_bytes((input("Would you like to increase your max health or strength?\n: ")+" ").lower()[0].encode(),'big')),2),1)
 while read_byte(1).to_bytes((read_byte(1).bit_length()+7)//8,'big').decode()!="h"and read_byte(1).to_bytes((read_byte(1).bit_length()+7)//8,'big').decode()!="m"and read_byte(1).to_bytes((read_byte(1).bit_length()+7)//8,'big').decode()!="s":print("\x1B[2JInvalid option.\n");write_byte(int(bin(int.from_bytes((input("Would you like to increase your max health or strength?\n: ")+" ")[0].encode(),'big')),2),1)
 if read_byte(1).to_bytes((read_byte(1).bit_length()+7)//8,'big').decode()=="h"or read_byte(1).to_bytes((read_byte(1).bit_length()+7)//8,'big').decode()=="m":
  write_byte(read_byte(4)+1,4);print("\x1B[2JMax health increased by 1!")
 else:
  write_byte(read_byte(2)+1,2);print("\x1B[2JStrength increased by 1!")
def poti():
 write_byte(read_byte(4),3);print(f"\nYou found {read_byte(0)} potions!\n");write_byte(read_byte(5)+read_byte(0),5)
if(input("\x1B[2JHint, if you want to beat the game, only upgrade your strength by 1 and don't use any cheat codes!\n\nHint, you can perform any action with just its first letter!\n\n\nDo you have a secret code?\n: ")+" ").lower()[0]=="y":
 write_bit(63,1);write_bit(61,1)
else:
 write_bit(63,0);write_bit(61,0)
write_byte(0,6);write_bit(62,1);write_byte(1,5);write_bit(56,0)
if read_bit(63)==1:
 for c in input("\x1B[2JWhat is the code?\n: ")[:4].lower():
  write_byte(int(bin(int.from_bytes(c.encode(),'big')),2),read_byte(6));write_byte(read_byte(6)+1,6)
else:
 input('\x1B[2JPsst, one code is "poti"! (enter to continue)')
if read_bit(63)==1 and read_byte(6)!=0:
 if read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="2":
  if read_byte(6)==4:
   write_byte(2,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["2","l","v","l"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 elif read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="3":
  if read_byte(6)==4:
   write_byte(3,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["3","=","0","3"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 elif read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="e":
  if read_byte(6)==3:
   write_byte(4,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["e","x","p"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 elif read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="l":
  if read_byte(6)==4:
   write_byte(5,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["l","v","l","5"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 elif read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="t":
  if read_byte(6)==4:
   write_byte(255,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["t","n","t","y"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 elif read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="b":
  if read_byte(6)==4:
   write_byte(254,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["b","0","$","$"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 elif read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="p":
  if read_byte(6)==4:
   write_byte(253,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["p","o","t","i"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 elif read_byte(0).to_bytes((read_byte(0).bit_length()+7)//8,'big').decode()=="\x1b":
  if read_byte(6)==4:
   write_byte(251,5);write_bit(56,1)
   for i in range(read_byte(6)):
    if not read_byte(i).to_bytes((read_byte(i).bit_length()+7)//8,'big').decode()==["\x1b","[","a","\x1b"][i]:
     write_bit(62,0);write_byte(1,5);write_bit(56,0)
  else:
   write_bit(62,0)
 else:
  write_bit(62,0)
else:
 write_bit(62,0)
input("\x1B[2JInvalid code. (enter to continue)")if read_bit(62)==0 and read_bit(61)==1 else 0;print("\x1B[2J");print("Cheat enabled.\n")if read_bit(56)==1 else 0;write_byte(read_byte(5),0);write_bit(62,0);write_bit(61,0);write_byte(5,4);write_byte(2,2);write_byte(2,5)
if read_byte(0)==255:
 write_byte(1,0);write_byte(20,4);write_byte(20,2)
if read_byte(0)==254:
 write_byte(5,0);write_byte(20,4);write_byte(20,2)
if read_byte(0)==253:
 write_byte(1,0);write_byte(100,5)
if read_byte(0)==251:
 write_bit(56,0);write_byte(5,0);write_byte(255,4);write_byte(255,2);write_byte(255,5);write_bit(61,1)
write_byte(read_byte(4),3)
if read_byte(0)==1:
 input(f"Level {read_byte(0)}! (enter to continue)");write_byte(2,0);write_byte(5,1);print("\x1B[2JYou encounter a small rodent!");level()
 if read_bit(62)==0:
  print("\x1B[2JThe rodent was defeated!\n");write_byte(2,0);exp();poti()
if read_byte(0)==2 and read_bit(62)==0:
 input(f"Level {read_byte(0)}! (enter to continue)");write_byte(3,0);write_byte(4,1);print("\x1B[2JYou encounter a evil ghoul!");level()
 if read_bit(62)==0:
  print("\x1B[2JThe ghoul was defeated!\n");write_byte(3,0);exp();poti()
if read_byte(0)==3 and read_bit(62)==0:
 input(f"Level {read_byte(0)}! (enter to continue)");write_byte(2,0);write_byte(10,1);print("\x1B[2JYou encounter an evil lake monster!");level()
 if read_bit(62)==0:
  print("\x1B[2JThe lake monster was defeated!\n");write_byte(4,0);exp();poti()
if read_byte(0)==4 and read_bit(62)==0:
 input(f"Level {read_byte(0)}! (enter to continue)");print("\x1B[2JYou find an XP orb!\n");write_byte(5,0);exp()
if read_byte(0)==5 and read_bit(62)==0:
 input("\nBOSS (enter to continue)");print("\nYou encounter a massive evil duck!");write_byte(3,0);write_byte(20,1);level()
print("\x1B[2JGreat, now try beat it without cheats!\n"if read_bit(56)==1 and read_bit(62)==0 else"\x1B[2JThe huge evil duck was defeated and peace was restored to the land!\n"if read_bit(62)==0 else"",end="");print("\nhttps://bit.ly/382Jahf")if read_byte(2)==255 and read_byte(4)==255 and read_byte(5)==0 else 0;print("\nhttps://bit.ly/3wcgAlt")if read_bit(61)==1 and(read_byte(5)==169 or read_byte(5)==69)and(read_byte(3)==169 or read_byte(3)==69)else 0;print("\nEND.\n")