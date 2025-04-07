#this file will create a loops that will loop through movies tickets and give a price
prompt = "\nEnter the age of ticket holder"
prompt += "\nEnter quit when you are done: "

active = True
ticket_number = 0
int(ticket_number)


while active:
    response = input(prompt)
    if response.isdigit():
        response = int(response)
        ticket_number = ticket_number + 1
        if response < 3:
            print("Because the child is younger than three, the ticket is free")
        elif response < 12:
            print("The ticket for a child between 3 and 12 is 10 dollars")
        elif response > 12:
            print("The ticket price for children over 12 is 15 dollars")
        else:
            active = False
    elif response == 'quit':
        active = False
    else:
        print("Please enter an age and not jibberish")

ticket_number = str(ticket_number)    
print(f"The number of tickets you are using is {ticket_number}")

    