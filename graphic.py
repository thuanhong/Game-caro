import pyglet
from resource import *


class chess:
    def __init__(self, x, y, img = None):
        self.x = x
        self.y = y
        if img != None:
            self.sprite = pyglet.sprite.Sprite(img)
            self.sprite.x = self.x
            self.sprite.y = self.y

    def draw(self):
        self.sprite.draw()


class gameMain(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img = pyglet.image.load('img/board.png')
        self.chess_board = chess(0, 0, self.img)

        self.chess_x = pyglet.image.load('img/x.png')
        self.chess_o = pyglet.image.load('img/o.png')
        self.frame_rate = 1/60.0
        self.player = 'X'
        self.win = False
        self.cur_player = pyglet.text.Label('Player : X', y=500, x=10, font_size = 25)

        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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

    def reload(self): # reload game
        self.player = 'X'
        self.win = False

        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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

    def on_draw(self):
        self.clear()
        self.chess_board.draw()

        for x in range(16): # draw chess on display
            for y in range(16):
                if self.board[x][y] == 'X':
                    chess(x*30, y*30, self.chess_x).draw()
                elif self.board[x][y] == 'O':
                    chess(x*30, y*30, self.chess_o).draw()

        if check_draw(self.board): # draw when the chess board is no avaiable
            self.result = pyglet.text.Label('DRAW ' + ", Click E to exit, press R to reload",
                                                    y=500, x=10, font_size = 25)
            self.result.draw()
        elif self.win: # when X win or O win
            self.result = pyglet.text.Label('Congartulation player ' + self.player + ' win'
                                                  + ", Click E to exit, press R to reload",
                                                    y=500, x=10)
            self.result.draw()
        else: # draw current player
            self.cur_player.draw()

    def on_mouse_press(self, x, y, button, modifiers): # take mouse event
        if button == pyglet.window.mouse.LEFT and not self.win:
            try:
                if self.board[int(x/30)][int(y/30)] == ' ': # when click on the square contain " "
                    if not handle_main(int(x/30), int(y/30), self.player, self.board):
                        if self.player == 'X':
                            self.player = 'O'
                        else:
                            self.player = 'X'
                        self.cur_player.text = 'Player : ' + self.player
                    else:
                        self.win = True
            except: # except error Out IndexList when click outside chess board
                pass

    def on_key_press(self, button, modifiers): # take keyboard event
        if button == pyglet.window.key.R:
            self.reload()
        if button == pyglet.window.key.E:
            pyglet.app.exit()

    def update(self, dt):
        pass


if __name__ == '__main__':
    window = gameMain(600, 600, 'Caro')
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
