def hbd(age):
    for base in range(2, age + 1):

        num1 = 2 * base + 0

        num2 = 2 * base + 1
        print(f"trying base : {base}, '20'={num1}, '20' = {num2}")
        if num1 == age:
            return f"saimai is just 20, in base {base}!"
        elif num2 == age:
            return f"saimai is just 21, in base {base}!"

    return "No suitable base found."


year = input("Enter year: ")
print(hbd(int(year)))
