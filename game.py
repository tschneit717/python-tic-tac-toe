class Game:
    win_status = False
    active_player = "x"
    turn = 0
    moves = {
        1 : " ",
        2 : " ",
        3 : " ",
        4 : " ",
        5 : " ",
        6 : " ",
        7 : " ",
        8 : " ",
        9 : " " 
    }

    def check_columns(self):
        if self.turn >= 5:
            for i in range(1, 4):
                if self.moves[i] == self.moves[i + 3] == self.moves[i + 6] and self.moves[i] == self.active_player:
                    self.win_status = True
                    break;

    def check_rows(self):
        if self.turn >= 5:
            for i in range(1, 9, 3):
                if self.moves[i] == self.moves[i + 1] == self.moves[i + 2] and self.moves[i] == self.active_player:
                    self.win_status = True
                    break;

    def check_diagonal(self):
        if self.turn >= 5:
            for i in range(1, 4, 2):
                if self.moves[i] == self.moves[5] and self.moves[i] == self.active_player:
                    if (i == 1 and self.moves[i + 8] == self.moves[i]) or (i == 3 and self.moves[i + 4] == self.moves[i]):
                        self.win_status = True
                        break;


    def check_for_win(self):
            self.check_columns(self)
            self.check_rows(self)
            self.check_diagonal(self)
            if self.win_status == True:
                print("We have a winner! Congratulations, {}!".format(self.active_player))
            else:
                if self.turn == 9:
                    print("Game over! No one won")
                else:
                    self.swap_player(self)
                    self.player_turn(self)

    def render_board(self):
        vertical_bars = "{0:5}|{0:5}|{0:5}".format(" ")
        horizontal_bars = "{0}{1}{0}{1}{0}".format("-" * 5, "|")
        row = "{0:^5}|{1:^5}|{2:^5}"

        for i in range(11):
            if i == 1:
                print(row.format(self.moves[1], self.moves[2], self.moves[3]))
            elif i == 5:
                print(row.format(self.moves[4], self.moves[5], self.moves[6]))
            elif i == 9:
                print(row.format(self.moves[7], self.moves[8], self.moves[9]))
            elif i == 3 or i == 7:
                print(horizontal_bars)
            else:
                print(vertical_bars)


    def swap_player(self):
        self.active_player = "x" if self.turn % 2 == 0 else "o"
        if self.active_player == "x":
            print("It's player x's turn, please enter your move: ")
        else:
            print("It's player o's turn, please enter your move: ")


    def check_for_valid_action(self):
        action = int(input("Enter your coordinate from 1 to 9: "))
        is_valid = False
        while not is_valid:
            if action < 0 or action > 9:
                print("That is not a valid coordinate!")
                action = int(input("Enter your coordinate from 1 to 9: "))
            if self.moves[action] != " ":
                print("That space is already occupied!")
                action = int(input("Enter your coordinate from 1 to 9: "))
            else: 
                is_valid = True
                self.moves[action] = self.active_player
                self.turn += 1



    def player_turn(self):
        self.check_for_valid_action(self)
        self.render_board(self)
        self.check_for_win(self)
    
    def start_game(self):
        print("Welcome to my game, would you like to play? ")

        self.render_board(self)
        self.player_turn(self)

    
Game.start_game(Game)