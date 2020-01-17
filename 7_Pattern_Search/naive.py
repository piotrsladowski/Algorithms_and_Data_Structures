from pathlib import Path
import os

numOfRowsString = input("Enter matrix size [1000,2000,3000]: ")

if os.name == 'nt':
    fullPath = Path("patterns\{0}_pattern.txt".format(numOfRowsString))
elif os.name == 'posix':
    fullPath = Path("patterns/{0}_pattern.txt".format(numOfRowsString))

fl = open(fullPath, 'r')
rows = int(numOfRowsString)
Matrix = [[None for x in range(rows)] for y in range(rows)]

tempX = 0
for line in fl.readlines():
    tempY = 0
    line = line.rstrip()
    for item in line:  
        Matrix[tempX][tempY] = item
        tempY += 1
    tempX += 1


numOfOccurrences = 0

for r in range(0, rows-2):
    for c in range(0, rows-2):
        try:
            if Matrix[r][c] == 'A' and Matrix[r][c + 1] == 'B' and Matrix[r][c + 2] == 'C':
                if Matrix[r+1][c] == 'B' and Matrix[r+2][c] == 'C':
                    numOfOccurrences += 1
                    c += 2
        except IndexError:
            pass

print("Pattern occured {0} times".format(numOfOccurrences))
