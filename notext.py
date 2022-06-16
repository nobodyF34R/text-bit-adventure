def a(B=1,C=0):global A;A=[int(X)for Y in[list(7*"0"+bin(B)[2:])[-8:]if i==C else A[i*8:i*8+8]for i in range(8)]for X in Y]
def b(C=60,D=0):global A;A=[(0 if D!=1 else 1)if i==C else A[i]for i in range(64)]
def c(C=0):return int(''.join([str(A[i+8*C])for i in range(8)]),2)
def d():input()
def e():
 a(c(4),3);b(57);b(59);b()
 while c(1)>0:
  a(0,6)
  while(c(6),c(5))==(112,0)or not c(6)in[97,112,100]or(c(6),A[60]+A[59])==(97,2):a(ord((input()+" ").lower()[0]),6)
  if c(6)==97:a(0 if c(1)-c(2)<1 else c(1)-c(2),1);b(63);b(59 if A[60]==1 else 60,1)
  elif c(6)==112:
   if 5+c(3)>c(4):a(c(4),3)
   else:a(c(3)+5,3)
   a(c(5)-1,5);b(63);b();b(59)
  else:b(63,1);b();b(59)
  if c(1)>0:
   if(hash(str(A))%3,A[57],A[60])==(0,0,1):b(57,1);a(255 if c(1)+2>255 else c(1)+2,1)
   else:
    b(57)
    if A[63]==1:a(0 if c(3)-int(c()/2)<1 else c(3)-int(c()/2),3)
    else:a(0 if c(3)-c()<1 else c(3)-c(),3)
   if c(3)<1:b(62,1);break
def f():
 while c(1)!=104 and c(1)!=109 and c(1)!=115:a(ord((input()+" ").lower()[0]),1)
 if c(1)in[104,109]:a(c(4)+1,4)
 else:a(c(2)+1,2)
A=[0]*64;a()
if input().lower()[:1]=="y":
 input();input()
else:input()
a(5,4);a(2,2);a(2,5)
if c()==1:a(5,1);d();a(2);e()
if(c(),A[62])==(2,0):f();d();a(3);a(4,1);e()
if(c(),A[62])==(3,0):f();d();a(2);a(10,1);e();a(4)
if(c(),A[62])==(4,0):f();d();a(5);f()
if c()==5:input();a(3);a(20,1);e()