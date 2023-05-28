import random as r
nump = r.randint(10,99)
print(nump)
num = int(input("enter a two digit number"))
while num!=10:
    nump1 = nump
    c = 0
    while num%10!=0:
        numpr = nump1%10
        numr = num%10
        numpq = nump1//10
        numq = num//10
        if numpr == numr:
            c = c+1
    if c==2:
        print("you have guessed it correctly")
        break
    else:
        print("you have guessed %d right" %c)
        num = int(input("enter a two digit number"))
else:
    print("you quit the game")
