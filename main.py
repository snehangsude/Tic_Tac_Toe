from grid import Grid
from logo import logo


def main():
    """Initializes the class Grid and runs the program"""
    game = Grid()

    game_on = True
    while game_on:
        placement = game.choice()
        game.create_grid(placement[0], placement[1])
        end_game = game.comp_turn(placement)
        result = game.check_results()
        if result is None:
            if end_game:
                print('It\'s a Draw')
                game_on = False
        elif result:
            print('You Win')
            game_on = False
        elif not result:
            print('You Lose')
            game_on = False


if __name__ == '__main__':
    print(logo)
    main()
