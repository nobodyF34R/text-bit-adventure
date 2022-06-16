alive=1
level=1
health=hash(" ")%5+4 #max is 8
strength = hash(" ")%3+2 #max is 4
while alive==1:
    current_health=health
    print("level",level,"\nseed is",hash(str(level)))
    print("enemy health is",hash(str(level))%6+level) #max is level + 5
    print("enemy strength is",hash(str(level))%5+level) #max is level + 4
    print("your health is",health)
    print("your strength is",strength)
    break
