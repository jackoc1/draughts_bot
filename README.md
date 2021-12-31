# Overview
The reason I created this project is to practice software design while including an AI component in the form of a bot  
to familiarise myself with algorithms used in machine learning and AI.  

This project is built exclusively in Python since understanding and not performance is my main goal. Python is also the  
standard language for most machine learning projects if I end up including and bots capable of being trained, rather than  
brute forcing moves.

# draughts_bot
The draughts_bot repository contains two packages:
1. draughts
2. draughts_bots

## draughts
A package which contains the modules necessary for a basic implementation for a playable game of draughts.

|        Module         | Description                                                              |
|:---------------------:|:-------------------------------------------------------------------------|
|       board.py        | Logical backend for managing the game state and enforcing the game rules |
|       player.py       | Allows players human/bot to interact with the board                      |
|  terminal_display.py  |                                                                          |
| graphical_display.py  |                                                                          |

* __board__: a logical backend for managing the game state and enforcing compliance with the game's rules at all times.
* __player__: allows human players to manually interact with the game board.
* __graphical/terminal__: displays the board and player choices (if human) to either a terminal or graphical window.

## draughts_bots
A package which contains different draughts_bots designed to be usable in the draughts module as well as other draughts
games so long as game state is converted to a readable form by the bot.

For now just contains an alpha-beta minimax bot although more can be added.

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