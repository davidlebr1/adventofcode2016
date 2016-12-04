keypadPart1 = [	[0 ,0, 0, 0, 0],
				[0, 1, 2, 3, 0], 
				[0 ,4, 5, 6, 0], 
				[0 ,7, 8, 9, 0],
				[0 ,0, 0, 0, 0],
			 ]

keypadPart2 = [ [0, 0, 0, 0, 0, 0, 0],
				[0, 0 ,0, 1, 0, 0, 0],
				[0, 0, 2, 3, 4, 0, 0],
				[0, 5, 6, 7, 8, 9, 0],
				[0, 0, 'A', 'B', 'C', 0, 0],
				[0, 0, 0, 'D', 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0]
			 ]


def readFile():
	with open('input.txt') as f:
		lines = f.read()
	return lines.split('\n')


def findCode(content, keypad, part, x, y):
	button = ''
	code = ''
	startX = x
	startY = y
	for instruction in content:
		for move in instruction:
			if move == 'L':
				if keypad[startY][startX-1] > 0:
					startX -= 1
			if move == 'R':
				if keypad[startY][startX+1] > 0:
					startX += 1			
			if move == 'U':
				if keypad[startY-1][startX] > 0:
					startY -= 1		
			if move == 'D':
				if keypad[startY+1][startX] > 0:
					startY += 1
		
		code += str(keypad[startY][startX])

	print part + code

if __name__ == '__main__':
	content = readFile()
	findCode(content, keypadPart1, "Part 1 : ", 2, 2)
	findCode(content, keypadPart2, "Part 2 : ", 1, 3)
