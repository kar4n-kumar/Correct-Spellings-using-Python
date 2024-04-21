import random


"""
QN:ROCK PAPER SCISSOR GAME
Winning Rules as follows:
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.

"""

print("welcome to  rock paper scissor")
print("1.Rock\n2.Paper\n3.Scissor")
points={"bot":0,"user":0}
def fub():
    points = {'user': 0, 'bot': 0}

    while True:
        choices=["rock",'paper','scissor']
        inpt1= input("Enter the answer : ")
        inpt=inpt1.lower()


        if inpt not in choices:
            print("Invalid input")
            continue

        random1 = random.choice(choices)
        print("Bot choice:", random1)

        if (inpt1 == random1):
            print("Retake")
        elif (inpt =='rock' and random1 =='scissor') or (inpt =='paper' and random1=='rock') or (inpt =='scissor' and random1 =='paper'):
            print("User won")
            points['user'] += 1
        else:
            print("Bot won")
            points['bot'] += 1

        print("Points:", points)

        if points['user'] == 3 or points['bot'] == 3:
            print("Game over!")
            print(points)
            exit()

fub()
