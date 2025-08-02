print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
for i in range(n):
    line = "." * (n - i - 1)
    if i == 0:
        line += "*" + "+" * i
    else:
        line += "*" + "+" * (i * 2 - 1) + "*"

    line += "." * (2 * (n - i - 1) - 1)
    if i == 0:
        line += "*" + "+" * i
    elif i == n - 1:
        line += "+" * (i * 2 - 1) + "*"
    else:
        line += "*" + "+" * (i * 2 - 1) + "*"

    line += "." * (n - i - 1)
    # a single line
    print(line)
    # top part

for i in range(n * 2 - 2):
    line = "." * (i + 1)
    if i == (n * 2 - 2) - 1:
        line += "*"
    else:
        line += "*" + "+" * ((2 * (n * 2 - 2)) - ((i + 1) * 2 + 1)) + "*"

    line += "." * (i + 1)
    print(line)
