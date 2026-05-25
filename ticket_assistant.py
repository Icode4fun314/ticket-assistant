import json
FILE_NAME = "tickets.json"
try:
    with open(FILE_NAME, "r") as file:
        tickets = json.load(file)
except FileNotFoundError:
    tickets = []
def ticket_response(issue):
    issue_lower = issue.lower()

    if "printer" in issue_lower:
        category = "Printer Issue"
        response = "Check printer connection and restart the printer."

    elif "password" in issue_lower:
        category = "Account Access"
        response = "Reset password through the account portal."

    else:
        category = "General IT Support"
        response = "Gather more information from the user."

    if "down" in issue_lower or "urgent" in issue_lower or "cannot work" in issue_lower:
        priority = "High"

    elif "slow" in issue_lower or "freezing" in issue_lower:
        priority = "Medium"

    else:
        priority = "Low"

    return {
        "issue": issue,
        "category": category,
        "priority": priority,
        "response": response
    }
def save_tickets():
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)
while True:
    user_issue = input("Enter the support issue, or type 'quit' to exit: ")

    if user_issue.lower() == "quit":
        break

    ticket = ticket_response(user_issue)
    tickets.append(ticket)
    save_tickets()

    print("\n--- Ticket Created ---")
    print("Issue received:", ticket["issue"])
    print("Category:", ticket["category"])
    print("Priority:", ticket["priority"])
    print("Suggested Response:", ticket["response"])
    print("Total Tickets Stored:", len(tickets))

print("\nSession ended.")
print("Final ticket count:", len(tickets))
print("Tickets saved to:", FILE_NAME)