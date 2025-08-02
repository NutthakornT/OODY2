# def new_range():
#     print("*** New Range ***")
#     inp = input("Enter Input : ")
#     numlst = list(map(float, inp.strip().split()))
#     result = []

#     if len(numlst) == 1:
#         start, end, step = 0.0, numlst[0], 1.0
#     elif len(numlst) == 2:
#         start, end, step = numlst[0], numlst[1], 1.0
#     elif len(numlst) == 3:
#         start, end, step = numlst[0], numlst[1], numlst[2]

#     while step > 0 and start < end:
#         result.append(round(start, 3))
#         start += step

#     print(tuple(result))


# new_range()
