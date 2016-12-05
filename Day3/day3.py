

def readFile():
	with open('input.txt') as f:
		lines = f.read()
	return lines.split('\n')


def getTriangle(input):
	triangle = 0
	triangleVert = 0
	valueList = []
	verticalList = []

	count = 0
	for lines in input:
		value = " ".join(lines.split()).split(' ')
		valueList.append(value)
		a = int(value[2])
		b = int(value[1])
		c = int(value[0])

		if b+c > a and c+a > b and a+b > c:
			triangle += 1

	print "Part 1 : " + str(triangle)

	for val in valueList:

		if (count+1) % 3 == 0:
			verticalList.append(valueList[count-2][0] + ',' + valueList[count-1][0] + ',' + valueList[count][0])
			verticalList.append(valueList[count-2][1] + ',' + valueList[count-1][1] + ',' + valueList[count][1])
			verticalList.append(valueList[count-2][2] + ',' + valueList[count-1][2] + ',' + valueList[count][2])

		count += 1

	for val in verticalList:
		value = val.split(',')
		a = int(value[2])
		b = int(value[1])
		c = int(value[0])

		if b+c > a and c+a > b and a+b > c:
			triangleVert += 1

	print "Part 2 : " + str(triangleVert)


if __name__ == '__main__':
	content = readFile()
	getTriangle(content)