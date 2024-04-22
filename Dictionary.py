print("Demonstration of Dictonary")

Price = {"Python": 2000, "Java": 1500, "C":1100, "C++":3000}

print(Price)    # {'Python': 2000, 'Java': 1500, 'C': 1100, 'C++': 3000}

print(type(Price))  #<class 'dict'>

print(Price["C"])   #1100

print(Price.keys()) #dict_keys(['Python', 'Java', 'C', 'C++'])

print(Price.values())   # dict_values([2000, 1500, 1100, 3000])

Price = {"Python": 2000, "Java": 1500, "C":1100, "C++":3000, "Java":4300}

print(Price) #Keys if we write duplicate then previous value overridden by new value