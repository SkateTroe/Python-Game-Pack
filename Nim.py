exit = 0
Board = [0,0,0]
player = 1

def ShowBoard(Board):
	print()
	for i in range(0, 3):
		for j in range (0, Board[i]):
			print('O ', end='')
		print()
	print()
	print()

def NextTurn(player):
	if player == 1:
		player = 2
	else:
		player = 1
	return player



def NewGame():
	player = 2
	Board = [3,5,7]
	winner = 0
	
	while winner == 0:
		ShowBoard(Board)
		player = NextTurn(player)
		print("Player ", player, "'s turn.")
		go1 = 0
		go2 = 0
		while go1 == 0:
			try:
				row = int(input("Which row will you take from?"))
				if row < 1 or row > 3 or row is None:
					print("Please choose a row between 1-3")
				elif Board[row-1] == 0:
					print("That row is empty.")
				else:
					go1 = 1
			except ValueError:
				pass


		while go2 == 0:
			try:
				pieces = int(input("How many from this row will you take?"))
				if pieces > Board[row-1]:
					print("There aren't that many pieces in that row.")
				elif pieces is None:
					pass
				else:
					go2 = 1
			except ValueError:
				pass


		Board[row-1] = Board[row-1] - pieces
		if Board[0] == 0 and Board[1] == 0 and Board[2] == 0:
			winner = NextTurn(player)

	print("CONGRATULATIONS TO PLAYER ", winner, "!! YOU WIN!!")
	print()
	print()
	print()