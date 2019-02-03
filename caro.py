from os import system

def check_win(x, y, player):

    arr = [ [[1, 0], [-1, 0]], # check 8 direction
            [[0, 1], [0, -1]],
            [[1, 1], [-1, -1]],
            [[1, -1], [-1, 1]] ]

    for h in arr:
        count = 0
        cou_ene = 0
        tmp_x = x
        tmp_y = y
        try:
            while board[tmp_x][tmp_y] != ' ': # check direction
                if board[tmp_x][tmp_y] == player:
                    count += 1
                    tmp_x += h[0][0]
                    tmp_y += h[0][1]
                else:
                    cou_ene += 1
                    break
        except:
            pass
        tmp_x = x
        tmp_y = y
        try:
            while board[tmp_x][tmp_y] != ' ': # check opposite direction
                if board[tmp_x][tmp_y] == player:
                    count += 1
                    tmp_x += h[1][0]
                    tmp_y += h[1][1]
                else:
                    cou_ene += 1
                    break
        except:
            pass

        if count >= 6 and cou_ene != 2:
            return True
    return False


def print_board(): # print chess out display
    print('  ', end=' ')
    for x in range(16):
        print(x+1, end=' ')
    print()
    for x in range(16):
        print(str(x+1)+'  ' if x < 9 else str(x+1)+' ', end='')
        for y in range(16):
            print(board[x][y] + ' ' if y < 9 else board[x][y] + '  ', end='')
        print()

if __name__ == '__main__':
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    player = 'O'
    while True:
        system('clear')
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        print_board()
        print('Player ' + player + ' (enter row) : ', end='') # input row
        row = int(input())
        print('Player ' + player + ' (enter column) : ', end='') # input column
        col = int(input())

        while row not in range(16) or column not in range(16) or board[row-1][col-1] != ' ': # when user input index wrong
            print('Something was wrong !!!, Input Again')
            print('Player ' + player + ' (enter row) : ', end='')
            row = int(input())
            print('Player ' + player + ' (enter column) : ', end='')
            col = int(input())

        board[row-1][col-1] = player
        if check_win(row-1, col-1, player):
            break

    print_board()
    print('================================Player' + player + 'win==================================')
