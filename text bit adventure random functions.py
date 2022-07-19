def a(B=1,C=0):global A;A[C*8:C*8+8]=[0 if(B if B>0 else 0)&(1<<7-i)<1 else 1 for i in range(8)];return B
def b(C=60,D=0):global A;A[C]=D
def c(C=0):return int(''.join(map(str,A[C*8:C*8+8])),2)
def d():input(f"Level {c()}! (enter to continue)")
def e():
 a(c(4),3);A[58:61]=[0]*3;k(f"\nEnemy health is {c(1)}.")
 while c(1)>0:
  a(0,6)
  while(c(6),c(5))==(112,0)or not c(6)in[97,112,100]or(c(6),A[60]+A[59])==(97,2):k("\x1B[2JNo more potions!\n"if c(6)==112 else"\x1B[2JToo exausted.\n"if(c(6),A[60]+A[59])==(97,2)else str(k("\x1B[2JPlayer stats:\npotion amount:",c(5),"\ncurrent health:",c(3),"\nmax health:",c(4),"\nstrength:",c(2),"\n\nenemy stats:\nhealth:",c(1),"\nstrength:",c(),("\n\nNice."if c(5)in[69,169]or c(3)in[169,69]else"")))[:-4]if c(6)in[115,108]else"\x1B[2JInvalid action.\n"if c(6)!=0 else"");a(ord((input("Do you "+(""if A[60]+A[59]>1 else"attack, ")+"potion, defend or look at stats?\n: ")+" ").lower()[0]),6)
  if c(6)<98:k("\x1B[2JYou attack!\nYou do",c(2),f"damage!\nEnemy health is now {a(c(1)-c(2),1)}.");b(63);b(59 if A[60]>0 else 60,1)
  elif c(6)>111:
   if 5+c(3)>c(4):k("\x1B[2JYou restore",c(4)-c(3),"health!");a(c(4),3)
   else:k("\x1B[2JYou restore 5 health!");a(c(3)+5,3)
   k("You have",a(c(5)-1,5),"potion"+("s"if c(5)!=1 else""),"left!"+("\n\nNice."if c(5)in[69,169]else""));b(63);b();b(59)
  else:k("\x1B[2JYou defend!");b(63,1);b();b(59)
  if c(1)>0:
   if A[60]and not hash(str(A))%3+A[58]:b(58,1);k("\nEnemy heals!\nEnemy gains 2 health.\nEnemy has",a(c(1)+2,1),"health remaining!")
   else:
    b(58);k("\nEnemy attacks!")
    if A[63]>0:k("Enemy does",int(c()/2),"damage!");a(c(3)-int(c()/2),3)
    else:k("Enemy does",c(),"damage!");a(c(3)-c(),3)
    k("You have",c(3),"health remaining!"+("\n\nNice."if c(3)in[69,169]else""))
   if c(3)<1:k("SECRET ENDING\n\nOh! why hello there!\nIt's me,\nthe creator of this game!\nI just wanted to personally congratulate you on getting this ending.\nEven after getting god-like powers, you still laid down your sword and let the world return to its balance.\nYou are amazing and have shown so much dedication and patience to this game and i commend you for that!\nNo matter what they are, you can achieve your dreams!\nDon't let anything stop you!\nAnyways it's my time to go now.\nWith all that said,\ngoodbye player!"if(c(4),A[61])==(255,1)else"You die!");b(62);break
def f():
 while c(1)!=104 and c(1)!=109 and c(1)!=115:a(ord((input(("\x1B[2JInvalid option.\n\n"if c(1)!=0 else"")+"Would you like to increase your max health or strength?\n: ")+" ").lower()[0]),1)
 if c(1)in[104,109]:a(c(4)+1,4);k("\x1B[2JMax health increased by 1!")
 else:a(c(2)+1,2);k("\x1B[2JStrength increased by 1!")
def g():k("\nYou found",c(),"potions!\n");a(c(5)+c(),5)
def h():k("\x1B[2JYou encounter a",end="")
def j():k("\x1B[2JThe ",end="")
def k(S):print(S)
A=[0]*64;a()
if input("\x1B[2JHint, if you want to beat the game, upgrade your health by at least 2 and don't use any cheat codes!\n\nHint, you can perform any action with just its first letter!\n\n\nDo you have a secret code?\n: ").lower()[:1]=="y":
 for i in input("\x1B[2JWhat is the code?\n: ")[:4].lower():a(ord(i),c(6));a(c(6)+1,6)
 a(2 if[c(i)for i in range(4)]==[50,108,118,108]else 3 if[c(i)for i in range(4)]==[51,61,48,51]else 4 if[c(i)for i in range(3)]==[101,120,112]else 5 if[c(i)for i in range(4)]==[108,118,108,53]else 9 if[c(i)for i in range(4)]==[116,110,116,121]else 8 if[c(i)for i in range(4)]==[98,48,36,36]else 7 if[c(i)for i in range(4)]==[112,111,116,105]else 6 if[c(i)for i in range(4)]==[27,91,97,27]else 1)
 if c()<2:input("\x1B[2JInvalid code. (enter to continue)");k("\x1B[2J")
 else:b(56,1);k("\x1B[2JCheat enabled.\n")
else:input('\x1B[2JPsst, one code is "poti"! (enter to continue)');k("\x1B[2J")
a(5,4);a(2,2);a(2,5);b(62,1)
if c()>8:a();a(20,4);a(20,2);a(20,5)
if c()>7:a(5);a(20,2)
if c()>6:a();a(100,5)
if c()>5:b(56);a(5);a(255,4);a(255,2);a(255,5);b(61,1)
if c()<2:a(5,1);d();a(2);h();k(" small rodent!");e()
if c()==2 and A[62]:j();k("rodent was defeated!\n");f();g();d();a(3);a(4,1);h();k("n evil ghoul!");e()
if c()==3 and A[62]:j();k("ghoul was defeated!\n");f();g();d();a(2);a(10,1);h();k("n evil lake monster!");e();a(4)
if c()==4 and A[62]:j();k("lake monster was defeated!\n");f();g();d();k("\x1B[2JYou find an XP orb!\n");a(5);a(0,1);f()
if c()>4:input("\nBOSS (enter to continue)");h();k(" massive evil duck!");a(3);a(20,1);e()
k("\x1B[2JGreat, now try beat it without cheats!\n"if A[56]and A[62]else"\x1B[2JThe huge evil duck was defeated and peace was restored to the land!\n"if A[62]>0 else"","\nhttps://u.nu/jBjgR\n"if(c(2),c(4),c(5))==(255,255,0)else"\nhttps://u.nu/xmQTa\n"if A[61]and c(5)in[169,69]and c(3)in[169,69]else"","\nEND.\n")
pass