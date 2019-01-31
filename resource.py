def handle_main(x, y, player, board):
    def check_win(x, y, player, board):

        arr = [ [[1, 0], [-1, 0]],
                [[0, 1], [0, -1]],
                [[1, 1], [-1, -1]],
                [[1, -1], [-1, 1]] ]

        for h in arr:
            count = 0
            tmp_x = x
            tmp_y = y
            try:
                while board[tmp_x][tmp_y] == player:
                    count += 1
                    tmp_x += h[0][0]
                    tmp_y += h[0][1]
                    if count == 6:
                        return True
            except:
                pass
            tmp_x = x
            tmp_y = y
            try:
                while board[tmp_x][tmp_y] == player:
                    count += 1
                    tmp_x += h[1][0]
                    tmp_y += h[1][1]
                    if count == 6:
                        return True
            except:
                pass
        return False

    board[x][y] = player
    return check_win(x, y, player, board)
