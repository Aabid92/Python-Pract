list1 = ["one", "two", "three"]

list2 = [1, 2, 3]

print(list1+list2)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)

cell = [[1, 2, 3],
        [4, 5, 6],
        [6, 7, 8]
        ]
print(cell[1][1:])

users = ["Juned", "Usman"]

users.append("Aabid")
print(users)

users.insert(0, "Shaikh")
print(users)

users.pop(0) # pop use as method in python 

print(users)

del users[1]  # del use as statement in python 

print(users)

# some of usefull thing we can do with list

print(len(users)) # print lenght of the list

check  = "Juned" in users

print(check)

print(sorted(users))

users.sort()   # sort the original list
print(users)

