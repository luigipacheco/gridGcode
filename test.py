x = 200
y = 200
px = 10
py = 10
countX = 0
countY = 0

print("G28")

for Y in range(int(y/py+1)):

    countX = 0
    for X in range(int(x/px+1)):
        print("G01 X" + str(countX)+" Y"+str(countY))
        countX = countX + px
    countY = countY+ py