print("*** Converting hh.mm.ss to seconds ***")
time = input("Enter hh mm ss : ")
lis = time.split(" ")
hour = int(lis[0])
min = int(lis[1])
sec = int(lis[2])


sec1 = hour * 60 * 60
sec2 = min * 60
sec3 = sec
sum_sec = sec1 + sec2 + sec3
if min < 0 or min >= 60:
    print(f"mm({min}) is invalid!")
else:
    print(f"{hour:02d}:{min:02d}:{sec:02d} = {sum_sec:,} seconds")
