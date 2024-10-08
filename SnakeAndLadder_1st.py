class Jumper():
    start: int
    end: int

    def __init__(self, start:int, end: int) -> None:
        self.start = start
        self.end = end

class Board:
    players: list

    def __init__(self, players: int) -> None:
        self.players = [0]*players
        print(self.players)

    def add_jumpers(self, jumpers: list[Jumper]):
        self.jumpers = jumpers

    def move_player(self, player: int, step: int ) -> bool:
        player_index = player-1
        if self.players[player_index] == 0:
            if step == 6:
                self.players[player-1] = 1
        
        elif self.players[player_index]+step == 100:
            print(f"Player {player} own the match")
            return True
        
        elif(self.players[player_index] +step < 100):
            self.players[player_index] += step
        
        for jumper in self.jumpers:
            if jumper.start == self.players[player_index]:
                self.players[player_index] = jumper.end
            
        return False
    
    def print_players_position(self) -> None:
        print(self.players)
    
import random
class Dice:
    
    def roll_dice(self) -> int:
        return random.randint(1,6)
    

dice = Dice()


players_count = 4
board = Board(players_count)
jumpers = [Jumper(4, 14), Jumper(8, 30), Jumper(28, 65), Jumper(21, 42), Jumper(50, 67), 
           Jumper(71, 92), Jumper(88, 99),
           Jumper(32, 10), Jumper(36, 6), Jumper(48, 26), Jumper(62, 18),  Jumper(88, 24),
           ]

board.add_jumpers(jumpers=jumpers)
is_game_over = False
player = 1
while(not is_game_over):
    step = dice.roll_dice()
    print(f"Player: {player} with step: {step}")
    is_game_over = board.move_player(player, step)
    board.print_players_position()
    player = 1 if player + 1 > players_count else player+1
    input()
