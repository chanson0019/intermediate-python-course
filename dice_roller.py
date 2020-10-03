import random

def main():
    diceRolls = int(input('How many dice would you like to roll? '))
    diceSize = int(input('How many sides are the dice? '))
    diceSum = 0
    for i in range(0,diceRolls):

        roll = random.randint(1,diceSize)
        diceSum = diceSum + roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Failure')
        elif roll == diceSize:
            print(f'You called a {roll}! Critical Success!')
        else:
            print(f'You rolled a {roll}')
    print(f'You have roled a total of {diceSum}')

if __name__== "__main__":
    main()
