first_grid = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

player = "X"


def display_grid(grid):
    print("-------------")
    for i in range(3):
        print("| ", end='')
        for j in range(3):
            print(grid[i][j] + " |", end=' ')
        print()
        print("-------------")


def change_grid(grid, position):
    if position[0] < 0 or position[0] > len(grid)-1 or position[1] < 0 or position[1] > len(grid[0])-1:
        print("You choose nonexistent position")
        select_position(grid)
    else:
        global player
        if grid[position[0]][position[1]] == '.':
            if player == "X":
                grid[position[0]][position[1]] = "X"
                player = "O"
            else:
                grid[position[0]][position[1]] = "O"
                player = "X"
        else:
            print("Choose other position")
            select_position(grid)


def select_position(grid):
    print(f"\n{player}'s move")
    try:
        line = int(input("Choose line: "))
        column = int(input("Choose column: "))
        change_grid(grid, [line-1, column-1])
    except ValueError:
        print("you didn't enter a number")


win = False
winner = ""


def start_game(grid):
    while not win:
        check_winner(grid)
        if win:
            if winner:
                print(f"Winner: {winner}")
            else:
                print("No winner")
            return
        select_position(grid)
        display_grid(grid)


def check_winner(grid):
    global win, winner

    has_empty_position = False

    for line in grid:
        if line[0] == line[1] == line[2] != ".":
            win = True
            winner = line[0]
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] != ".":
            win = True
            winner = grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] != ".":
        win = True
        winner = grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] != ".":
        win = True
        winner = grid[0][2]

    for i in grid:
        for j in i:
            if j == ".":
                has_empty_position = True

    if not has_empty_position:
        win = True


start_game(first_grid)
