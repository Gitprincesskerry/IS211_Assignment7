# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 7 Assignment

import random

class PigGame():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def game(self):
        dice = OneDie() #initialize die class
        while self.player1.score < 100 and self.player2.score < 100:
            tempscore = 0
            hold = False
            print("\n\n It's now player 1's turn! \n\n")
            while hold == False:
                dice.onedieroll()
                if dice.value == 1:
                    print("Sorry, you have rolled a 1, next players turn. ")
                    hold = True
                else:
                    tempscore = tempscore + dice.value
                    print("You have rolled %d, you currently have %d points. Would you like to roll or hold? (type r for roll and h for hold)." %(dice.value, tempscore))
                    reply = raw_input()
                    reply = reply.lower()

                    if reply == 'h':
                        self.player1.score = self.player1.score + tempscore
                        print("Player 1 has %d points " %self.player1.score)
                        hold = True
                    if self.player1.score + tempscore >= 100:
                        self.player1.score = self.player1.score + tempscore
                        hold = True
                        print("Your score is greater than or equal to 100.")

            tempscore = 0
            hold = False
            print("\n\n It's now player 2's turn! \n\n")
            while hold == False:
                dice.onedieroll()
                if dice.value == 1:
                    print("Sorry, you have rolled a 1, next players turn. ")
                    hold = True
                else:
                    tempscore = tempscore + dice.value
                    print("You have rolled %d, you currently have %d points. Would you like to roll or hold? (type r for roll and h for hold)." %(dice.value, tempscore))
                    reply = raw_input()
                    reply = reply.lower()

                    if reply == 'h':
                        self.player2.score = self.player2.score + tempscore
                        print("Player 2 has %d points " %self.player2.score)
                        hold = True
                    if self.player2.score + tempscore >= 100:
                        self.player2.score = self.player2.score + tempscore
                        hold = True
                        print("Your score is greater than or equal to 100.")

        if self.player1.score> self.player2.score:
            print("Player 1, Has Won. Congratulations!!! ")
        elif self.player2.score > self.player1.score:
            print("Player 2, Has Won. Congratulations!!! ")
        else:
            print("Congratulations to you both!!!")

class Player(object):
    def __init__(self):
        self.score = 0

    def output_score():
        return self.score

class OneDie(object):
    def __init__(self):
        random.seed(0)
        self.value = 0

    def onedieroll(self):
        self.value = random.randint(1,6)
        return self.value

if __name__ == "__main__":
    x = PigGame()
    x.game()
