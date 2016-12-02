import re, math

'''
For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?
'''

find = False
allPoints = []
part2 = 0

def readFile():
	with open('input.txt') as f:
		lines = f.read()
	return lines.split(', ')


def transition(step, direction, x, y):
	global find
	global part2
	if not find:
		for i in range(step):
			if direction == 'O':
				x -= 1
			elif direction == 'E':
				x += 1
			elif direction == 'N':
				y += 1
			elif direction == 'S':
				y -= 1

			if str(x) + '_' + str(y) in allPoints:
				part2 = math.fabs(x - 0) + math.fabs(y - 0)
				find = True

			allPoints.append(str(x) + '_' + str(y))

def pathReader(puzzle):

	direction = 'N'
	blockAway = 0
	countPoint = 0
	pointX = 0
	pointY = 0
	pointList = []

	for path in puzzle:
		path = re.split('(\d+)', path)

		if countPoint % 2 == 0:
			if direction == 'N':
				if path[0] == 'L':
					transition(int(path[1]), 'O', pointX, pointY)
					pointX = pointX - int(path[1])
					direction = 'O'
				else:
					transition(int(path[1]), 'E', pointX, pointY)
					pointX = pointX + int(path[1])
					direction = 'E'
			else:
				if path[0] == 'L':
					transition(int(path[1]), 'E', pointX, pointY)
					pointX = pointX + int(path[1])
					direction = 'E'
				else:
					transition(int(path[1]), 'O', pointX, pointY)
					pointX = pointX - int(path[1])
					direction = 'O'
		else:
			if direction == 'E':
				if path[0] == 'L':
					transition(int(path[1]), 'N', pointX, pointY)
					pointY = pointY + int(path[1])
					direction = 'N'
				else:
					transition(int(path[1]), 'S', pointX, pointY)
					pointY = pointY - int(path[1])
					direction = 'S'
			else:
				if path[0] == 'L':
					transition(int(path[1]), 'S', pointX, pointY)
					pointY = pointY - int(path[1])
					direction = 'S'
				else:
					transition(int(path[1]), 'N', pointX, pointY)
					pointY = pointY + int(path[1])
					direction = 'N'

		pointList += [str(pointX) + ', ' + str(pointY)]

		countPoint += 1
	blockAway = math.fabs(pointX - 0) + math.fabs(pointY - 0)
	print "Part 1 : " + str(blockAway)

if __name__ == '__main__':
	puzzle = readFile()
	pathReader(puzzle)
	print "Part 2 : " + str(part2)
