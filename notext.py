def a(B=1,C=0):global A;A[C*8:C*8+8]=[0 if(B if B>0 else 0)&(1<<7-i)<1 else 1 for i in range(8)];return B
def b(C=60,D=0):global A;A[C]=D
def c(C=0):return int(''.join(map(str,A[C*8:C*8+8])),2)
def d():input("")
def e():
 a(c(4),3);A[58:61]=[0]*3;print("")
 while c(1)>0:
  a(0,6)
  while(c(6),c(5))==(112,0)or not c(6)in[97,112,100]or(c(6),A[60]+A[59])==(97,2):print(""if c(6)==112 else""if(c(6),A[60]+A[59])==(97,2)else str(print("",c(),(""if c(5)in[69,169]or c(3)in[169,69]else"")))[:-4]if c(6)in[115,108]else""if c(6)!=0 else"");a(ord((input(""+(""if A[60]+A[59]>1 else"")+"")+" ").lower()[0]),6)
  if c(6)<98:print("");b(63);b(59 if A[60]>0 else 60,1)
  elif c(6)>111:
   if 5+c(3)>c(4):print("");a(c(4),3)
   else:print("");a(c(3)+5,3)
   print(""+(""if c(5)in[69,169]else""));b(63);b();b(59)
  else:print("");b(63,1);b();b(59)
  if c(1)>0:
   if A[60]and not hash(str(A))%3+A[58]:b(58,1);print("")
   else:
    b(58);print("")
    if A[63]>0:print("");a(c(3)-int(c()/2),3)
    else:print("");a(c(3)-c(),3)
    print(""+(""if c(3)in[69,169]else""))
   if c(3)<1:print(""if(c(4),A[61])==(255,1)else"");b(62);break
def f():
 while c(1)!=104 and c(1)!=109 and c(1)!=115:a(ord((input((""if c(1)!=0 else"")+"")+" ").lower()[0]),1)
 if c(1)in[104,109]:a(c(4)+1,4);print("")
 else:a(c(2)+1,2);print("")
def g():print("");a(c(5)+c(),5)
def h():print("",end="")
def j():print("",end="")
A=[0]*64;a()
if input("").lower()[:1]=="y":
 for i in input("")[:4].lower():a(ord(i),c(6));a(c(6)+1,6)
 a(1)
 if c()<2:input("");print("")
 else:b(56,1);print("")
else:input('');print("")
a(5,4);a(2,2);a(2,5);b(62,1)
if c()>8:a();a(20,4);a(20,2);a(20,5)
if c()>7:a(5);a(20,2)
if c()>6:a();a(100,5)
if c()>5:b(56);a(5);a(255,4);a(255,2);a(255,5);b(61,1)
if c()<2:a(5,1);d();a(2);h();print("");e()
if c()==2 and A[62]:j();print("");f();g();d();a(3);a(4,1);h();print("");e()
if c()==3 and A[62]:j();print("");f();g();d();a(2);a(10,1);h();print("");e();a(4)
if c()==4 and A[62]:j();print("");f();g();d();print("");a(5);a(0,1);f()
if c()>4:input("");h();print("");a(3);a(20,1);e()
print(""if A[56]and A[62]else""if A[62]>0 else"",""if(c(2),c(4),c(5))==(255,255,0)else""if A[61]and c(5)in[169,69]and c(3)in[169,69]else"","")