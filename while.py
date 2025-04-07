
prompt = "\nPlease enter the name of a city that you have visited: "
prompt += "\nEnter 'quit' to end this program. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would love to visit {city.title()}!")



   

