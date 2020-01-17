from pathlib import Path
import os
import random
import math

fl = open("TSP.txt", 'r')
cities = []
cities1 = {}

for line in fl:
    s = line.replace('\n', '')
    s = s.split('\t')
    temp = []
    temp.append(float(s[1]))
    temp.append(float(s[2]))
    cities1[int(s[0])] = temp
    cities.append(temp)

bestVerticle = None
shortestPath = math.inf
path = []

def szukaj(vert, userChoice):
    global shortestPath
    global bestVerticle
    global path
    path = []
    total = 0
    choosen = vert
    path.append(choosen)
    first = choosen
    notVisited = [i for i in range (1,101)]
    notVisited.remove(choosen)

    while len(notVisited) != 0:
        droga = math.inf
        ver = None
        for c in notVisited:
            path2 = math.sqrt((cities1[choosen][0] - cities1[c][0])**2 + (cities1[choosen][1] - cities1[c][1])**2)
            if path2 < droga:
                droga = path2
                ver = c
        total += droga
        choosen = ver
        notVisited.remove(choosen)
        path.append(choosen)
        last = choosen
    
    #Closing path
    if userChoice == 'c':
        total += math.sqrt((cities1[first][0] - cities1[last][0])**2 + (cities1[first][1] - cities1[last][1])**2)
    if total < shortestPath:
        shortestPath = total
        bestVerticle = vert

choice = input("Path or closed path? [p/c]: ")
for w in range (1,101):
    szukaj(w, choice)


print("Shortest path starts from node {0} and is equal to: {1}".format(bestVerticle, shortestPath))
