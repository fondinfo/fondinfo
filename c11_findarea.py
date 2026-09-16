def find_area(board, x, y, val, area=None):
    if area is None:
        area = set()
    if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
        return area

    if board[y][x] == val and (x, y) not in area:
        area.add((x, y))  # area is a set of points
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            find_area(board, x + dx, y + dy, val, area)
    return area


def main():
    board = [[0, 1, 0, 0],
             [0, 1, 1, 0],
             [1, 0, 1, 1],
             [0, 0, 0, 0]]
    w, h = 4, 4

    x = int(input("x? "))
    y = int(input("y? "))
    v = int(input("v? "))
    area = find_area(board, x, y, v)
    print(area)

if __name__ == "__main__":
    main()
