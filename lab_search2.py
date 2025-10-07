print("This is your BOOK!!!")
s = input("Enter input: ")
shelf_str, requests_str = s.split("/")
shelf = shelf_str.split()
requests = requests_str.split()

counter = set()

total_cost = 0

for req in requests:
    if req in shelf:
        pos = shelf.index(req) + 1  # price ตาม position
        total_cost += pos
        print(f"Search {req} -> found at {pos} move to front -> ", end=" ")
        shelf.remove(req)
        shelf.insert(0, req)
        print(" ".join(shelf))
    elif req in counter:  # repeat = add new
        total_cost += 1
        print(f"Search {req} -> add new book -> ", end=" ")
        counter.remove(req)
        shelf.insert(0, req)
        print(" ".join(shelf))
    else:
        cost = len(shelf) + 1
        total_cost += cost
        print(f"Search {req} -> not found ->", end=" ")
        print(" ".join(shelf))
        counter.add(req)

print("\nFinal books:", " ".join(shelf))
print("Total cost:", total_cost)
