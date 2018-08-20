import time
#store game data
b = '1'
p = "~"
s = "S"
xp = 2
yp = 5
xa = 2
ya = 1
xam = 0
yam = 0
GameDisplay1 = [b, b, p, b, b]
GameDisplay2 = [b, b, b, b, b]
GameDisplay3 = [b, b, b, b, b]
GameDisplay4 = [b, b, b, b, b]
GameDisplay5 = [b, b, s, b, b]
BorderH = '|||||||||||||||||||||||||'
userinput = ""

#define functions 
def printscreen():
	print(BorderH)
	print(GameDisplay1)
	print(GameDisplay2)
	print(GameDisplay3)
	print(GameDisplay4)
	print(GameDisplay5)
	print(BorderH)
	print(yp, xp)

def right():
	print(BorderH)
	print(BorderH)	

#runs the game
print("Deadly Pythons")
print("Python = S You = ~")
print("Controls: up, down, left, or right and if you want to leave use s")
print('Created By: Kart Krafter')
print('Published By: Scratchysoft')
user = raw_input('Do You Want To Play y/n: ')
while True:
	if (user == "y"):
		printscreen()
		while True:
			userinput = raw_input('Your move: ')
			#player
			if(userinput == 's'):
				exit()
			elif(yp == 5):
				GameDisplay1[xp] = b
			elif(yp == 4):
				GameDisplay2[xp] = b
			elif(yp == 3):
				GameDisplay3[xp] = b
			elif(yp == 2):
				GameDisplay4[xp] = b
			else:
				GameDisplay5[xp] = b

			if (userinput == 'up'):
				yp += 1
				right()
			elif(userinput == 'down'):
				yp -= 1
				right()
			elif(userinput == 'right'):
				xp += 1
				right()
			elif(userinput == 'left'):
				xp -= 1
				right()
			else:
				print ('That is not a direction to move in')
				print ('Use up, down, left, or right and if you want to leave use s')

			if (yp == 5):
				GameDisplay1[xp] = p
			elif(yp == 4):
				GameDisplay2[xp] = p
			elif(yp == 3):
				GameDisplay3[xp] = p
			elif(yp == 2):
				GameDisplay4[xp] = p
			else:
				GameDisplay5[xp] = p

			if ((yp == ya + 1) & (xp == xa)):
				print("You Win")
				time.sleep(5)
				exit()
			elif((yp == ya - 1) & (xp == xa)):
				print("You Win")
				time.sleep(5)
				exit()
			elif((xp == xa + 1) & (yp == ya)):
				print("You Win")
				time.sleep(5)
				exit()
			elif((xp == xa - 1) & (yp == ya)):
				print("You Win")
				time.sleep(5)
				exit()

			#computer
			if(ya == 5):
				GameDisplay1[xa] = b
			elif(ya == 4):
				GameDisplay2[xa] = b
			elif(ya == 3):
				GameDisplay3[xa] = b
			elif(ya == 2):
				GameDisplay4[xa] = b
			elif(ya == 1):
				GameDisplay5[xa] = b

			if(ya >= yp):
				yam = ya - yp
			else:
				yam = yp - ya

			if(xa >= xp):
				xam = xa - xp
			else:
				xam = xp - xa

			if(yam >= xam):
				if(yam >= 0):
					ya += 1
				else:
					ya -= 1
			else:
				if(xam <= 0):
					xa += 1
				else:
					xa -= 1

			if(ya == 5):
				GameDisplay1[xa] = s
			elif(ya == 4):
				GameDisplay2[xa] = s
			elif(ya == 3):
				GameDisplay3[xa] = s
			elif(ya == 2):
				GameDisplay4[xa] = s
			elif(ya == 1):
				GameDisplay5[xa] = s
			print(xa, ya)

			if ((ya == yp + 1) & (xa == xp)):
				print("You Loose")
				time.sleep(5)
				exit()
			elif((ya == yp - 1) & (xa == xp)):
				print("You Loose")
				time.sleep(5)
				exit()
			elif((xa == xp + 1) & (ya == yp)):
				print("You Loose")
				time.sleep(5)
				exit()
			elif((xa == xp - 1) & (ya == yp)):
				print("You Loose")
				time.sleep(5)
				exit()

			printscreen()

			
	else:
		exit()
