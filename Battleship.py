import random

cShipYard = [['A','B','C','D','P'],
			[5,4,3,3,2],
			['Aircraft Carrier','Battleship','Cruiser','Destroyer', 'Patrol Ship']]

def cls():
	print("\n" * 50)

def BlankMap():
	Map = [['  ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','0 '],
		   ['A ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['B ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['C ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['D ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['E ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['F ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['G ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['H ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['I ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
		   ['J ','- ','- ','- ','- ','- ','- ','- ','- ','- ','- ']]
	return Map

def FillBoard():

	#initialize and display the board
	Map = BlankMap()
	Display(Map)

	#Repeat 5 times: one for each ship.
	for i in range (0,5):
		
		#This while loop basically contains each instance of the for loop it's
		#	nested in. IsFinalPlacement will be set to true if and only if all
		#	other tests are passed and the user confirms their choice.
		IsFinalPlacement = False
		
		while IsFinalPlacement == False:
			#cShipYard contains data on the ships in play. Row 2 contains ship names.
			print("Please select starting position for your", cShipYard[2][i])

			#Takes standard Battleship input--B4, J8, etc--and converts into numeric
			#	coordinates. Then tests that a ship has not already been placed at
			#	those coordinates.
			IsSpaceAvailable = False
			while IsSpaceAvailable == False:
				StartPoint = input()
				Coordinates = ConvertCoordinates(StartPoint)
				
				row = int(Coordinates[0])
				column = int(Coordinates[1])
				
				#Hard to have a X10 option, so we're calling it X0.
				if column == 0:
					column = 10

				if Map[row][column] != '- ':
					print("You already have a ship there!")
				else:
						IsSpaceAvailable = True
			#Dynamic menu, only offers legal options, and always lists options
			#	numerically, without gaps. opt controls the option numbers, incrementing
			#	whenever a new option is added to the menu.
			#
			#options[] is an array of keywords that will assigned to position "opt"
			opt = 1
			options = ["","","","","",""]
			print("Please choose direction:")
			if int(row)-int(cShipYard[1][i]) > 0 and Overlap(row,column,cShipYard[1][i],Map,'U') == False:
				print(opt, ": Up")
				options[opt] = "Up"
				opt = opt + 1
			if int(row)+int(cShipYard[1][i]) < 11 and Overlap(row,column,cShipYard[1][i],Map,'D') == False:
				print(opt, ": Down")
				options[opt] = "Down"
				opt = opt + 1
			if int(column)-int(cShipYard[1][i]) > 0 and Overlap(row,column,cShipYard[1][i],Map,'L') == False:
				print(opt, ": Left")
				options[opt] = "Left"
				opt = opt + 1
			if int(column)+int(cShipYard[1][i]) < 11 and Overlap(row,column,cShipYard[1][i],Map,'R') == False:
				print(opt, ": Right")
				options[opt] = "Right"
				opt = opt + 1
			options[opt] = "Change"
			print(opt, ": Change Coordinates")
			print()

			#Test if the input choice is among the valid options. If not, an error will be thrown and
			#	caught, and the loop will repeat. 
			IsValidChoice = False

			while IsValidChoice == False:
				try:
					Direction = int(input("Choice:   "))
					print()
				
					if options[Direction] == "Up":
						for j in range (0,cShipYard[1][i]):
							Map[row - j][column] = cShipYard[0][i] + " "
							IsValidChoice = True
							IsFinalPlacement = True

					elif options[Direction] == "Down":
						for j in range (0,cShipYard[1][i]):
							Map[row + j][column] = cShipYard[0][i] + " "
							IsValidChoice = True
							IsFinalPlacement = True

					elif options[Direction] == "Left":
						for j in range (0,cShipYard[1][i]):
							Map[row][column - j] = cShipYard[0][i] + " "
							IsValidChoice = True
							IsFinalPlacement = True

					elif options[Direction] == "Right":
						for j in range (0,cShipYard[1][i]):
							Map[row][column + j] = cShipYard[0][i] + " "
							IsValidChoice = True
							IsFinalPlacement = True

					else:
						IsValidChoice = True
						IsFinalPlacement = False
				except:
					print("Please choose a option between 1 and ", opt)
		Display(Map)
	return Map

def AutoFill():

	#Accept while loop allows user to reject a random board.
	Accept = 'N'
	while Accept != 'Y':
		Map = BlankMap()

		for i in range (5):
			#ValidChoice ensures that each ship is properly placed.
			IsValidChoice = False
			while IsValidChoice == False:

				#SpotEmpty checks that the starting poitn is valid for each ship.
				IsSpotEmpty = False
				while IsSpotEmpty == False:
					row = random.randint(1,10)
					col = random.randint(1,10)

					if Map[row][col] == '- ':
						IsSpotEmpty = True

				options = ["","","","",""]
				opt = 1

				if row-int(cShipYard[1][i]) > 0 and Overlap(row,col,cShipYard[1][i],Map,'U') == False:
						options[opt] = "Up"
						opt = opt + 1
				if row+int(cShipYard[1][i]) < 11 and Overlap(row,col,cShipYard[1][i],Map,'D') == False:
						options[opt] = "Down"
						opt = opt + 1
				if col-int(cShipYard[1][i]) > 0 and Overlap(row,col,cShipYard[1][i],Map,'L') == False:
						options[opt] = "Left"
						opt = opt + 1
				if col+int(cShipYard[1][i]) < 11 and Overlap(row,col,cShipYard[1][i],Map,'R') == False:
						options[opt] = "Right"
						opt = opt + 1

				Direction = random.randint(1,opt)
						
				if options[Direction] == "Up":
					for j in range (0,cShipYard[1][i]):
						Map[row - j][col] = cShipYard[0][i] + " "
						IsValidChoice = True

				elif options[Direction] == "Down":
					for j in range (0,cShipYard[1][i]):
						Map[row + j][col] = cShipYard[0][i] + " "
						IsValidChoice = True

				elif options[Direction] == "Left":
					for j in range (0,cShipYard[1][i]):
						Map[row][col - j] = cShipYard[0][i] + " "
						IsValidChoice = True

				elif options[Direction] == "Right":
					for j in range (0,cShipYard[1][i]):
						Map[row][col + j] = cShipYard[0][i] + " "
						IsValidChoice = True

		Display(Map)
		Accept = input("Type Y to accept, N to rebuild.")

	return Map

def Overlap(row,column,Length,Map,Direction):
	if Direction == 'U':
		try: 
			for i in range (0,Length):
				if Map[row-i][column] != "- ":
					return True
			return False
		except:
			return False

	if Direction == 'D':
		try: 
			for i in range (0,Length):
				if Map[row+i][column] != "- ":
					return True
			return False
		except:
			return False

	if Direction == 'L':
		try: 
			for i in range (0,Length):
				if Map[row][column-i] != "- ":
					return True
			return False
		except:
			return False

	if Direction == 'R':
		try: 
			for i in range (0,Length):
				if Map[row][column+i] != "- ":
					return True
			return False
		except:
			return False
		
def ConvertCoordinates(Point):
	go = 0
	while go == 0:
		Point = Point.strip()
		if len(Point) != 2:
			print("Coordinates should consist of only 1 letter and 1 number.")
			row = 0
			column = 0
		elif Point[0].isalpha() == True and Point[1].isdigit() == True:
			if ('A' <= Point[0] <= 'J' or 'a' <= Point[0] <= 'j') and 0 <= int(Point[1]) <= 9:
				row = Alpha2Num(Point[0])
				column = Point[1]
				if row == 0:
					print("Please choose a valid letter")
				else:
					go = 1
			else:
				row = 0
				column = 0
		elif Point[0].isdigit() == True and Point[1].isalpha() == True:
			if ('A' <= Point[1] <= 'J' or 'a' <= Point[1] <= 'j') and 0 <= int(Point[0]) <= 9:
				row = Alpha2Num(Point[1])
				column = Point[0]
				if row == 0:
					print("Please choose a valid letter")
				else:
					go = 1
			else:
				row = 0
				column = 0
		else:
			print("Coordinates should consist of only 1 letter and 1 number.")
			row = 0
			column = 0
		if go == 0:
			Point = input("Please input new point: ")
	Coordinates = [row,column]
	return Coordinates	

def Alpha2Num(Alpha):
	ref = ['A','B','C','D','E','F','G','H','I','J']
	ref2 = ['a','b','c','d','e','f','g','h','i','j']
	try:
		for i in range (0,10):
			if ref[i] == Alpha or ref2[i] == Alpha:
				return i + 1
	except:
		return 0

def Display(Map):

	for i in range (0,11):
		for j in range (0,11):
			print (Map[i][j],end='')
		print()

def LaunchAttack(Row,Col,Map):

	Target = Map[Row][Col]
	if Target == "- ":
		Damage = ["o ","False",]
	elif Target == "A ":
		Damage = ["X ","True", 0]
	elif Target == "B ":
		Damage = ["X ", "True", 1]
	elif Target == "C ":
		Damage = ["X ", "True", 2]
	elif Target == "D ":
		Damage = ["X ", "True", 3]
	elif Target == "P ":
		Damage = ["X ", "True", 4]
	return Damage


def FriendMode():

	cls()

	Player = 1
	winner = False
	ShipYard1 = ShipYard2 = cShipYard
	score1 = score2 = 17

	#Make AutoFill() vs FillBoard() a choice
	print("Player 1:")
	print("1: Place your ships manually.")
	print("2: Automatically generate map.")
	print()
	
	FillChoice = int(input("Choice: "))
	if FillChoice == 1:
		Board1 = FillBoard()
	else
		Board1 = AutoFill()

	cls()

	#Make AutoFill() vs FillBoard() a choice
	print("Player 1:")
	print("1: Place your ships manually.")
	print("2: Automatically generate map.")
	
	FillChoice = int(input("Choice: "))
	if FillChoice == 1:
		Board1 = FillBoard()
	else
		Board1 = AutoFill()

	cls()


	Radar1 = BlankMap()
	Radar2 = BlankMap()

	while winner == False:

		if Player == 1:
			print("--------------------")
			print("      PLAYER 1      ")
			print("--------------------")
			print()
			input("Press Enter to reveal board")
			cls()
			print("--------------------")
			print("      PLAYER 1      ")
			print("--------------------")
			print()
			print("RADAR")
			print("______________________")
			Display(Radar1)
			print()
			print()
			print("YOUR SHIPS")
			print("______________________")
			Display(Board1)
			print()
			IsSpotEmpty = False

			while IsSpotEmpty == False:
				Attack = input("Input Attack Coordinates: ")

				AttackCoord = ConvertCoordinates(Attack)

				AtRow = int(AttackCoord[0])
				AtCol = int(AttackCoord[1])
				if AtCol == 0:
					AtCol = 10
				if Radar1[AtRow][AtCol] == "- ":
					IsSpotEmpty = True
				else:
					print("You have already attacked those coordinates.")

			Results = LaunchAttack(AtRow,AtCol,Board2)

			Radar1[AtRow][AtCol] = Results[0]

			cls()
			print("--------------------")
			print("      PLAYER 1      ")
			print("--------------------")
			print()
			print("RADAR")
			print("______________________")
			Display(Radar1)
			print()
			print()
			print("YOUR SHIPS")
			print("______________________")
			Display(Board1)
			print()

			if Results[1] == "True":
				ShipYard2[1][Results[2]] = ShipYard2[1][Results[2]] - 1
				if ShipYard2[1][Results[2]] == 0:
					print("You sank their ", cShipYard[2][Results[2]], "!!")
				else:
					print("Hit!!")
				Board2[AtRow][AtCol] = "X "
				score2 = score2 - 1
			else:
				print("Miss")
				Board2[AtRow][AtCol] = "o "
			print()
			print()

			input("Press Enter to end turn")
			cls()

		else:
			print("--------------------")
			print("      PLAYER 2      ")
			print("--------------------")
			print()
			input("Press Enter to reveal board")
			cls()
			print("--------------------")
			print("      PLAYER 2      ")
			print("--------------------")
			print()
			print("RADAR")
			print("______________________")
			Display(Radar2)
			print()
			print()
			print("YOUR SHIPS")
			print("______________________")
			Display(Board2)
			print()

			IsSpotEmpty = False

			while IsSpotEmpty == False:
				Attack = input("Input Attack Coordinates: ")

				AttackCoord = ConvertCoordinates(Attack)

				AtRow = int(AttackCoord[0])
				AtCol = int(AttackCoord[1])
				if AtCol == 0:
					AtCol = 10
				if Radar2[AtRow][AtCol] == "- ":
					IsSpotEmpty = True
				else:
					print("You have already attacked those coordinates.")

			Results = LaunchAttack(AtRow,AtCol,Board1)

			Radar2[AtRow][AtCol] = Results[0]

			cls()
			print("--------------------")
			print("      PLAYER 2      ")
			print("--------------------")
			print()
			print("RADAR")
			print("______________________")
			Display(Radar2)
			print()
			print()
			print("YOUR SHIPS")
			print("______________________")
			Display(Board2)
			print()

			if Results[1] == "True":
				ShipYard1[1][Results[2]] = ShipYard1[1][Results[2]] - 1
				if ShipYard1[1][Results[2]] == 0:
					print("You sank their ", cShipYard[2][Results[2]], "!!")
				else:
					print("Hit!!")
				Board1[AtRow][AtCol] = "X "
				score1 = score1 - 1
			else:
				print("Miss")
				Board1[AtRow][AtCol] = "o "
			print()
			print()
			input("Press Enter to end turn")
			cls()

		if score1 == 0 or score2 == 0:
			winner = 1
		else:
			if Player == 1:
				Player = 2
			else:
				Player = 1

	print("Player ", Player, " wins!!")






print("                                     |__")
print("                                     |\/")
print("                                     ---")
print("                                     / | [")
print("                              !      | |||")
print("                            _/|     _/|-++'")
print("                        +  +--|    |--|--|_ |-")
print("                     { /|__|  |/\__|  |--- |||__/")
print("                    +---------------___[}-_===_.'____                 /\ ")
print("                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _")
print(" __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")
print("|                                                                     BB-61/")
print(" \_________________________________________________________________________|")
print()
print()
print("              _           _   _   _           _     _       ")
print("             | |         | | | | | |         | |   (_)      ")
print("             | |__   __ _| |_| |_| | ___  ___| |__  _ _ __  ")
print("             | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ ")
print("             | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |")
print("             |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ ")
print("                                                     | |    ")
print("                                                     |_|    ")
print()
print()

Exit = False
while Exit == False:
	print("Choose a game mode:")
	print("1: Player vs Player")
	print("2: Player vs AI")
	print("0: Exit")
	print()
	mode = int(input("Choice:   "))

	if mode == 1:
		FriendMode()
	elif mode == 2:
		print("Still in development.")
	elif mode == 0:
		print ("Goodbye!!")
		Exit = True
	else:
		print("Please choose a valid mode")
		print(mode)