import random


class Grid:

    def __init__(self):
        """Initilaizes the Grid of the Tic-Tac-Toe"""
        self.lines = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.create_grid(None, None)
        self.comp_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    def create_grid(self, row, col, shape='X'):
        """Creates the intial grid for the game.

        :parameter:
        row: Takes the row of the chosen input from the user
        col: Takes the col of the chosen input from the user
        shape(optional): Defaults to 'X' but can be overwritten to any shape"""


        print("\n\n")
        for pos, line in enumerate(self.lines):
            if pos == row:
                line[col] = shape
            print("  ", line[0], "| ", line[1], " |", line[2])
            if pos < 2:
                print("-----|-----|-----")
        print("\n\n")

    def choice(self):
        """Allows the user to choose the required position of the marker placement. Returns the row and column
        of the marker"""
        marker = input('Where would you like to place the marker?: ')

        try:
            position = int(marker[0])
            place = int(marker[1])
        except (IndexError, ValueError, TypeError):
            print("Please choose a valid number")
            self.choice()
        else:
            if (position, place) not in self.comp_list:
                print("Invalid choice - Choose another value.")
                return self.choice()
            else:
                return position, place

    def comp_turn(self, selected):

        """Sets the comp turn as a random number from the list of tuples available.
        Availability based on available positions across the grid

        :parameter
        selected: Takes the last choice of the user"""

        if selected in self.comp_list:
            self.comp_list.remove(selected)
            if len(self.comp_list) == 0:
                return True
        choice = random.choice(self.comp_list)
        self.comp_list.remove(choice)
        self.create_grid(choice[0], choice[1], shape='O')

    def check_results(self):
        """Checks the results for the TIC-TAC-TOE"""
        for rows, cols in enumerate(self.lines):
            """Checking rows wise for X and O"""
            if rows == 0:
                if cols[0] == 'X' and cols[1] == 'X' and cols[2] == 'X':
                    return True
                elif cols[0] == 'O' and cols[1] == 'O' and cols[2] == 'O':
                    return False
            if rows == 1:
                if cols[0] == 'X' and cols[1] == 'X' and cols[2] == 'X':
                    return True
                elif cols[0] == 'O' and cols[1] == 'O' and cols[2] == 'O':
                    return False
            if rows == 2:
                if cols[0] == 'X' and cols[1] == 'X' and cols[2] == 'X':
                    return True
                elif cols[0] == 'O' and cols[1] == 'O' and cols[2] == 'O':
                    return False

            """Checking columns wise for X and O"""
        if self.lines[0][0] == 'X' and self.lines[1][0] == 'X' and self.lines[2][0] == 'X':
            return True
        elif self.lines[0][1] == 'X' and self.lines[1][1] == 'X' and self.lines[2][1] == 'X':
            return True
        elif self.lines[0][2] == 'X' and self.lines[1][2] == 'X' and self.lines[2][2] == 'X':
            return True
        elif self.lines[0][0] == 'O' and self.lines[1][0] == 'O' and self.lines[2][0] == 'O':
            return False
        elif self.lines[0][1] == 'O' and self.lines[1][1] == 'O' and self.lines[2][1] == 'O':
            return False
        elif self.lines[0][2] == 'O' and self.lines[1][2] == 'O' and self.lines[2][2] == 'O':
            return False

        """Checking diagonals"""
        if self.lines[0][0] == 'X' and self.lines[1][1] == 'X' and self.lines[2][2] == 'X':
            return True
        elif self.lines[2][0] == 'X' and self.lines[1][1] == 'X' and self.lines[0][2] == 'X':
            return True
        elif self.lines[0][0] == 'O' and self.lines[1][1] == 'O' and self.lines[2][2] == 'O':
            return False
        elif self.lines[2][0] == 'O' and self.lines[1][1] == 'O' and self.lines[0][2] == 'O':
            return False
