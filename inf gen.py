alive=1
level=1
potion_amount=hash(" ")%4+3 #max is 6
potion_effectiveness=hash(" ")%2+2 #max is 3
health=hash(" ")%5+4 #max is 8
strength=hash(" ")%3+2 #max is 4
while alive==1:
 current_health=health
 enemy_health=hash(str(level))%6+level #max is level + 5
 print("\x1B[2Jlevel",level,"\nseed is",hash(str(level)))
 print("enemy health is",enemy_health)
 print("enemy strength is",hash(str(level))%5+level) #max is level + 4
 print("your health is",health)
 print("your strength is",strength)
 print("potion amount is",potion_amount)
 print("potion effectiveness is",potion_effectiveness,"\n")
 while enemy_health>0 and alive==1:
  action=""
  while not action in["a","p","d"] or action=="p"and potion_amount==0:
   action=input("actions are attack, potion and defend: ")[:1]
  if action=="p":
   current_health+=potion_effectiveness
  if action=="a":
   enemy_health-=strength
  if action=="d":
   current_health-=(hash(str(level))%5+level)/2
  else:
   if enemy_health>0:
    current_health-=hash(str(level))%5+level
  if current_health<=0:
   alive=0
  print("\x1B[2Jenemy health is",enemy_health)
  print("your health is",current_health,"\n")
 if alive==1:
  level+=1
  potion_amount+=level
  upgrade=""
  while not upgrade in["1","2","3"]:
   upgrade=input("what would you like to upgrade?\n1=health\n2=strength\n3=potion effectiveness\n: ")
  if upgrade=="1":
   health+=1
  if upgrade=="2":
   strength+=1
  if upgrade=="3":
   potion_effectiveness+=1