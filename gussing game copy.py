from sys import *        
setExecutionLimit(500000)
import random

def game():
    t = 0
    c = int(raw_input("Which mode do you want to play? \n1.Easy(10) \n2.Medium(15) \n3.Hard(30) \nPlease choose a level"))
    n = 1
    if c == 1:
        n = n+10
    elif c== 2:
        n =n+15
    elif c == 3:
        n = n+30
    a = int(raw_input("Please type in a number"))
    b = random.randrange(1, n)

    while a!=b:
        if a < b:
            a = int(raw_input("Higher"))
            t = t +1
        elif a > b:
            a = int(raw_input("Lower"))
            t = t + 1
    if a == b:
        raw_input("Great! You got it!!! ")
        t = t + 1
        raw_input("You have tried "+ str(t) + " times.")
        return t

def playagain():
    c = int(raw_input("Do you want to play again? \n1.Yes \n2.No"))
    if c ==2:
        raw_input("Thank you for playing it!!!")
    if c == 1:
        game()

def main():
    d = int(raw_input("Welcome to the Guessing Game!!! \nHow many players do you have? \n1. 1 player \n2. 2 players(1 round)\n3. 2 players(3 rounds)\n4. 2 players(betting system)"))
    if d ==1:
        game()
        playagain()
    if d ==2:
        raw_input("\nFirst player's turn!")
        r1 = game()
        raw_input("\nSecond player's turn!")
        r2 = game()
        if r1 < r2:
            raw_input("\nFirst player wins!")
        if r1 >r2:
            raw_input("\nSecond player wins!")
        if r1 == r2:
            print("\nA draw!")
        playagain()
    if d ==3:
        p1 = 0
        p2 = 0
        for i in range(3):
            raw_input("\nFirst player's turn!")
            r1 = game()
            raw_input("\nSecond player's turn!")
            r2 = game()
            if r1 < r2:
                raw_input("\nFirst player wins in this round")
                p1 = p1 + 1
            if r1 > r2:
                raw_input("\nSecond player wins in this round")
                p2 = p2 +1
            if r1 == r2:
                raw_input("\nA draw!")
        if p1 >p2:
            raw_input("\nThe first player wins!!!")
        if p2 < p1:
            raw_input("\nThe second player wins!!!")
        if p1 == p2:
            raw_input("\nA draw in this round!")
        playagain()
    if d == 4:
        raw_input("\nYou have $100 now! Winning one round makes you earn $10! \nThe first one who get get $150 will win the game!")
        money1 = 100
        money2 = 100
        while money1 != 150 and money2!= 150:
            raw_input("\nFirst player's turn!")
            r1 = game()
            raw_input("\nSecond player's turn!")
            r2 = game()
            if r1 < r2:
                raw_input("\nFirst player wins in this round")
                money1 = money1 + 10
                raw_input("Now first player has "+ str(money1) + "dollars. \nThe second player has " + str(money2) + " dollars.")
            if r1 > r2:
                raw_input("\nSecond player wins in this round")
                money2 = money2 + 10
                raw_input("Now second player have " + str(money2) + "dollars. \nThe first player has " + str(money1) + " dollars.")
            if r1 == r2:
                raw_input("\nA draw in this round!")
        if money1 ==150:
            raw_input("\nThe first player wins!!!")
        if money2 == 150:
            raw_input("\nThe second player wins!!!")
        playagain()
main()
