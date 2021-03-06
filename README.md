# Zork-clue-code

Project Description

Zork-Clue is a text based game with a fully functional tile map, where the player can move around using text commands, 
the objective of the game is to find a weapon in one of the tiles on the map. 
The player will be given clues to navigate around the playing board ,
the board has multiple rooms and hallways with walls and doors to restrict the player from moving in all directions , 
when he reaches the location of the weapon the game will terminate. 
The player can move one tile for each move.The player has to find the weapon in the least possible amount of moves. 

Expected Outcome 

The expected outcome of the game is for the player to find the weapon with the least number of moves. 
In doing so the player can come up with a score (the number of moves taken by the player to find the weapon) ,
keep in mind that the scoring system in zork-clue is like the scoring system in golf, 
the leader is the one with the lowest score.

Structure for i/o

When the game starts, there is a description of the story behind the game and the objective of the game. 
The player is then expected to navigate through the gui, a picture of the map is shown for the player’s reference, 
this screen also shows the player what type of text inputs the interpreter will understand while the game is executed.
The user will then be displayed a text box to enter his input, 
repeatedly until the objective is completed.


The build of the project initially did not follow object oriented programming. 
It was a procedural approach to the problem at hand, but on refactoring and refining the original project, 
classes and objects have been created to follow an object oriented approach, this allowed for the end product to have multiplayer functionality, 
modularity and reusability even though the code has not been written for multiple players to play, with a couple of tweaks it can be achieved.

