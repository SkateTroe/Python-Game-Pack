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
	ShipYard = [['A','B','C','D','P'],
				[5,4,3,3,2],
				['Aircraft Carrier','Battleship','Cruiser','Destroyer', 'Patrol Ship']]

	Map = BlankMap()
	
	Display(Map)
	for i in range (0,5):
		go = 0
		while go == 0:
			Coordinates = [0]
			while Coordinates[0] == 0:
				print("Please select starting position for your ", ShipYard[2][i])
				go2 = 0
				while go2 == 0:
					StartPoint = input()
					Coordinates = ConvertCoordinates(StartPoint)
					row = int(Coordinates[0])
					column = int(Coordinates[1])
					if Map[row][column] != '- ':
						print("You already have a ship there!")
					else:
						go2 = 1
			opt = 1
			options = ["","","","","",""]
			print("Please choose direction:")
			if int(Coordinates[1])-int(ShipYard[1][i]) > 0 and Overlap(row,column,ShipYard[1][i],Map,'U') == False:
				print(opt, ": Up")
				options[opt] = "Up"
				opt = opt + 1
			if int(Coordinates[1])+int(ShipYard[1][i]) < 11 and Overlap(row,column,ShipYard[1][i],Map,'D') == False:
				print(opt, ": Down")
				options[opt] = "Down"
				opt = opt + 1
			if int(Coordinates[0])-int(ShipYard[1][i]) > 0 and Overlap(row,column,ShipYard[1][i],Map,'L') == False:
				print(opt, ": Left")
				options[opt] = "Left"
				opt = opt + 1
			if int(Coordinates[0])+int(ShipYard[1][i]) < 11 and Overlap(row,column,ShipYard[1][i],Map,'R') == False:
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
				for j in range (0,ShipYard[1][i]):
					Map[row - j][column] = ShipYard[0][i] + " "
					go = 1
			elif options[Direction] == "Down":
				for j in range (0,ShipYard[1][i]):
					Map[row + j][column] = ShipYard[0][i] + " "
					go = 1
			elif options[Direction] == "Left":
				for j in range (0,ShipYard[1][i]):
					Map[row][column - j] = ShipYard[0][i] + " "
					go = 1
			elif options[Direction] == "Right":
				for j in range (0,ShipYard[1][i]):
					Map[row][column + j] = ShipYard[0][i] + " "
					go = 1
			else:
				go = 0
		Display(Map)

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
	if column == 0:
		column = 10
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

Board1 = FillBoard()

Display(Board1)