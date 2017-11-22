responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would like to climbe someday? ")

	responses[name] = response
	repeat = input("Would like to let another person respond? (yest/no) ")
	if repeat == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")
	print("Me too")