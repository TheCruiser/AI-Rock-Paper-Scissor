import random
print("                      Rock Paper Scissor                   ")
print("Your AI Partner is Elisa ;)")
player = input("Make your move : ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'
print(f"Elisa played {computer}")

if player==computer:
    print("it's a tie")
elif player=='rock':
    if(computer=="scissors"):
        print("you won")
    elif(computer=="paper"):
        print("Elisa won")
elif player=='paper':
    if(computer=="scissors"):
        print("Elisa won")
    elif(computer=="rock"):
        print("you won")
elif player=='scissors':
    if(computer=="rock"):
        print("Elisa won")
    elif(computer=="paper"):
        print("You won")
else:
    print("something went wrong")