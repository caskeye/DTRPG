from base import Player

player = Player("Bryan")

player.connect()
while True:
    player.take_turn(input('Player:'))
