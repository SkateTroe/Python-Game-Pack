import Nim

exit = 0
print("-~-~-~-~-~-~WELCOME-~-~-~-~-~-~-~")
print("Grab a friend, let's play a game!")
while exit is 0:
	print("Main menu:")
	print("1: The Game of Nim")
	print("0: Exit")
	print()
	option = int(input("Menu selection: "))
	if option == 1:
		Nim.NewGame()
	elif option == 0:
		exit = 1
	else:
		print("Please select a valid answer: ", option)

print("Goodbye!")
print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")



