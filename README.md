# Overview
The reason I created this project is to practice software design while including an AI component in the form of a bot  
to familiarise myself with algorithms used in machine learning and AI.  

This project is built exclusively in Python since understanding and not performance is my main goal. Python is also the  
standard language for most machine learning projects, which will be handy if I end up including any bots capable  
of being trained, rather than just brute forcing moves with a state space search.  

I chose draughts over chess because the rules are much simpler to implement and the goal isn't to implement the  
most complex game possible. 

# draughts_bot
The draughts_bot repository contains two packages:
1. draughts
2. draughts_bots

## draughts
A package which contains the modules necessary for a basic implementation for a playable game of draughts.

|   Module    | Description                                                                                 |
|:-----------:|:--------------------------------------------------------------------------------------------|
|  board.py   | Game board which keeps track of a player's draughts pieces and their movements.             |
| draughts.py | Backend for managing game logic and getting player moves.                                   |
|  player.py  | Allows human/bot players to interact with the draughts game class.                          |
| display.py  | Terminal/Graphical frontend which displays an interactive draughts board and any game info. |


## draughts_bots
A package which contains different draughts_bots designed to be usable in any draughts game so long as game state is  
converted to a readable form by the bot.

For now just contains a random choice, basic heuristic and alpha-beta minimax bot although more can be added.

# Usage
play_draughts.py takes three mandatory command line arguments.

|    Argument     | Description                                                                                                                                                             |
|:---------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --player1 / -p1 | "human" if the first player is human, else relative file path to bot program from root directory.                                                                       |
| --player2 / -p2 | "human" if the second player is human, else relative file path to bot program from root directory.                                                                      |
| --display / -d  | "terminal" if using terminal ASCII board visuals, "graphical" for a board GUI to pop up.                                                                                |



### Example 1
``python play_draughts.py --player1=human --player2=human --display=graphical``

### Example 2
``python play_draughts.py -p1=human -p2=draughts_bots/alphabeta_minimax_draughts_bot.py -d=terminal``

# Running tests
...

_Note: There are no tests for the display modules as I'm not sure how to go about unit testing a UI._

# Contributing
When this is actually a working release if you'd like to make pull requests for improvements to the graphcial UI,  
optimisations to the draughts engine or just creating your own draughts bot for others to play against feel free to  
do so.  

You can include any info for accreditation at the top of your bots source file if you would like e.g. GitHub account name.
