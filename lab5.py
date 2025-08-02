print("*** Fun with countdown ***")


def find_countdowns(lst):
    result = []
    i = 0
    while i < len(lst):
        if lst[i] > 1:
            countdown = [lst[i]]
            j = i + 1
            while j < len(lst) and lst[j] == countdown[-1] - 1:
                countdown.append(lst[j])
                j += 1
            if countdown[-1] == 1:
                result.append(countdown)
                i = j
            else:
                i += 1
        elif lst[i] == 1:
            result.append([1])
            i += 1
        else:
            i += 1
    return [len(result), result]


lst = list(map(int, input("Enter List : ").split()))
print(find_countdowns(lst))
