def find_area(board, x, y, val, area=None):
    if not area:
        area = set()
    h, w = len(board), len(board[0])
    if 0 <= x < w and 0 <= y < h and board[y][x] == val and (x, y) not in area:
        area.add((x, y))
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            find_area(board, x + dx, y + dy, val, area)
    return area
        
        
board = [[0, 1, 0, 0],
         [0, 1, 1, 0],
         [1, 0, 1, 1],
         [0, 0, 0, 0]]

x = int(input("x? "))
y = int(input("y? "))
val = int(input("val? "))
area = find_area(board, x, y, val)
print(area)
