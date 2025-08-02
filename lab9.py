def bon(w):
    total = 0
    j = 0
    for i in set(w):  # {"a","s","c","i"}
        if w.count(i) > 1:  # {"a","s","c","i","i"}
            total += (ord(i) - 96) * 4

    return total


code = input("Enter secret code : ")
print(bon(code))
