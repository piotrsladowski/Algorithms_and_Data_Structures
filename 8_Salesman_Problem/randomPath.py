from pathlib import Path
import os
import random
import math


fl = open("TSP.txt", 'r')
cities = []

for line in fl:
    s = line.replace('\n', '')
    s = s.split('\t')
    temp = []
    temp.append(float(s[1]))
    temp.append(float(s[2]))
    cities.append(temp)

cost = math.inf
path = []
indices = [i for i in range(100)]
for n in range(1):
    length = 0
    indicesShuffled = random.sample(indices, 100)
    for i in range(99):
        length += math.sqrt((cities[indicesShuffled[i]][0] - cities[indicesShuffled[i+1]][0])**2 + (cities[indicesShuffled[i]][1] - cities[indicesShuffled[i+1]][1])**2)
    # Connect first and last node
    length += math.sqrt((cities[indicesShuffled[0]][0] - cities[indicesShuffled[99]][0])**2 + (cities[indicesShuffled[0]][1] - cities[indicesShuffled[99]][1])**2)
    if length < cost:
        cost = length
    path = indicesShuffled
print(path)
print("Cost: {0}".format(cost))