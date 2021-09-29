import random


class Player():
    #Base class
    def __init__(self, letter):
        #players entry as x or o
        self.letter = letter

    def get_move(self, game):
        #method body to override later
        pass


class HumanPlayer(Player):
    #inherited class for player's move
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #overridden method to get players move
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            #check if the square value is correct or not also check
            #if that spot is available on the board or not
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    #inherited class derived from player class
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #overridden method to get computer's move
        square = random.choice(game.available_moves())
        return square
