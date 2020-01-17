from pathlib import Path
import os
import random
import math
import time

def getKey(dictt,value):
     return [key for key in dictt.keys() if (dictt[key] == value)]

def check(first, second):
    verticesDegree[first] += 1
    verticesDegree[second] += 1
    if verticesDegree[first] == 3 or verticesDegree[second] == 3: #prevent creating 3rd degree node
        verticesDegree[first] -= 1
        verticesDegree[second] -= 1
        return False
    elif ((1 not in verticesDegree.values()) and (2 in verticesDegree.values())): #prevent early closing of the path
        verticesDegree[first] -= 1
        verticesDegree[second] -= 1
        return False


userChoice = input("Path or closed path? [p/c]: ")
timeTotal = 0

for t in range(100):
    fl = open("TSP.txt", 'r')
    cities = {} #city id + coords
    totalLen = 0
    edgeWeights = {} #dict contains edge weights. Will be easier to find last edge
    verticesDegree = {}
    wk = [] #list contains edge weights. Will be easier to access elements

    for line in fl:
        s = line.replace('\n', '')
        s = s.split('\t')
        temp = []
        temp.append(float(s[1]))
        temp.append(float(s[2]))
        cities[int(s[0])] = temp

    timeStart = time.time()

    for i in range(1,101):
        verticesDegree[i] = 0

    x = 1
    for o in range(1,101):
        for p in range(x, 101):
            if o != p:
                key = str(o) + '-' + str(p)
                waga = math.sqrt((cities[o][0] - cities[p][0])**2 + (cities[o][1] - cities[p][1])**2)
                edgeWeights[key] = waga
                wk.append([key, waga])
        x += 1

    wk.sort(key=lambda x: x[1])

    # We have to add 99 edges starting from smallest weights
    for p in range(1,100):
        i = 0
        nodes = wk[i][0].split('-') # Get edges with smallest weight and check if we can add them
        first = int(nodes[0])
        second = int(nodes[1])
        while check(first, second) == False:
            nodes = wk[i][0].split('-')
            first = int(nodes[0])
            second = int(nodes[1])
            i += 1
        # Increase path lenght and remove used edge
        totalLen += wk[i][1]
        del wk[i]

    #Close path
    if userChoice == 'c':
        cos = getKey(verticesDegree, 1)
        lastEdge = str(cos[0]) + '-' + str(cos[1])
        totalLen += edgeWeights[lastEdge]


    timeTotal += time.time() - timeStart


print("Mean time: {0}".format(timeTotal/100))
print("Path lenght: {0}".format(totalLen))