def find_area(board, x, y, val, area=None):
    if area is None:
        area = set()
    h, w = len(board), len(board[0])
    if 0 <= x < w and 0 <= y < h and board[y][x] == val and (x, y) not in area:
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
    v = board[y][x] if 0 <= x < w and 0 <= y < h else None
    area = find_area(board, x, y, v)
    print(area)

if __name__ == "__main__":
    main()
