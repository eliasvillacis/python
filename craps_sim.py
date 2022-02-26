import random

shooter = 1 
on = 0 
wallet = 100
bet = 10
diceroll = 0

# As long as wallet is not zero time to play
while wallet > 0:
    d = (random.randrange(0, 6) + 1)
    d2 = (random.randrange(0, 6) + 1)
    dt = d + d2
    diceroll += 1
    print("Dice: ",dt, " Dice roll: ", diceroll)
    
    # Check if we have natural win or craps other wise set on
    if shooter == 1:
        if(dt == 7 or dt == 11):
            shooter = 1 
            wallet = wallet + (bet * 1.0)
            print("Win natural ", wallet)
        elif(dt == 2 or dt == 3 or dt == 12):
            shooter = 1 
            wallet = wallet + (bet * -1.0)
            print("Craps ", wallet)
        else:
            shooter = 2 
            on = dt
            print("on")
    # Check if we hit the on value or get craps otherwise keep rolling
    else:
        if(dt == 7 or dt == 11):
            shooter = 1 
            wallet = wallet - (bet * 1.0)
            print("on loser ", wallet)
        elif(dt==on):
            wallet = wallet + (bet * 1.0)
            print("on win ", wallet)
        else:
            print("free throw")
