w = 0
l = 0
t = 0

while (t < 5) and (w < 3) and (l < 3):
    wt = str(w)
    lt = str(l)
    print("\ncurrent result: " + wt + ":" + lt)
    
    import random
    computer = random.randint(1,3)
    computer = int(computer)

    if computer == 1:
        com = "scissor"

    elif computer == 2:
        com = "papper"

    elif computer == 3:
        com = "stone"


    my = input("Input scissor,papper or stone. Or input end to exit the game:")
    op = ["scissor", "papper", "stone"]
    if (my not in op) and (my != "end"):
        print("Error!!Please input your option again.")
        continue
    elif my == "end":
        print("Goodbye!!")
        break
    elif my == com:
        print("you and computer: " + com)
        print("Deuce!!")
        continue
    elif (my == "scissor" and com == "papper") or (my == "papper" and com == "stone") or (my == "stone" and com == "scissor"):
        print("you: " + my + " vs computer: " + com)
        print("You win in this round.")
        t += 1
        w += 1
        continue
    elif (com == "scissor" and my == "papper") or (com == "papper" and my == "stone") or (com == "stone" and my == "scissor"):
        print("you: " + my + " vs computer: " + com)
        print("You lose in this round.")
        t += 1
        l += 1
        continue
        
if w > l:
    print("You win!!")
elif w < l:
    print("You have failed in this game....")

