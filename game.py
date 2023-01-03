print("Welcome to my game, would you like to play? ")
vertical_bars = "{0:5}|{0:5}|{0:5}".format(" ")
horizontal_bars = "{0}{1}{0}{1}{0}".format("-" * 5, "|")
row = "{0:^5}|{1:^5}|{2:^5}"

class Game:
    turn = 0
    moves = []

    def check_for_win(self):
        if self.turn > 9:
            print("Game over!")
        else:
            self.player_turn(self)

    def render_board(self):
        for i in range(11):
            if i == 1:
                print(row.format(" ", " ", " "))
            elif i == 5:
                print(row.format(" ", " ", " "))
            elif i == 9:
                print(row.format(" ", " ", " "))
            elif i == 3 or i == 7:
                print(horizontal_bars)
            else:
                print(vertical_bars)


    def check_for_valid_turn(self):
        action = int(input("Enter your coordinate from 1 to 9: "))
        is_valid = False
        while not is_valid:
            if action < 0 or action > 9:
                print("That is not a valid coordinate!")
                action = int(input("Enter your coordinate from 1 to 9: "))
            if action in self.moves:
                print("That space is already occupied!")
                action = int(input("Enter your coordinate from 1 to 9: "))
            else: 
                is_valid = True
                self.moves.append(action)
                self.turn += 1



    def player_turn(self):
        if self.turn % 2 == 0:
            print("It's player x's turn, please enter your move: ")
        else:
            print("It's player o's turn, please enter your move: ")
        self.check_for_valid_turn(self)
        self.render_board(self)
        self.check_for_win(self)
    
    def start_game(self):
        self.render_board(self)
        self.player_turn(self)

    
Game.start_game(Game)