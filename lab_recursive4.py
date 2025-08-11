def water_f(r, c):
    up, down, left, right = 0, 0, 0, 0
    # check all direction for water to flood
    # up
    if r - 1 >= 0 and data[r - 1][c] <= data[r][c]:  # จุดบนน้อยกว่าจุดที่่น้ำอยู่ = จม
        up = 1
    # down
    if r + 1 < row and data[r + 1][c] <= data[r][c]:
        down = 1
    # right
    if c + 1 < column and data[r][c + 1] <= data[r][c]:
        right = 1
    # left
    if c - 1 >= 0 and data[r][c - 1] <= data[r][c]:
        left = 1

    data[r][c] = "99"  # mark already process for not flow back

    if up:
        # print("hi")
        water_f(r - 1, c)
    if down:
        water_f(r + 1, c)
    if right:
        water_f(r, c + 1)
    if left:
        water_f(r, c - 1)

    data[r][c] = "0"  # flood


print(" *** Water Flow ***")
n = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split("/")
# print(n) ['5,5', '13361,86412,83455,09591,34223', '2,2']
row, column = map(int, n[0].split(","))
data = [list(row) for row in n[1].split(",")]
# print(data)
initial_r, initial_c = map(int, n[2].split(","))

if row <= 0 or row >= 10 or column <= 0 or column >= 10:
    print("Error: Rows and columns must be between 1 and 9")
elif initial_r >= row or initial_c >= column:
    print("Error: Start coordinates are out of grid bounds")
else:
    water_f(initial_r, initial_c)
    for row in data:
        print("".join(row))
