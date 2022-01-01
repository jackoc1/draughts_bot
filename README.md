# Overview
The reason I created this project is to practice software design while including an AI component in the form of a bot  
to familiarise myself with algorithms used in machine learning and AI.  

This project is built exclusively in Python since understanding and not performance is my main goal. Python is also the  
standard language for most machine learning projects, which will be handy if I end up including any bots capable  
of being trained, rather than just brute forcing moves with a state space search.

# draughts_bot
The draughts_bot repository contains two packages:
1. draughts
2. draughts_bots

## draughts
A package which contains the modules necessary for a basic implementation for a playable game of draughts.

|        Module        | Description                                                                                     |
|:--------------------:|:------------------------------------------------------------------------------------------------|
|       board.py       | Logical backend for managing the game state and enforcing the game rules.                       |
| player_interface.py  | Abstract base class which bot and player must implement to ensure functionality with the board. |
|      player.py       | Allows human players to interact with the board.                                                |
|        bot.py        | Makes use of bots in draughts_bots decisions to automatically interact with the board.          |
| terminal_display.py  | Frontend which displays a basic draughts board in ASCII form as well as any textual game info.  |
| graphical_display.py | Frontend which displays a GUI for players to play draughts or to watch bots play.               |


## draughts_bots
A package which contains different draughts_bots designed to be usable in any draughts game so long as game state is  
converted to a readable form by the bot.

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

# Running tests
...

_Note: There are no tests for the display modules as I'm not sure how to go about unit testing a UI._

# Contributing
When this is actually a working release if you'd like to make pull requests for improvements to the graphcial UI,  
optimisations to the draughts engine or just creating your own draughts bot for others to play against feel free to  
do so.  

You can include any info for accreditation at the top of your bots source file if you would like e.g. GitHub account name.
