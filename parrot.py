prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program.  "
print(prompt)
message = ""

active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)
		print("Woo")
