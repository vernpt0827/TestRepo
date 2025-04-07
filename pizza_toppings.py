prompt = "\nEnter a pizza topping and I will add it to your pizza"
prompt += "\nEnter 'quit' when you are done: "


active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"I will add {message} to you pizza")

