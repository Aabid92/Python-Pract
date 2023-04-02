cities = ["Mumbai", "Dehli", "Banglore", "Nashik"]

for x in cities:
    print(x)

for x in range(10):  # using range function
    print(x)

print("\n")

for x in range(2, 10, 2):  # using range with start-stop-step

    print(x)
my_list = list(range(2, 10, 2))

print(my_list,"\n")

for i,cities in enumerate(cities):  # using enumerate for get get index number
                                    # index values pointing to index number.
    print(i,cities)
print("\n")

name_age = {"aabid" :25, "juned" :26, "usman": 23}

for x in name_age:
    print(x)

for x , name_age in name_age.items():   
    print(x,name_age)
