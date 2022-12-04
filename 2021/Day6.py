creatures = sorted(list(map(int,open("input6.txt", "r").read().split(","))))

print(len(creatures))

#D = [[i, creatures.count(str(i))] for i in range(9)]

D = {}

for i in creatures:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1

for i in range(9):
    if i not in D:
        D[i] = 0

#print(D)

prev_D = D

days = 256

for day in range(days):
    #print({key:D[key] for key in sorted(D.keys())})
    prev_D = D.copy()
    for i in range(8):
        if i == 0:
            D[8] = prev_D[0]
            D[6] = prev_D[7] + prev_D[0]
            D[0] = prev_D[1]
        elif i != 6:
            
            D[i] = prev_D[i+1] 
        
#for some reason I don't understand prev_D is updating before I need it to    
#changed prev_D

print({key:D[key] for key in sorted(D.keys())})




"""for day in range(80):
    for i in range(9):
        if i != 0:
            update_D[i-1] = D[i]
        else:
            print(i)
            update_D[6] += D[0]
            update_D[8] = D[0]
        print(update_D)

    D = update_D
    print(D)"""   

    

print(sum(D.values()))
            
        


"""for i in range(days):
    if 0 not in creatures:
        creatures = list(map(lambda x: x-1,creatures))
    else:
        current_creatures = map(lambda x: x-1, creatures)
        #print("1")
        current_creatures = [x if x != -1 else 6 for x in current_creatures] #8 has been changed for a 6
        #print("2")
        current_creatures.extend([6]*creatures.count(0))
        #print("3")
        creatures = current_creatures
    #print(i)
print(len(creatures))"""

#ineficient for big numbers as it is exponential


"""t = 0

for i in range(1,6):
    t += D[i]*pow(2, (days-i)//6)
    
print(t/2)"""



