# Memory Tiles
Console-based and unix-compatible interactive card game focusing on your memorization skills.

# How to play
Clone the repo <br />
Navigate to folder <br />
Run python3 memory.py <br />
Play!!

# Goal
Match all pairs of tiles as fast as possible. After finding all the matches, the game will output the seconds it took the player to finish.

# Game Rules
Tiles are displayed in a 2D array format and indexed starting from 0 for the row and column. Input should be in the (row, column) format. For example, in the following array:

| * * * * |<br />
| * a * * |<br />
| * * * * |<br />
| * * * * |<br />

The letter a's index is 11.
When prompted to "Guess: ", input "11".

Guess two locations. If there's a match, the lower case letters will convert to upper case letters to keep track of the matches. If there is no match, tiles will "turn around" to their astrick format.

# Levels
There are 3 levels available for the player: 1, 2, 3. <br />
Level 1 is a 2x2 matrix. <br />
Level 2 is a 4x4 matrix. <br />
Level 3 is a 4x8 matrix. <br />
