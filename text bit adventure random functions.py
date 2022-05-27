A=[]
def a(B,C):
 global A;F=[];[F.append(str(bin(B)[2:])[i-(8-len(str(bin(B)[2:])))])if 7-len(bin(B)[2:])<i else F.append(0)for i in range(8)];E=A;A=[]
 for i in range(8):
  for x in range(8):
   if not i==C:
    try:
     A.append(E[x+8*i])
    except:
     A.append(0)
   else:
    A.append(int(F[x]))
def b(C,D=3):
 global A;E=A;A=[]
 for i in range(64):
  if not i==C:
   try:
    A.append(E[i])
   except:
    A.append(0)
  else:
    A.append(0)if D!=True else A.append(1)
def c(C):
 global A;return int(''.join([str(A[i+8*C])for i in range(8)]),2)
def d(C):
 global A
 try:
  return A[C]
 except:
  return 0
def e():
 input(f"Level {c(0)}! (enter to continue)")
def f():
 b(57,0);b(59,0);b(60,0);print(f"Enemy health is {c(1)}.\n")
 while c(1)>0:
  a(int(bin(int.from_bytes((input("Do you potion, defend or look at stats?\n: "if d(60)==1 and d(59)==1 else"Do you attack, potion, defend or look at stats?\n: ")+" ").lower()[0].encode(),'big')),2),6)
  while(c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="p"and c(5)==0)or(c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()!="a"and c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()!="p"and c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()!="d")or(c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="a"and d(60)==1 and d(59)==1):print("\x1B[2JNo more potions!")if c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="p"else print("\x1B[2JToo exausted.")if(c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="a"and d(60)==1 and d(59)==1)else print(f"\x1B[2JPlayer stats:\npotion amount: {c(5)}\ncurrent health: {c(3)}\nmax health: {c(4)}\nstrength: {c(2)}\n\nenemy stats:\nhealth: {c(1)}\nstrength: {c(0)}\n")if(c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="s"or c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="l")else print("\x1B[2JInvalid action.");print("Nice.\n")if d(61)==1 and(c(5)==69 or c(3)==69 or c(5)==169 or c(3)==169)and(c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="s"or c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="l")else 0;a(int(bin(int.from_bytes((input("Do you potion, defend or look at stats?\n: "if d(60)==1 and d(59)==1 else"Do you attack, potion, defend or look at stats?\n: ")+" ").lower()[0].encode(),'big')),2),6)
  if c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="a":
   print(f"\x1B[2JYou attack!\nYou do {c(2)} damage!");a(0,1)if c(1)-c(2)<1 else a(c(1)-c(2),1);print(f"Enemy health is now {c(1)}.");b(63,0);b(59,1)if d(60)==1 else 0;b(60,1)if d(60)==0 else 0
  elif c(6).to_bytes((c(6).bit_length()+7)//8,'big').decode()=="p":
   if 5+c(3)>c(4):
    print(f"\x1B[2JYou restore {c(4)-c(3)} health!");a(c(4),3)
   else:
    print(f"\x1B[2JYou restore 5 health!");a(c(3)+5,3)
   a(c(5)-1,5);print(f"You have {c(5)} potion left!"if c(5)==1 else f"You have {c(5)} potions left!");b(63,0);b(60,0);b(59,0);print("Nice.")if c(5)==69 or c(5)==169 and d(61)==1 else 0
  else:
   print("\x1B[2JYou defend!");b(63,1);b(60,0);b(59,0)
  if c(1)>0:
   if next((int(3*(abs(hash(str(hash(str(hash(str(sum([c(x)for x in range(8)]))))+str(i+1)))))%10**13)/10**13)for i in range(2**6)))==0 and d(57)==0 and d(60)==1:
    b(57,1);a(255,1)if c(1)+2>255 else a(c(1)+2,1);print(f"\nEnemy heals!\nEnemy gains 2 health.\nEnemy has {c(1)} health remaining!\n")
   else:
    b(57,0);print("\nEnemy attacks!")
    if d(63)==1:
     print(f"Enemy does {int(c(0)/2)} damage!");a(0,3)if c(3)-int(c(0)/2)<1 else a(c(3)-int(c(0)/2),3)
    else:
     print(f"Enemy does {c(0)} damage!");a(0,3)if c(3)-c(0)<1 else a(c(3)-c(0),3)
    print(f"You have {c(3)} health remaining!\n");print("Nice.\n")if d(61)==1 and(c(3)==69 or c(3)==169)else 0
   if c(3)<1:
    print("SECRET ENDING\n\nOh! why hello there!\nit's me,\nthe creator of this game!\nI just wanted to personally congratulate you on getting this ending.\nEven after getting god-like powers, you still laid down your sword and let the world return to its balance.\nYou are amazing and have shown so much dedication and patience to this game and i commend you for that!\nNo matter what they are, you can achieve your dreams!\nDon't let anything stop you!\nAnyways it's my time to go now.\nWith all that said,\ngoodbye player!"if c(2)==255 and c(4)==255 and d(61)==1 else"You die!");b(62,1);break
def g():
 a(int(bin(int.from_bytes((input("Would you like to increase your max health or strength?\n: ")+" ").lower()[0].encode(),'big')),2),1)
 while c(1).to_bytes((c(1).bit_length()+7)//8,'big').decode()!="h"and c(1).to_bytes((c(1).bit_length()+7)//8,'big').decode()!="m"and c(1).to_bytes((c(1).bit_length()+7)//8,'big').decode()!="s":print("\x1B[2JInvalid option.\n");a(int(bin(int.from_bytes((input("Would you like to increase your max health or strength?\n: ")+" ")[0].encode(),'big')),2),1)
 if c(1).to_bytes((c(1).bit_length()+7)//8,'big').decode()=="h"or c(1).to_bytes((c(1).bit_length()+7)//8,'big').decode()=="m":
  a(c(4)+1,4);print("\x1B[2JMax health increased by 1!")
 else:
  a(c(2)+1,2);print("\x1B[2JStrength increased by 1!")
def h():
 a(c(4),3);print(f"\nYou found {c(0)} potions!\n");a(c(5)+c(0),5)
if(input("\x1B[2JHint, if you want to beat the game, upgrade your strength by 1 or 2 and don't use any cheat codes!\n\nHint, you can perform any action with just its first letter!\n\n\nDo you have a secret code?\n: ")+" ").lower()[0]=="y":
 b(63,1);b(61,1)
b(62,1);a(1,5)
if d(63)==1:
 for i in input("\x1B[2JWhat is the code?\n: ")[:4].lower():
  a(int(bin(int.from_bytes(i.encode(),'big')),2),c(6));a(c(6)+1,6)
else:
 input('\x1B[2JPsst, one code is "poti"! (enter to continue)')
if d(63)==1 and c(6)!=0:
 if c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="2":
  if c(6)==4:
   a(2,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["2","l","v","l"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 elif c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="3":
  if c(6)==4:
   a(3,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["3","=","0","3"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 elif c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="e":
  if c(6)==3:
   a(4,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["e","x","p"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 elif c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="l":
  if c(6)==4:
   a(5,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["l","v","l","5"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 elif c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="t":
  if c(6)==4:
   a(255,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["t","n","t","y"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 elif c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="b":
  if c(6)==4:
   a(254,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["b","0","$","$"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 elif c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="p":
  if c(6)==4:
   a(253,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["p","o","t","i"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 elif c(0).to_bytes((c(0).bit_length()+7)//8,'big').decode()=="\x1b":
  if c(6)==4:
   a(251,5);b(56,1)
   for i in range(c(6)):
    if not c(i).to_bytes((c(i).bit_length()+7)//8,'big').decode()==["\x1b","[","a","\x1b"][i]:
     b(62,0);a(1,5);b(56,0)
  else:
   b(62,0)
 else:
  b(62,0)
else:
 b(62,0)
input("\x1B[2JInvalid code. (enter to continue)")if d(62)==0 and d(61)==1 else 0;print("\x1B[2J");print("Cheat enabled.\n")if d(56)==1 else 0;a(c(5),0);b(62,0);b(61,0);a(5,4);a(2,2);a(2,5)
if c(0)==255:
 a(1,0);a(20,4);a(20,2)
if c(0)==254:
 a(5,0);a(20,4);a(20,2)
if c(0)==253:
 a(1,0);a(100,5)
if c(0)==251:
 b(56,0);a(5,0);a(255,4);a(255,2);a(255,5);b(61,1)
a(c(4),3)
if c(0)==1:
 e();a(2,0);a(5,1);print("\x1B[2JYou encounter a small rodent!\n");f()
 if d(62)==0:
  print("\x1B[2JThe rodent was defeated!\n");a(2,0);g();h()
if c(0)==2 and d(62)==0:
 e();a(3,0);a(4,1);print("\x1B[2JYou encounter a evil ghoul!\n");f()
 if d(62)==0:
  print("\x1B[2JThe ghoul was defeated!\n");a(3,0);g();h()
if c(0)==3 and d(62)==0:
 e();a(2,0);a(10,1);print("\x1B[2JYou encounter an evil lake monster!\n");f()
 if d(62)==0:
  print("\x1B[2JThe lake monster was defeated!\n");a(4,0);g();h()
if c(0)==4 and d(62)==0:
 e();print("\x1B[2JYou find an XP orb!\n");a(5,0);g()
if c(0)==5 and d(62)==0:
 input("\nBOSS (enter to continue)");print("\x1B[2JYou encounter a massive evil duck!\n");a(3,0);a(20,1);f()
print("\x1B[2JGreat, now try beat it without cheats!\n"if d(56)==1 and d(62)==0 else"\x1B[2JThe huge evil duck was defeated and peace was restored to the land!\n"if d(62)==0 else"",end="");print("\nhttps://bit.ly/382Jahf")if c(2)==255 and c(4)==255 and c(5)==0 else 0;print("\nhttps://bit.ly/3wcgAlt")if d(61)==1 and(c(5)==169 or c(5)==69)and(c(3)==169 or c(3)==69)else 0;print("\nEND.\n")