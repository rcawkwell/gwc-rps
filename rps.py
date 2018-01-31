#Girls Who Code 2018 In structional Staff Technical Project
import math 
import random, itertools
import sys

'''
Rock is 0. Paper is 1. Scissors is 2.
'''
ROCK = 'rock' 
PAPER = 'paper' 
SCI = 'scissors' 

class SetUp
	#initialize game
	def __init__(self):
	#defines the human turn
	def humanTurn(self): 
		humMove = raw_input("Rock? Paper? Scissors?: ")
		#checks for capitalization errors
		humMove = humMove.lower()
		while(humMove):
			if (humMove == ROCK or humMove == PAPER or humMove == SCI): 
				return humMove
			else: 
				print('Something went wrong with your input. Try again') 
				humMove = raw_input('Rock? Paper? Scissors?: ')

	#defines the computer player turn
	def compTurn(self):
		move = randint(0,2)
		if (move == 0) 
			return ROCK
		elif (move == 1) 
			return PAPER
		else 
			return SCI
	#decide who has won the round
	#since only 7 different outcomes to check, brute force
	def compareTurns(self, hMove, cMove):
		if hMove is cMove: 
			return 'tie' 
		else: 
			if hMove == ROCK: 
				if cMove == PAPER: 
					return 'lose'
				else:
					return 'win'
			elif hMove == PAPER: 
				if cMove == SCI: 
					return 'lose' 
				else: 
					return 'win'
			else: 
				if cMove == ROCK: 
					return 'lose' 
				else: 
					return 'win'
def main()
