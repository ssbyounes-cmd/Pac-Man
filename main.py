from game import Game


def main():
    # Parsing logic will be done right here later on.
    # For now we just pass whatever is needed as a variable 
    WIDTH = 20
    HEIGHT = 20

    game = Game(WIDTH, HEIGHT)  # Set the width and height of the maze
    game.run()

if __name__ == "__main__":
    main()
