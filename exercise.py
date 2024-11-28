class Game():
    def __init__(self):
        self.turn = "x"
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None, 
        }

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    
    def play_game(self):
        print("Shall we play a game?")
        self.print_board()

        while True:
            self.place_piece()

            if self.check_winner() is not None:
                self.print_message()
                break

            if self.check_for_tie():
                self.print_message()
                break

            self.turn = 'o' if self.turn == 'x' else 'x'
            self.print_message()
        

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.tie == False and self.check_winner() == True:
            print(f'{self.winner} wins the game!')
        else:
            print(f"Play continues!")

    
    def get_move(self):
        while True:
            move = input(f"It's player {self.turn}. Enter a valid move (example: A1): ").lower()
            if move not in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
                print(f'{move} is invalid. Please try again')
            elif self.board[move] != None:
                print(f'{move} is on an occupied space. Try again')
            else:
                return move

    def place_piece(self):
        move = self.get_move()
        self.board[move] = self.turn
        self.print_board()


    def check_winner(self):
        # self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])
        winning_moves = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1']
        ]

        for winning_move in winning_moves:
            if self.board[winning_move[0]] == self.board[winning_move[1]] == self.board[winning_move[2]] != None:
                self.winner = self.board[winning_move[0]]
                return True
            else:
                None



    def check_for_tie(self):
        if self.check_winner() is None and all(self.board[position] is not None for position in self.board):
            self.tie = True
            print(f'We have a tie. Play again?')
            return True
        else:
            return False




    # def get_move(self):

# game_instance = Game()
# game_instance.play_game()

game1 = Game()
# print(game1.print_board()) # printed board
# game1.play_game()
# print(game1.print_message())
# print(game1.get_move())
# print(game1.place_piece())
# print(game1.check_winner())
# print(game1.check_for_tie())

game1.play_game()


# Your goal is to implement the following user stores:

# As a user (AAU), I want to see a welcome message at the start of a game.
# AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
# AAU, at the beginning of each turn, told whose turn it is: It’s player X’s turn!
# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
# AAU, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
# AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
# AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.