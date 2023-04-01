exchange_rate = {"Euro": 1.11,
                 "USD": 2.22,
                 "INR":0.22
                 }

print(exchange_rate["Euro"]) # access key of INR

exchange_rate["INR"] = 1.4

print(exchange_rate)

exchange_rate["UAE"] = 2.3  # adding new pair to dist

print(exchange_rate)

print({**exchange_rate, **{"PAK": 0.22, "USD": 3.22}})  # merging with asterisk 

print(exchange_rate | {"PAK": 0.22, "USD": 3.22})       #merging with pipe 

# we can aslo use string as key in dist

dist = {1: "one", 2: "two", 3: "three"}
print(dist[1])

