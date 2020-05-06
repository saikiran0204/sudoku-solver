board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def valid(x, y, number):
	for i in range(0, 9):
		if board[x][i] == number or board[i][y] == number:
			return False
	box_x = x // 3
	box_y = y // 3
	for i in range(box_x*3, box_x*3+3):
		for j in range(box_y*3, box_y*3+3):
			if board[i][j] == number:
				return False
	return True


def find_last_solver():
	for i in range(8, -1, -1):
		for j in range(8, -1, -1):
			if board[i][j] == 0:
				return (i, j)
	return False



def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def main(x, y, last):
	if x == last[0] and y == last[1]:
		return True
	for i in range(x,9):
		for j in range(0, 9):
			if board[i][j] == 0:
				for k in range(1, 10):
					if valid(i, j, k):
						board[i][j] = k
						if main(i,j,last) == True:
							return True
						else:
							board[i][j] = 0
				return False



last = find_last_solver()
if last:
	if main(0,0,last):
		print_board(board)
	else:
		print("Not possible to solve")
