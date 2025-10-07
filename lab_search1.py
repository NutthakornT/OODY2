inp = input("Enter Input : ")
print()
inp, target = inp.split("/")
inp = list(map(float, inp.strip().split(" ")))
target = int(target)
last = len(inp) - 1
first = inp[0]
# print(first)
if target > inp[last]:
    index = 999
    percentile = 100
    print(f"index      :   {index}")
    print(f"percentile :   {percentile}")
elif target < first:
    index = -1
    percentile = 0
    print(f"index      :   {index}")
    print(f"percentile :   {percentile}")

else:
    check_re = 0
    for i in range(len(inp) - 1):
        if i + 1 >= len(inp) - 1:

            break
        if inp[i] == inp[i + 1]:
            check_re = 1

    upper_value = 0
    lower_value = 0
    n = len(inp)
    decimal = target - int(target)
    lower_value = [x for x in inp if x <= target]
    lower_value = max(lower_value)
    upper_value = [x for x in inp if x >= target]
    upper_value = min(upper_value)

    lower_index = inp.index(lower_value)
    if upper_value == lower_value:  # if its in the input

        index = float(lower_index)
        if check_re == 1:
            index += 1
    else:
        # index = (upper_value - lower_value) * decimal + lower_value
        index = lower_index + (target - lower_value) / (upper_value - lower_value)
    percentile = (index + 1) * 100 / n
    if percentile == 100 or percentile == 0:
        percentile = int(percentile)
    else:
        percentile = float(percentile)
    print(f"index      :   {index}")
    print(f"percentile :   {percentile}")
pass
