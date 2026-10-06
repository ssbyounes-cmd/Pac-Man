### Project Management
## Rules: please use + to indicate a new addition and - to indicate a deletion.

05/10/2026 - ychoucho:
+ Created a virtual environment using "uv init" and installed both pygame and the mazegenerator package.
+ Built MenuState with functional Start/Quit buttons and PlayingState that successfully parses and renders the imperfect maze from the external mazegenerator package.
The Game class is the engine that keeps running the game loop, handling events, and managing state transitions. (please have a look at the UML diagram for a better understanding of the architecture)

The game now starts in the menu state, and clicking "Start" transitions to the playing state (which has just the maze rendered for now), while "Quit" exits the game. 
+ Adjusted screen dimensions for menu and playing states. (Menu: 800x600, Playing: is based on maze size)
+ Added a Makefile for easy installation and running of the game. Use "make install" to set up the environment and "make run" to start the game.

Understand Project structure Before splitting the tasks
contribution
