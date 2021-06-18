from board import Board

if __name__ == "__main__":
    game_board = Board(rocks=3)
    counter = 0
    while True:
        player = "B" if counter % 2 else "A"
        counter += 1
        name = input(f"Get player {player} hole name: ")
        status, message = game_board.scatter(name)
        if not status:
            print(message)
            counter -= 1
            continue
        game_board.draw()
