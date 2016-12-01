
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def main():
    input_value = raw_input()

    visited_positions = []
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

        current_direction %= 4  # normalize direction
        all_moves = dict(movements)
        movements[current_direction] += amount

        # part 2
        for i in range(1, amount):
            all_moves[current_direction] += 1
            pos_x = all_moves[EAST] - all_moves[WEST]
            pos_y = all_moves[NORTH] - all_moves[SOUTH]
            if (pos_x, pos_y) in visited_positions:
                print 'ALREADY VISITED!', abs(pos_x) + abs(pos_y)
            else:
                visited_positions.append((pos_x, pos_y))

    move_x = abs(movements[EAST] - movements[WEST])
    move_y = abs(movements[NORTH] - movements[SOUTH])
    print 'TOTAL DISTANCE =', move_x + move_y


if __name__ == '__main__':
    main()
