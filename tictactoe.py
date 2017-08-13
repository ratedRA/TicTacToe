
# author - Aman Prasad

import os
import random

def clear():
	os.system('cls')

def displayBoard(theBoard):
	clear()
	print('	|	|')
	print( theBoard[7] +'	'+ '|' + theBoard[8] + '	|' + theBoard[9])
	print('	|	|')
	print('--------|-------|----------')
	print('	|	|')
	print( theBoard[4] +'	'+ '|' + theBoard[5] + '	|' + theBoard[6])
	print('	|	|')
	print('--------|-------|----------')
	print('	|	|')
	print( theBoard[1] +'	'+ '|' + theBoard[2] + '	|' + theBoard[3])
	print('	|	|')

def firstPlayer():
	if random.randint(0,1) == 1:
		return 'Player1'
	else:
		return 'player2'

def playerInput():
	sign = ''
	while not (sign == 'X' or sign  == 'O'):
		sign = input("Player1: choose your sign X or O:").upper()
	if sign == "X":
		return ('X','O')
	else :
		return ('O','X')

def play(board,player):
	position = ''
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not emptyCheck(board,int(position)):
		position = (input("enter the position where you want to mark:"))
	board[int(position)] = "   " +player

def boardFull(board):
	for i in range(1,10):
		if emptyCheck(board,i):
			return False
	return True

def gameWon(board,mark):
	if board[1] == board[2] == board [3] == "   "+mark:
		return True
	if board[4] == board[5] == board [6] == "   "+mark:
		return True
	if board[7] == board[8] == board [9] == "   "+mark:
		return True
	if board[7] == board[4] == board [1] =="   "+mark:
		return True
	if board[8] == board[5] == board [2] == "   "+mark:
		return True
	if board[9] == board[6] == board [3] == "   "+mark:
		return True	
	if board[1] == board[5] == board [9] == "   "+mark:
		return True
	if board[7] == board[5] == board [3] == "   "+mark:
		return True

def emptyCheck(board, position):
	return board[position] == ''

print(' TicTacToe!')
replay = True
while replay == True:
	board = ['']*10
	gameOn = True
	player1Sign, player2Sign = playerInput()
	start = firstPlayer()
	print(start + " will start the game")

	while gameOn == True:
		#print(board)
		if start == 'Player1':
			displayBoard(board)
			play(board, player1Sign)
			if gameWon(board,player1Sign) :
				displayBoard(board)
				print('Congratulations!player1 you have won the game')
				gameOn = False
				print("Do you want to play again?[Y/N]")
				again = input().upper()
				if again == 'N':
					print("BYE")
					replay = False

			else : 
				if boardFull(board):
					displayBoard(board)
					print("This is a tie")
					print("Do you want to play again?[Y/N]")
					again = input().upper()
					if again == 'N':
						print("BYE")
						replay = False
					break
				else:
					start = 'Player2'
		else:
			displayBoard(board)
			play(board, player2Sign)
			if gameWon(board,player2Sign) :
				displayBoard(board)
				print('Congratulations!Player2 you have won the game')
				gameOn = False
				print("Do you want to play again?[Y/N]")
				again = input().upper()
				if again == 'N':
					print("BYE")
					replay = False
			else : 
				if boardFull(board):
					displayBoard(board)
					print("This is a tie")
					print("Do you want to play again?[Y/N]")
					again = input().upper()
					if again == 'N':
						print("BYE")
						replay = False
					break
				else:
					start = 'Player1'


