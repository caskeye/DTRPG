from base import Player

player = Player("Dudecles")

player.connect()
while True:
    player.take_turn(input('Player:'))
