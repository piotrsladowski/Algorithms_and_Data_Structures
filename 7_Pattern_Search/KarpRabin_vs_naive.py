from pathlib import Path
import os
import KarpRabin_hash_function as hashKR
import time

numOfRowsString = input("Enter matrix size [1000,2000,3000]: ")
numOfProbes = int(input("Enter number of iterations: "))

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
timeNowKarp = time.time()
wzorzec = hashKR.createHash('A', 'B', 'C')
for t in range(0, numOfProbes):
    for r in range(0, rows):
        hInRow = hashKR.createHash(Matrix[r][0], Matrix[r][1], Matrix[r][2])
        if hInRow == wzorzec:
                    hinCol = hashKR.createHash(Matrix[r][c], Matrix[r+1][c], Matrix[r+2][c])
                    if hInRow == hinCol:
                        numOfOccurrences += 1
        for c in range(1, rows):
            try:
                hInRow = hashKR.changeHash(hInRow, Matrix[r][c-1], Matrix[r][c+2])
                if hInRow == wzorzec:
                    hinCol = hashKR.createHash(Matrix[r][c], Matrix[r+1][c], Matrix[r+2][c])
                    if hInRow == hinCol:
                        numOfOccurrences += 1               
            except IndexError:
                pass


timeNowNaive = time.time()
for t in range(0, numOfProbes):
    for r in range(0, rows-2):
        for c in range(0, rows-2):
            try:
                if Matrix[r][c] == 'A' and Matrix[r][c + 1] == 'B' and Matrix[r][c + 2] == 'C':
                    if Matrix[r+1][c] == 'B' and Matrix[r+2][c] == 'C':
                        c += 2
            except IndexError:
                pass


print("Karp-Rabin mean time: {0} seconds".format((time.time()-timeNowKarp)/numOfProbes))
print("Naive mean time: {0} seconds".format((time.time()-timeNowNaive)/numOfProbes))
print("Pattern occured {0} times".format(numOfOccurrences))
