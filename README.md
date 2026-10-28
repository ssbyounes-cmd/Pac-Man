### Project Management
## Rules: please use + to indicate a new addition and - to indicate a deletion.

05/10/2026 - ychoucho:
+ Created a virtual environment using "uv init" and installed both pygame and the mazegenerator package.
+ Built MenuState with functional Start/Quit buttons and PlayingState that successfully parses and renders the imperfect maze from the external mazegenerator package.
The Game class is the engine that keeps running the game loop, handling events, and managing state transitions. (please have a look at the UML diagram for a better understanding of the architecture)

The game now starts in the menu state, and clicking "Start" transitions to the playing state (which has just the maze rendered for now), while "Quit" exits the game. 
+ Adjusted screen dimensions for menu and playing states. (Menu: 800x600, Playing: is based on maze size)
+ Added a Makefile for easy installation and running of the game. Use "make install" to set up the environment and "make run" to start the game.









13/10/2026 - ychoucho:
+ Added pygame.time.clock to manage time and control the frame rate of the game loop. clock.tick() 
returns the number of milliseconds that have passed since the last call to tick(), which help for example
track each frame and update the game state accordingly.
+ Added a Sparkle class to create a visual effect in the menu state. The sparkles move upwards at random speeds and reset to the bottom of the screen when they go off the top. their coordinates in each frame
get updated based on the elapsed time.
+ Added a button class to handle button rendering and click detection.
+ Adjusted maze rendering to leave an empty space at the top of the screen for the score display (50 pixels) given that the highest maze height and width is 22 and 29 respectively.









23/10/2026 - ychoucho:
+ Added get_pixel_pos() method to convert maze cell coordinates to pixel coordinates for rendering.
The intended logic is to use this method to position entities based on their movement within the maze.
The game engine will work with just cell coordinates (len(self.cells[0]), len(self.cells)), and the rendering will handle the conversion to pixel coordinates for display. 

+ Separated maze rendering from playing state class to a separate maze class.

+ Added the two left buttons of Instructions and Score to the menu state. Clicking on "Instructions" transitions to the instructions state, while clicking on "High Scores" transitions to the score state. Escape key can be used to return to the menu state for both states. (Work still in progress for the new pages. UI enhancements are going to be added later.)

+ Added a simple pause state that can be accessed by pressing the spacebar. The pause state displays a "PAUSED" message and allows the player to resume the game by pressing the spacebar again or returning to the main menu.
+ Added a highscore page (its content is going to be updated later) and an instructions page (its content is going to be updated later) to the game. Both pages can be accessed from the menu state and return to the menu state by pressing the escape key.



27/10/2026 - ychoucho:
+ Added several UI elements for all pages (Title, background, HUD bar, panels, small widgets for time, lives, level, and score). 


