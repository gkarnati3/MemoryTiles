import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#beginning rules
print(bcolors.WARNING)
print('       --------------------------------')
print('      |      Welcome to Memory!        |')
print('      |   How well can you remember?   |')
print('       --------------------------------')
print(bcolors.OKGREEN)
print(' -------------------------------------------')
print('|             House Rules:                  |')
print('| Goal: Match all tiles as fast as possible |')
print('| How to play: Choose a tile (row, col)     |')
print('|              Ex. 01 --> row = 0, col = 1  |')
print('| Levels: Each level\'s board gets bigger    |')
print('|         Options = 1 2 3                   |')
print('| Matches: Capitalized (Ex. AA)             |')
print('| No Match: Lower Case Letters (Ex. ab)     |')
print(' -------------------------------------------' + bcolors.ENDC)

print(bcolors.FAIL)
name = input('Name --> ')
level = input('Level --> ')

#level 1
board1 = list('AABB')
random.shuffle(board1)
board1 = [board1[:2],
        board1[2:]]
output1 = [list('*'*2) for i in range(2)]

#level 2
board2 = list('AABBCCDDEEFFGGHH')
random.shuffle(board2)
board2 = [board2[:4],
        board2[4:8],
        board2[8:12],
        board2[12:]]
output2 = [list('*'*4) for i in range(4)]

#level 3
board3 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPP')
random.shuffle(board3)
board3 = [board3[:8],
        board3[8:16],
        board3[16:24],
        board3[24:]]
output3 = [list('*'*8) for i in range(4)]

board = list()
output = list()

if (level == "1") :
    board = board1
    output = output1
elif (level == "2") :
    board = board2
    output = output2
elif (level == "3") :
    board = board3
    output = output3
else:
    print('Bruh, there are only 3 levels.')
    exit()

ready = input('Ready(Y/N) --> ')

if (ready == 'N' or ready == 'n'):
    print('Too bad!')
    print(bcolors.ENDC)
else:
    print(bcolors.ENDC)


print('------------')

def pickATile():
    a,b = map(int, input('Guess1: '))
    print('------------')
    show_board((a,b))
    c,d = map(int, input('Guess2: '))
    print('------------')
    show_board((a,b), (c,d))
    if board[a][b] == board[c][d]:
        print(bcolors.HEADER + 'MATCH!' + bcolors.ENDC)
        output[a][b] = board[a][b]
        output[c][d] = board[c][d]
    else:
        print(bcolors.HEADER + 'NOT A MATCH!' + bcolors.ENDC)
    if any('*' in row for row in output):
        return True

def show_board(*tiles):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row, col) in tiles:
                print(board[row][col].lower(), end='', flush=True)
            else:
                print(output[row][col], end='', flush=True)
        print()

show_board()
t = time.monotonic()

while pickATile():
    pass

print('------------')
print(bcolors.WARNING)
print('Congrats,', name)
print('Time:', time.monotonic() - t, 'seconds')
print(bcolors.ENDC)