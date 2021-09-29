import math
import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe():
    #game itself
    def __init__(self):
        #constructor to create 3x3 board
        #also tracks the current winner
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        #printing the baord on screen
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            #printing separators to make board look good
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    #static because we dont have to pass anything 
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        #simply imposes no.'s in the rows
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        #funtion to actually make a move
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        #checks column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        #checks diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False #if all check fails

    def empty_squares(self):
        #check for empty squares
        return ' ' in self.board

    def num_empty_squares(self):
        #returns no. of empty spaces
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
        #['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #iterate while the game stills has empty squares
    #we don't have to worry about winner because we'll just return that
    #which breaks the loop
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            #if valid
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')#just an empty line
            
            if game.current_winner:
                #cause we can only win just after a move
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)