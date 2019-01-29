

def initial(): 
    global data,turn,players
    players = {-1: ' ', 0: 'X', 1: 'O' }
    turn = 0
    data = [ [-1,-1,-1], [-1,-1,-1], [-1,-1,-1] ]
    WelcomeString = '*'*20 +'Welcome to the Tic Toc Toe Game' + '*'*20
    print(WelcomeString)
    print(len(WelcomeString)*'*')
    print(len(WelcomeString)*'*'+'\n'*2)

def printTurn():
    global turn
    players = { 0: 'Player 1', 1: 'Player 2' }
    print('%s Turn,'%players[turn])
def playerMove(x,y):
    if data[x][y] != -1:
        print(10*'!'+'Cannot play this field filled already'+10*'!')
        return False
    else:
        data[x][y] = turn
        return True
def checkFinishGame():
    global isFinish
    checkV = False
    checkH = False
    checkC = False

    # Checking Horizontal 
    for row in data:
        if -1 not in row:
            checkH = sum(row)%3 == 0
    # Checking Vertical 
    for col in [[row[i] for row in data ] for i in range(len(data[0]))]:
        if -1 not in col:
            checkV = sum(col)%3 == 0
    # Checking Cross
    cross =[ [data[i][i] for i in range(len(data[0]))], [data[i][i] for i in range(len(data[0])-1,-1,-1)] ] 
    for cr in cross:
        if -1 not in cr:
            checkC = sum(cr) % 3 == 0 
    
    isFinish = checkV or checkH or checkC
    return isFinish


    
def printBoard(shape='*'):
    global data,players
    starLineHorizontal = 40*'*'
    for i in range(0,7):
        line = ''
        if i%2==0:
            line = shape*13
        else:
            for j in range(0,13):
                if j%2!=0:
                    line += ' '
                elif j%4==0:
                    line += shape
                else:
                    line += players[data[i//2][j//4]]
        print(line)
            
initial()
printBoard()

while True:
    printTurn()
    coordinates = input(' Where do you want mark [ ex: 0,1]')
    coordinates = coordinates.split(',')
    if len(coordinates)==2:
        coordinates[0] = int(coordinates[0])
        coordinates[1] = int(coordinates[1])
    else:
        print('wrong coordinates')
        pass
    if coordinates[0]>-1 and coordinates[0]<3 and coordinates[1]>-1 and coordinates[1]<3:
        if not playerMove(coordinates[0],coordinates[1]):
            continue
        printBoard()
    else:
        print('Out of bound') 
    
    if checkFinishGame():
        print("Game Finish, Player %d WON "%(turn+1))
        break
    if turn==0:turn=1 
    else: turn = 0

# *************
# * X * O * X *
# *************
# * X * X * X *
# *************
# * X * X * X *
# *************

