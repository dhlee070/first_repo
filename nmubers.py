#for value in range(1,5):
#	print(value)
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for number in range(1, 11):
#	squared_number = number ** 2
	squares.append(number ** 2)
print(squares)

digits = list(range(1,10))
digits.append(0)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
