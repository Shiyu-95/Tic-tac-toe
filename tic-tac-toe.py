def hello():
    print('Welcome in my first mini-project tic-tac-toe')
    print("Please write your move as horizontal vertical from 0 to 2 e.g. 12")


def show():
    print(f'  0 1 2')
    for i in range(3):
        row_info = " ".join(board[i])
        print(f"{i} {row_info}")


def game_going():
    while True:
        cords = input("         your move: ".split())

        if len(cords) != 2:
            print("Write 2 coordinates")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print('It should be numbers')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Choose from 0 to 2")
            continue

        if board[x][y] != " ":
            print("this spot is not empty")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


hello()
board = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print('X is moving')
    else:
        print('0 is moving')

    x, y = game_going()

    if num % 2 == 1:
        board[x][y] = 'X'
    else:
        board[x][y] = '0'

    if check_win():
        break

    if num == 9:
        print("draw")
        break


