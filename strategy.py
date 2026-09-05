# strategy.py
# ============================================================
# This is the ONLY file you need to edit.
# ============================================================
#
# Your job: fill in the choose_move function below so that
# it picks a smart position instead of always picking the
# first available one.
#
# You do NOT need to touch tictactoe.py or play.py.
# Run your strategy any time with:  python play.py


def choose_move(game, player):
    """
    Decide which position to play next.

    Parameters
    ----------
    game : TicTacToe
        The current game object.

        Useful things you can do with it:
            game.available_moves()  →  list of open positions, e.g. [1, 3, 7]
            game.board              →  the full 10-element board list
                                       (board[1] through board[9] are the squares)
            game.X                  →  the string 'X'
            game.O                  →  the string 'O'

    player : str
        Who you are — either game.X or game.O.

    Returns
    -------
    int
        The position number (1-9) you want to play.
        It must be one of the numbers in game.available_moves().
    """

    # ---------------------------------------------------------------
    # Starter behavior: always pick the first open square. (this is a dumb strategy, don't use it)
    # ---------------------------------------------------------------
    # remember YOU are X. X goes first. 
    
    # Step 1: find out which moves are still available.
    open_squares = game.available_moves()
    
    # Step 2: If the center square is open, take it first.
    if 5 in open_squares:
        return 5 
    
    # Step 3: If corner 1 is available, put an X there.
    if 1 in open_squares:
        return 1

    # If corner 3 is available, put an X there.
    if 3 in open_squares:
        return 3

    # If corner 7 is available, put an X there.
    if 7 in open_squares: 
        return 7

    # If corner 9 is available, put an X there.
    if 9 in open_squares:
        return 9

    # Step 4: If corners are gone, choose an open side.
    sides = [2,4,6,8]
    for side in sides:
        if side in open_squares:
            return side
