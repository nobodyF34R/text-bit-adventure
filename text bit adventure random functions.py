def a(B=1,C=0):global A;A=[int(X)for Y in[list(7*"0"+bin(B)[2:])[-8:]if i==C else A[i*8:i*8+8]for i in range(8)]for X in Y]
def b(C=60,D=0):global A;A=[(0 if D!=1 else 1)if i==C else A[i]for i in range(64)]
def c(C=0):return int(''.join([str(A[i+8*C])for i in range(8)]),2)
def d():input(f"Level {c()}! (enter to continue)")
def e():
 a(c(4),3);b(57);b(59);b();print(f"\nEnemy health is {c(1)}.\n")
 while c(1)>0:
  a(ord((input("Do you potion, defend or look at stats?\n: "if A[60]==1 and A[59]==1 else"Do you attack, potion, defend or look at stats?\n: ")+" ").lower()[0]),6)
  while c(6)==112 and c(5)==0 or c(6)!=97 and c(6)!=112 and c(6)!=100 or c(6)==97 and A[60]==1 and A[59]==1:print("\x1B[2JNo more potions!\n")if c(6)==112 else print("\x1B[2JToo exausted.\n")if c(6)==97 and A[60]==1 and A[59]==1 else print(f"\x1B[2JPlayer stats:\npotion amount: {c(5)}\ncurrent health: {c(3)}\nmax health: {c(4)}\nstrength: {c(2)}\n\nenemy stats:\nhealth: {c(1)}\nstrength: {c()}\n"+("\nNice.\n"if c(5)==69 or c(3)==69 or c(5)==169 or c(3)==169 else""))if c(6)==115 or c(6)==108 else print("\x1B[2JInvalid action.\n");a(ord((input("Do you potion, defend or look at stats?\n: "if A[60]==1 and A[59]==1 else"Do you attack, potion, defend or look at stats?\n: ")+" ").lower()[0]),6)
  if c(6)==97:print("\x1B[2JYou attack!\nYou do",c(2),"damage!");a(0 if c(1)-c(2)<1 else c(1)-c(2),1);print(f"Enemy health is now {c(1)}.");b(63);b(59 if A[60]==1 else 60,1)
  elif c(6)==112:
   if 5+c(3)>c(4):print("\x1B[2JYou restore",c(4)-c(3),"health!");a(c(4),3)
   else:print("\x1B[2JYou restore 5 health!");a(c(3)+5,3)
   a(c(5)-1,5);print("You have 1 potion left!"if c(5)==1 else "You have"+c(5)+"potions left!"+("\n\nNice."if c(5)==69 or c(5)==169 else""));b(63);b();b(59)
  else:print("\x1B[2JYou defend!");b(63,1);b();b(59)
  if c(1)>0:
   if hash(str(A))%3==0 and A[57]==0 and A[60]==1:b(57,1);a(255 if c(1)+2>255 else c(1)+2,1);print("\nEnemy heals!\nEnemy gains 2 health.\nEnemy has",c(1),"health remaining!\n")
   else:
    b(57);print("\nEnemy attacks!")
    if A[63]==1:print("Enemy does",int(c()/2),"damage!");a(0 if c(3)-int(c()/2)<1 else c(3)-int(c()/2),3)
    else:print("Enemy does",c(),"damage!");a(0 if c(3)-c()<1 else c(3)-c(),3)
    print("You have",c(3),"health remaining!\n"+("\nNice.\n"if c(3)==69 or c(3)==169 else""))
   if c(3)<1:print("SECRET ENDING\n\nOh! why hello there!\nIt's me,\nthe creator of this game!\nI just wanted to personally congratulate you on getting this ending.\nEven after getting god-like powers, you still laid down your sword and let the world return to its balance.\nYou are amazing and have shown so much dedication and patience to this game and i commend you for that!\nNo matter what they are, you can achieve your dreams!\nDon't let anything stop you!\nAnyways it's my time to go now.\nWith all that said,\ngoodbye player!"if c(2)==255 and c(4)==255 and A[61]==1 else"You die!");b(62,1);break
def f():
 a(ord((input("Would you like to increase your max health or strength?\n: ")+" ").lower()[0]),1)
 while c(1)!=104 and c(1)!=109 and c(1)!=115:print("\x1B[2JInvalid option.\n");a(ord((input("Would you like to increase your max health or strength?\n: ")+" ").lower()[0]),1)
 if c(1)==104 or c(1)==109:a(c(4)+1,4);print("\x1B[2JMax health increased by 1!")
 else:a(c(2)+1,2);print("\x1B[2JStrength increased by 1!")
def g():print("\nYou found",c(),"potions!\n");a(c(5)+c(),5)
def h():print("\x1B[2JYou encounter a",end="")
def j():print("\x1B[2JThe ",end="")
A=[0]*64;a()
if input("\x1B[2JHint, if you want to beat the game, upgrade your health by at least 2 and don't use any cheat codes!\n\nHint, you can perform any action with just its first letter!\n\n\nDo you have a secret code?\n: ").lower()[:1]=="y":
 for i in input("\x1B[2JWhat is the code?\n: ")[:4].lower():a(ord(i),c(6));a(c(6)+1,6)
 a(2 if[c(i)for i in range(4)]==[50,108,118,108]else 3 if[c(i)for i in range(4)]==[51,61,48,51]else 4 if[c(i)for i in range(3)]==[101,120,112]else 5 if[c(i)for i in range(4)]==[108,118,108,53]else 9 if[c(i)for i in range(4)]==[116,110,116,121]else 8 if[c(i)for i in range(4)]==[98,48,36,36]else 7 if[c(i)for i in range(4)]==[112,111,116,105]else 6 if[c(i)for i in range(4)]==[27,91,97,27]else 1)
 if c()==1:input("\x1B[2JInvalid code. (enter to continue)");print("\x1B[2J")
 else:b(56,1);print("\x1B[2JCheat enabled.\n")
else:input('\x1B[2JPsst, one code is "poti"! (enter to continue)');print("\x1B[2J")
a(5,4);a(2,2);a(2,5)
if c()==9:a();a(20,4);a(20,2);a(20,5)
if c()==8:a(5);(20,2)
if c()==7:a();a(100,5)
if c()==6:b(56);a(5);a(255,4);a(255,2);a(255,5);b(61,1)
if c()==1:a(5,1);d();a(2);h();print(" small rodent!");e()
if c()==2 and A[62]==0:j();print("rodent was defeated!\n");f();g();d();a(3);a(4,1);h();print(" evil ghoul!");e()
if c()==3 and A[62]==0:j();print("ghoul was defeated!\n");f();g();d();a(2);a(10,1);h();print("n evil lake monster!");e();a(4)
if c()==4 and A[62]==0:j();print("lake monster was defeated!\n");f();g();d();print("\x1B[2JYou find an XP orb!\n");a(5);f()
if c()==5:input("\nBOSS (enter to continue)");h();print(" massive evil duck!");a(3);a(20,1);e()
print("\x1B[2JGreat, now try beat it without cheats!\n"if A[56]==1 and A[62]==0 else"\x1B[2JThe huge evil duck was defeated and peace was restored to the land!\n"if A[62]==0 else"",end="");print("\nhttps://bit.ly/382Jahf"if c(2)==255 and c(4)==255 and c(5)==0 else"\nhttps://bit.ly/3wcgAlt"if A[61]==1 and(c(5)==169 or c(5)==69)and(c(3)==169 or c(3)==69)else"",end="");print("\nEND.\n")