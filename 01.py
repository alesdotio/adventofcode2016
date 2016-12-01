NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def main():
    input_value = raw_input()

    movements = {
        NORTH: 0,
        EAST: 0,
        SOUTH: 0,
        WEST: 0,
    }
    current_direction = NORTH

    for action in input_value.split(', '):
        turn = action[0]
        amount = int(action[1:])

        if turn == 'R':
            current_direction += 1
        else:
            current_direction -= 1

        current_direction = current_direction % 4  # normalize direction
        movements[current_direction] += amount

    pos_x = abs(movements[NORTH] - movements[SOUTH])
    pos_y = abs(movements[EAST] - movements[WEST])
    print pos_x + pos_y


if __name__ == '__main__':
    main()
