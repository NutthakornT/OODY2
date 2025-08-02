def hbd(age):
    for base in range(2, age + 1):

        num1 = 2 * base + 0

        num2 = 2 * base + 1
        print(f"trying base : {base}, '20'={num1}, '21' = {num2}")
        if num1 == age:
            return f"saimai is just 20, in base {base}!"
        elif num2 == age:
            return f"saimai is just 21, in base {base}!"

    return "No suitable base found."


year = input("Enter year : ")
print(hbd(int(year)))

# trying base : 2, '20'=4, '21' = 5
# trying base : 3, '20'=6, '21' = 7
# trying base : 4, '20'=8, '21' = 9
# trying base : 5, '20'=10, '21' = 11
# trying base : 6, '20'=12, '21' = 13
# trying base : 7, '20'=14, '21' = 15
# trying base : 8, '20'=16, '21' = 17
# trying base : 9, '20'=18, '21' = 19
# trying base : 10, '20'=20, '21' = 21
# trying base : 11, '20'=22, '21' = 23
# trying base : 12, '20'=24, '21' = 25
# trying base : 13, '20'=26, '21' = 27
# trying base : 14, '20'=28, '21' = 29
# trying base : 15, '20'=30, '21' = 31
# trying base : 16, '20'=32, '21' = 33
# trying base : 17, '20'=34, '21' = 35
# trying base : 18, '20'=36, '21' = 37
# trying base : 19, '20'=38, '21' = 39
# trying base : 20, '20'=40, '21' = 41
# trying base : 21, '20'=42, '21' = 43
# trying base : 22, '20'=44, '21' = 45
# saimai is just 21, in base 22!
