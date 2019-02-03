def check_draw(board): # check state draw
    for x in board:
        if ' ' in x:
            return False
    return True


def handle_main(x, y, player, board):
    def check_win(x, y, player, board): # True if either of my two player win

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

    board[x][y] = player
    return check_win(x, y, player, board)
