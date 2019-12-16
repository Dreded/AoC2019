#https://adventofcode.com/2019/day/3
with open(r'Day3_input.txt', 'r') as f:
    data = f.read()
    WirePaths = data.split('\n')
    if WirePaths[-1] == '': WirePaths.pop() #Pop blank newline off if it exists that is added by many text editors

def getWirePoints(WirePath):
    currentPosition = [0,0]
    currentWirePoints = []
    for point in WirePath:
        direction = point[0]
        distance = int(point[1:])
        if direction == 'U':
            for _ in range(distance):
                currentPosition[1] += 1
                currentWirePoints.append(tuple(currentPosition))
        elif direction == 'D':
            for _ in range(distance):
                currentPosition[1] -= 1
                currentWirePoints.append(tuple(currentPosition))
        elif direction == 'L':
            for _ in range(distance):
                currentPosition[0] -= 1
                currentWirePoints.append(tuple(currentPosition))
        elif direction == 'R':
            for _ in range(distance):
                currentPosition[0] += 1
                currentWirePoints.append(tuple(currentPosition))
    return currentWirePoints
wires = []
for wirePath in WirePaths:
    wires.append(getWirePoints(wirePath.split(',')))
intersections = set(wires[0]) & set(wires[1])

intersectSum = []
for x,y in intersections:
    intersectSum.append(abs(x)+abs(y))
print(min(intersectSum)) #Part1

#getlist of intersections
thisSum = []
count = -1
pos = 0
for point in intersections:
    count += 1
    for wire in wires:
        if count == 0:
            thisSum.append(wire.index(point))
        if count == 1:
            thisSum[pos] += wire.index(point)
            pos += 1
print(min(thisSum))

print(2 + min(sum(wire.index(intersect) for wire in wires) for intersect in intersections)) #Part 2
