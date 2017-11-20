import os

cShipYard = [['A','B','C','D','P'],
			[5,4,3,3,2],
			['Aircraft Carrier','Battleship','Cruiser','Destroyer', 'Patrol Ship']]

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

	Map = BlankMap()
	
	Display(Map)
	for i in range (0,5):
		go = 0
		while go == 0:
			Coordinates = [0]
			while Coordinates[0] == 0:
				print("Please select starting position for your ", cShipYard[2][i])
				go2 = 0
				while go2 == 0:
					StartPoint = input()
					Coordinates = ConvertCoordinates(StartPoint)
					row = int(Coordinates[0])
					column = int(Coordinates[1])
					if column == 0:
						column = 10
					if Map[row][column] != '- ':
						print("You already have a ship there!", Map[row][column])
					else:
						go2 = 1
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



			Direction = int(input("Choice:   "))
			print()
			if Direction > opt or Direction < 1:
				print("Please choose a listed option")
			elif options[Direction] == "Up":
				for j in range (0,cShipYard[1][i]):
					Map[row - j][column] = cShipYard[0][i] + " "
					go = 1
			elif options[Direction] == "Down":
				for j in range (0,cShipYard[1][i]):
					Map[row + j][column] = cShipYard[0][i] + " "
					go = 1
			elif options[Direction] == "Left":
				for j in range (0,cShipYard[1][i]):
					Map[row][column - j] = cShipYard[0][i] + " "
					go = 1
			elif options[Direction] == "Right":
				for j in range (0,cShipYard[1][i]):
					Map[row][column + j] = cShipYard[0][i] + " "
					go = 1
			else:
				go = 0
		Display(Map)
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
				go = 1
			else:
				row = 0
				column = 0
		elif Point[1].isalpha() == True and Point[0].isdigit() == True:
			if ('A' <= Point[1] <= 'J' or 'a' <= Point[0] <= 'j') and 0 <= int(Point[0]) <= 9:
				row = Alpha2Num(Point[0])
				column = Point[0]
				go = 1
			else:
				row = 0
				column = 0
		else:
			print("Coordinates should consist of only 1 letter and 1 number.")
			row = 0
			column = 0
	Coordinates = [row,column]
	return Coordinates	

def Alpha2Num(Alpha):
	ref = ['A','B','C','D','E','F','G','H','I','J']
	ref2 = ['a','b','c','d','e','f','g','h','i','j']
	for i in range (0,10):
		if ref[i] == Alpha or ref2[i] == Alpha:
			return i + 1

def Display(Map):

	for i in range (0,11):
		for j in range (0,11):
			print (Map[i][j],end='')
		print()

def LaunchAttack(Row,Col,Map):

	Target = Map[Row,Col]
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

	os.system("cls")

	Player = 1
	winner = False
	ShipYard1 = ShipYard2 = cShipYard
	score1 = score2 = 17

	print("Player 1: Place your ships.")
	Board1 = FillBoard()

	os.system("cls")

	print("Player 2: Place your ships")
	Board2 = FillBoard()

	os.system("cls")


	Radar1 = BlankMap
	Radar2 = BlankMap

	while winner == False:

		if Player == 1:
			print("--------------------")
			print("      PLAYER 1      ")
			print("--------------------")
			print()
			input("Press Enter to reveal board")
			os.system("cls")
			print("--------------------")
			print("      PLAYER 1      ")
			print("--------------------")
			print()
			print("RADAR")
			Display(Radar1)
			print()
			print()
			print("YOUR SHIPS")
			Display(Board1)
			print()
			Attack = input("Input Attack Coordinates: ")

			AttackCoord = ConvertCoordinates(Attack)

			AtRow = int(AttackCoord[0])
			AtCol = int(AttackCoord[1])
			if AtCol == 0:
				AtCol = 10

			Results = LaunchAttack(AtRow,AtCol,Board2)

			Radar1[AtRow][AtCol] = Results[0]

			os.system("cls")
			print("--------------------")
			print("      PLAYER 1      ")
			print("--------------------")
			print()
			print("RADAR")
			Display(Radar1)
			print()
			print()
			print("YOUR SHIPS")
			Display(Board1)
			print()

			if Results[1] == "True":
				ShipYard1[1][Results[2]] = ShipYard1[1][Results[2]] - 1
				if ShipYard1[1][Results[2]] == 0:
					print("You sank their ", ShipYard[2][Results[2]], "!!")
				else:
					print("Hit!!")
				score2 = score2 - 1
			else:
				print("Miss")
			print()
			print()

			input("Press Enter to end turn")
			print()
			print()

			input("Press Enter to end turn")
		else:
			print("--------------------")
			print("      PLAYER 2      ")
			print("--------------------")
			print()
			input("Press Enter to reveal board")
			os.system("cls")
			print("--------------------")
			print("      PLAYER 2      ")
			print("--------------------")
			print()
			print("RADAR")
			Display(Radar2)
			print()
			print()
			print("YOUR SHIPS")
			Display(Board2)
			print()
			Attack = input("Input Attack Coordinates: ")

			AttackCoord = ConvertCoordinates(Attack)

			AtRow = int(AttackCoord[0])
			AtCol = int(AttackCoord[1])
			if AtCol == 0:
				AtCol = 10

			Results = LaunchAttack(AtRow,AtCol,Board1)

			Radar2[AtRow][AtCol] = Results[0]

			os.system("cls")
			print("--------------------")
			print("      PLAYER 2      ")
			print("--------------------")
			print()
			print("RADAR")
			Display(Radar2)
			print()
			print()
			print("YOUR SHIPS")
			Display(Board2)
			print()

			if Results[1] == "True":
				ShipYard1[1][Results[2]] = ShipYard1[1][Results[2]] - 1
				if ShipYard1[1][Results[2]] == 0:
					print("You sank their ", ShipYard[2][Results[2]], "!!")
				else:
					print("Hit!!")
				Score1 = Score1 - 1
			else:
				print("Miss")
			print()
			print()
			input("Press Enter to end turn")

		if score1 == 0 or score2 == 0:
			winner = 1
		else:
			if player == 1:
				player = 2
			else:
				player = 1

	print("Player ", player, " wins!!")






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