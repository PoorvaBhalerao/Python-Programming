# Tuple datatype

# Heterogeneous
# Unordered
# UnIndexed
# Mutable
# Duplicate not Allowed

Arr = {11, 18.90, True, "Marvellous",11}
print(Arr)  # error not came but 11 is printed only once

# print(Arr[0]) #error data is not indexed

Arr.add("Python")
print(Arr)

Arr.discard("Python")
print(Arr)

Arr.remove(18.90)
print(Arr)

print(len(Arr))