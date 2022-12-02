#number guessing game Jared Law and Kyle Kehoe
#imports
import random

#Functions
def intro():
      print(
          """Welcome to our game! There are three basic modes: Easy, Hard, and Computer Guess.
          

      Easy mode gives you unlimited guess for a number that the computer chooses.
      Hard mode only allows you 7 guesses
      Swap allows you to choose a secrent number that the computer has to guess.
      
      Enter 'easy', 'hard' or 'swap' for the game you want. Enter quit to exit""")


def guess_correct(score, total):
    print('''                Congratulations!
            That is the correct number!
                    You win!''')
    print('Your score is' , score)
    print('your guesses were' , total)

def guess_low(total):
    print('\nYour guess was too low.')
    print('Your guesses were', total)

def guess_high(total):
    print('\nYour guess was too high.')
    print('Your guesses were', total)

def loss(total, secretNum):
    print('\nYou ran out of guesses! Too Bad!')
    print('Your guesses were ', total)
    print('The answer was ', secretNum)

def userSelectedNum(x,y):
    secretNumber=random.randint(x,y)
    return(secretNumber)

def Compsearch():
    Game=1
    feedback=0
    choice=0
    low=1
    mid=0
    high=100
    while Game>0:
        mid=int((low+high)//2)
        print('Is your number:' , mid)
        feedback=input('please enter your feedback: Low/High/Correct/Quit')
        if feedback.upper()=='LOW':
            low=mid+1
        elif feedback.upper()=='HIGH':
            high=mid-1
        elif feedback.upper()=='CORRECT':
            print('Launch codes confirmed. Thank you Mr.President')
            Game=-1
        elif feedback.upper()=='QUIT':
            Game=-1
            return -1

def guessCheckerBoss(y):
    total = []
    score = 100
    lim = False
    Guess = 0
    counter = 0
    while lim==False:       
        counter += 1
        if counter < 8:
            try:
                Guess=int(input('What is your guess?'))
            except ValueError:
                 return(-1)
            total.append(Guess)
            if Guess==y:
                guess_correct(score, total)
                lim=True
                return(-1)
            elif Guess<y:
                guess_low(total)
                score-=10
                #counter+=1
            elif Guess>y:
                guess_high(total)
                score-=10
                #counter+=1
        else:
            loss(total, secretNum)
            return(-1)

def guessCheckerEasy(y):
    total=[]
    score=100
    lim=False
    Guess=0
    counter=1
    while lim==False:
        try:
            Guess=int(input('What is your guess?'))
        except ValueError:
             return(-1)
        total.append(Guess)
        if Guess==y:
            print('''                Congratulations!
            That is the correct number!
                    You win!''')
            print('Your score is' , score)
            print('your guesses were' , total)
            lim=True
            return(-1)
        elif Guess<y:
            guess_low(total)
            score-=10
            counter+=1
        elif Guess>y:
            guess_high(total)
            score-=10
            counter+=1

#Global Variables
secretNum=0
Game=1
on=True
name=0
secretNumber=0
lowerBound=0
upperBound=0
choice=0
numSel=0


#Main
name=input('Hello there. What is your name?')
print('Hello' , name)
while on == True:
    Game=1
    intro()
    choice=input('Please enter easy,hard,swap, or quit')
    if choice.upper() == 'EASY':
        print('Welcome to the most basic version of our game! You have an unlimited number of guesses to guess the correct number')
        numSel=input('would you like to choose your custom range of numbers, or simply go with the default 1-100? (type custom or default)')
        if numSel.upper()=='CUSTOM':
            try:   
                print('you have chosen to select your own range of numbers')
                lowerBound=int(input('Please select the lower number'))
                upperBound=int(input('Please select the upper number'))
            except ValueError:
                break
            secretNum=userSelectedNum(lowerBound,upperBound)
        elif numSel.upper()=='DEFAULT':
            secretNum=random.randint(1,100)
        while Game>0:
            Game=guessCheckerEasy(secretNum)
            choice=0
    elif choice.upper() == 'HARD':
        print('Welcome to the most insanely difficult game you will ever play!')
        numSel=input('would you like to choose your custom range of numbers, or simply go with the default 1-100? (type custom or default)')
        if numSel.upper()=='CUSTOM':
            try:   
                print('you have chosen to select your own range of numbers')
                lowerBound=int(input('Please select the lower number'))
                upperBound=int(input('Please select the upper number'))
            except ValueError:
                break
            secretNum=userSelectedNum(lowerBound,upperBound)
        elif numSel.upper()=='DEFAULT':
            secretNum=random.randint(1,100)
        while Game>0:
            Game=guessCheckerBoss(secretNum)
            choice=0
    elif choice.upper() == 'SWAP':
        Compsearch()
        choice=0
    elif choice.upper() == 'QUIT':
        on=False
    else:
        print('sorry that is not a valid input')
        choice=0
