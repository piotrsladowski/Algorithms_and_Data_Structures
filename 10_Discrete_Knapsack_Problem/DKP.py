from pathlib import Path
import os

class Algo:
    #Macierz = [[0 for x in range(rozmiarPlecaka)] for y in range(rozmiarPlecaka)]
    Macierz = []
    wartosci = []
    rozmiarPlecaka = 0
    fileIn = None
    totalValue = 0
    dodane = []
    nieDodane = []
    def __init__(self):
        numOfRowsString = input("podaj wielkość macierzy(20, 100, 500, 1000): ")

        fullpath = ""
        if os.name == 'nt':
            mypath = "D:\\AGH\\ZSLAIDS\\materials\\plecaki"
            fullPath = Path(mypath, "packages{0}.txt".format(numOfRowsString))
        elif os.name == 'posix':
            mypath = "/mnt/d/AGH/ZSLAIDS/materials/plecaki"
            fullPath = Path(mypath, "packages{0}.txt".format(numOfRowsString))

        self.fileIn = open(fullPath, 'r')
        self.rozmiarPlecaka = int(numOfRowsString)

    def readSort(self):
        for line in self.fileIn:
            temp = line.split(',')
            if temp[0].isnumeric():
                oplacalnosc = int(temp[3])/(int(temp[1])*int(temp[2]))
                t = [int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]), oplacalnosc]
                self.wartosci.append(t)

        self.wartosci.sort(key=lambda x: x[4], reverse=True)

    def kolejne(self):
        self.Macierz = [[0 for x in range(self.rozmiarPlecaka)] for y in range(self.rozmiarPlecaka)]
        self.nieDodane = list(self.wartosci)
#Rozmiar = 0

#Pion = rozmiarPlecaka
#Poziom = rozmiarPlecaka
#PionMax = 0
#Zapelnione = 0

    def znajdz(self, element):
        for i in range(self.rozmiarPlecaka):
            for o in range(self.rozmiarPlecaka):
                try:
                    isPossible = True
                    for m in range(element[2]):
                        indi = o+element[1]
                        sublist = self.Macierz[i+m][o:indi]
                        if not all(v == 0 for v in sublist):
                            isPossible = False
                            break
                    if isPossible:
                        self.totalValue += element[3]
                        #inserted = True
                        self.dodane.append(element)
                        start = [i, o]
                        return start
                except IndexError:
                    pass

    def akt(self, start, element2):
        for s in range(start[0], element2[2]):
            for t in range(start[1], element2[1]):
                self.Macierz[s][t] = 1

    def rob(self):
        for el in self.wartosci:
            ind = self.znajdz(el)
            print(ind)
            self.akt(ind, el)


al = Algo()
al.readSort()
al.kolejne()   
al.rob()
print(al.totalValue)

#print(Rozmiar/(rozmiarPlecaka**2))
"""print(totalValue)
if os.name == 'nt':
    print("xD")"""