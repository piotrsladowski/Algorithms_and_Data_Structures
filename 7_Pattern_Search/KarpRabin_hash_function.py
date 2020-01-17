values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def createHash(a,b,c):
    hash = 0
    hash = values[c] + 16 * values[b] + (16**2)*values[a]
    hash = hash % 2767
    return hash

def changeHash(h, prev, next):
    hash = (h - ((16**2 % 2767) * values[prev])) % 2767
    hash = (hash * 16) % 2767
    hash = (hash + values[next]) % 2767
    return hash

