#a
square = list(map(lambda x : x**2, range(1,11)))
lessThanOne = list(map(lambda x : x-1, range(1,11)))

#b
largerThanSix = [x for x in range(1,11) if x >=6]
threePowerEven = [x**3 for x in range(1,11) if x%2 == 0]

print(square)
print(lessThanOne)
print(largerThanSix)
print(threePowerEven)