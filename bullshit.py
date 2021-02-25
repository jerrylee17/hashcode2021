from output import output
def parseData(inputFile):
    '''
    Returns a tuple: 
    ((D, I, F), streets, paths)
    '''

    # Read lines
    with open(inputFile, 'r') as f:
        data = f.readlines()
    # Current read index
    ci = 0
    D, I, S, V, F = list(map(int, data[ci].split()))
    ci += 1

    streets = []
    for _ in range(S):
        # each entry has b, e, l
        street = data[ci].split()
        street[0] = int(street[0])
        street[1] = int(street[1])
        street[3] = int(street[3])
        streets.append(street)
        ci += 1

    paths = []
    for _ in range(V):
        path = data[ci].split()
        path[0] = int(path[0])
        paths.append(path)
        ci += 1
    return ((D, I, F), streets, paths)

class intersection:
    def __init__(self, n):
        self.number = n
        self.cycle = []

filename = 'b.txt'

constants, streets, cars = parseData(filename)
D, I, F = constants


intersections = []
for i in range(I):
    me = intersection(i)
    intersections.append(me)

for r in streets:
    s, e = r[0], r[1]
    # intersections[s].cycle.append((r[2], 1))
    intersections[e].cycle.append((r[2], 10))

output(f'{filename[0]}-result.txt', intersections)

filename = 'c.txt'

constants, streets, cars = parseData(filename)
D, I, F = constants


intersections = []
for i in range(I):
    me = intersection(i)
    intersections.append(me)

for r in streets:
    s, e = r[0], r[1]
    # intersections[s].cycle.append((r[2], 1))
    intersections[e].cycle.append((r[2], 10))

output(f'{filename[0]}-result.txt', intersections)

filename = 'd.txt'

constants, streets, cars = parseData(filename)
D, I, F = constants


intersections = []
for i in range(I):
    me = intersection(i)
    intersections.append(me)

for r in streets:
    s, e = r[0], r[1]
    # intersections[s].cycle.append((r[2], 1))
    intersections[e].cycle.append((r[2], 10))

output(f'{filename[0]}-result.txt', intersections)

filename = 'e.txt'

constants, streets, cars = parseData(filename)
D, I, F = constants


intersections = []
for i in range(I):
    me = intersection(i)
    intersections.append(me)

for r in streets:
    s, e = r[0], r[1]
    # intersections[s].cycle.append((r[2], 1))
    intersections[e].cycle.append((r[2], 10))

output(f'{filename[0]}-result.txt', intersections)

filename = 'f.txt'

constants, streets, cars = parseData(filename)
D, I, F = constants


intersections = []
for i in range(I):
    me = intersection(i)
    intersections.append(me)

for r in streets:
    s, e = r[0], r[1]
    # intersections[s].cycle.append((r[2], 1))
    intersections[e].cycle.append((r[2], 2))

output(f'{filename[0]}-result.txt', intersections)