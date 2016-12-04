'''
You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?
'''

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
