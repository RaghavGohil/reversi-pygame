# Reversi pygame (Othello™)
Reversi more like - Othello™ in this project is made in pygame for my college project.
Never knew that Othello and Reversi had differences.

There are two differences between Othello™ and Reversi.

- In Othello™, the two colours are Black and White and Black always plays first
- In Othello™, the four squares in the middle of the board start with four counters already placed - white top left and bottom right; black top right and bottom left. The reason for this is that In Reversi, the extra freedom can result in an opening that produces a less interesting game.
- In Reversi if one player cannot not play a piece, the game finishes. In Othello™, a player without a move simply passes, and the other player keeps playing pieces until the first player can make a move again.

https://github.com/RaghavGohil/reversi-pygame/assets/71706645/1828a195-7ef3-4281-9622-4fa8aa6f07d1

# How to play the game

## Setup
The game is played on an 8×8 board with disc-like gaming pieces that have a black and a white side.

At the beginning of every game four pieces, two black and two white, are put in a definite starting position in the center of the board.


## Outflanking the opponent
The black player always makes the first move.

They must place a piece with the black side up on the board in such a position that there exists at least one straight (horizontal, vertical, or diagonal) occupied line between the new piece and another black piece. One or more contiguous white pieces have to be between them. This way the player “outflanks” their opponent.

##Turning the Pieces
After placing the piece, black turns over all white pieces lying on a straight line between the new piece and any anchoring black pieces. All reversed pieces now show the black side, and the black player may use them in later moves.

Now it is the white players turn. They operate under the same rules with the roles reversed. The player lays down a white piece, causing one or more black pieces to flip.

## Winning the Game
Both players take alternate turns. Moves that do not cause the flipping of the opponents pieces are not valid. If one player cannot make a valid move, play passes back to the other player.

The game ends when the board is full of pieces or when neither player can make a valid move. The player with the most pieces on the board at the end of the game wins.

# Dependencies
Run this in the command prompt after cloning / downloading this project.
```
pip install pygame
```

# How to run
```
python main.py
```
