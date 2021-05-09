trigger = False

for i in range(1, 332 + 1):
    if(trigger == True):
        break
    for j in range(1, 499 + 1):
        c = 1000 - (i + j)
        
        if((i + j + c == 1000) and (i**2 + j**2 == c**2)):
            print(i * j * c)
            trigger = True
            break
