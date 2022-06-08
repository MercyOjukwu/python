from ticTacToe.board import Board
from ticTacToe.player import Player


class Game:
    def __init__(self) -> None:
        self.game_board = Board
        self.player_one = None
        self.player_two = None

    def create_player_one(self, name, sign):
        self.player_one = Player(name, sign)

    def create_player_two(self, name, sign):
        self.player_two = Player(name, sign)

    def play(self, player: Player, position: int):
        print(f"{player.name}'s turn")
        self.game_board.fill_cell(position, player.sign)

    def determine_winner(self):
        pass


