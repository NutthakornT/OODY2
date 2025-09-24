def insertion_sort(unsorted, sorted_list=None):
    """Recursive insertion sort for ranking teams by points, then GD."""
    if not unsorted:
        return sorted_list

    if sorted_list is None: #first
        sorted_list = [unsorted.pop(0)]

    team = unsorted.pop(0) #start at second team
    sorted_list = insert_team(sorted_list, team)
 
    return insertion_sort(unsorted, sorted_list) #loop


def insert_team(sorted_list, team, index=0):
    
    points, gd = team[1]['points'], team[2]['gd']

    # insert at the end
    if index + 1 >= len(sorted_list):
        return insert_at_end(sorted_list, team, index)

    current_points = sorted_list[index][1]['points']
    next_points = sorted_list[index + 1][1]['points']

    #between
    if points > current_points and points < next_points:
        sorted_list.insert(index + 1, team)
        return sorted_list

    # point = current but < next
    if points >= current_points and points < next_points:
        if gd > sorted_list[index][2]['gd']:
            sorted_list.insert(index + 1, team)#place after current if gd>
        else:
            sorted_list.insert(index, team)
        return sorted_list

    
    if points < current_points:
         # Insert before the current
        sorted_list.insert(index, team)
        return sorted_list

    
    return insert_team(sorted_list, team, index + 1)


def insert_at_end(sorted_list, team, index):
    
    points, gd = team[1]['points'], team[2]['gd']
    last_team = sorted_list[-1]

    if points > last_team[1]['points']:
        sorted_list.insert(index + 1, team)

    elif points == last_team[1]['points']:
        if gd > last_team[2]['gd']:
            sorted_list.insert(index + 1, team)
        else:
            sorted_list.insert(index, team)

    else:
        sorted_list.insert(index, team)

    return sorted_list



inp = input("Enter Input : ").split("/")
teams = []

for record in inp:
    values = record.split(",")
    name = values.pop(0)

    wins, draws, losses, goals_for, goals_against = map(int, values)
    points = wins * 3 + draws * 0 + losses * 1  
    gd = goals_for - goals_against

    teams.append([name, {"points": points}, {"gd": gd}])


sorted_teams = insertion_sort(teams)


print("== results ==")
for i in range(len(sorted_teams) - 1, -1, -1):
    print(sorted_teams[i])
