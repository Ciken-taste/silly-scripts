# pprint is used to print the map in a beautiful way
import pprint
# Time is used to slow the game down
import time


# Gets the map ready.
def map_setter():
    game_map = {}

    # 10 rows from 0-9, 15 files.
    for r in range(0, 10):
        game_map["row{0}".format(r)] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pprint.pprint(game_map)
    return game_map


# Determines if a cell lives or dies.
def life_or_death(game_map):
    for row in range(0, 10):

        # current row
        observed_row = game_map["row" + str(row)]

        # Gets the neighbouring rows
        try:
            above_row = game_map["row" + str(row + 1)]
        except KeyError:
            above_row = False
        try:
            below_row = game_map["row" + str(row - 1)]
        except KeyError:
            below_row = False

        # Checks the files in the current row
        for file in range(0, 15):
            # Amount of neighbours decides if the cell will live or die
            neighbours = 0
            # Cell currently being checked
            observed_cell = observed_row[file]

            # Checks the neighbours
            for i in range(-1, 2):
                if observed_cell:
                    neighbours -= 1

                if observed_row[file + i]:
                    neighbours += 1

                if above_row[file + i]:
                    neighbours += 1

                if below_row[file + i]:
                    neighbours += 1

            if observed_cell and neighbours < 2:
                observed_cell = 0




    return game_map


def main():
    game_map = map_setter()
    while True:
        time.sleep(0.5)
        game_map = life_or_death(game_map)


if __name__ == '__main__':
    main()
