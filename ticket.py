import json

print("======== WELCOME TO TICKET CREATION SYSTEM ========")

title = ""

while not title:
    title = input("\nEnter title: ")
    title = title.strip()
    
    if not title:
        print("Title must not be Empty!")
    else:
        break

description = ""

while not description:
    description = input("Enter the description: ")
    description = description.strip()
    
    if not description:
        print("Description can't be empty!")
    else:
        break

try:
    with open("tickets.json", "r") as file:
        tickets = json.load(file)
except FileNotFoundError:
    tickets = []
except JSONDecodeError:
    tickets = []


next_uid = len(tickets) + 1
ticket_id = f"A{next_uid:03d}"


ticket = {
    "id": ticket_id,
    "title": title,
    "description": description  
}

tickets.append(ticket)

with open("tickets.json", "w") as file:
    json.dump(tickets, file, indent=4)

print("\n Ticket created successfully")
print(f"ID: {ticket_id}\nTitle: {title}\nDescription: {description}")