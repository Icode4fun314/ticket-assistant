import json
from datetime import datetime

FILE_NAME = "tickets.json"
try:
    with open(FILE_NAME, "r") as file:
        tickets = json.load(file)
except FileNotFoundError:
    tickets = []


def get_next_ticket_id():
    if not tickets:
        return 1001

    ticket_ids = []

    for ticket in tickets:
        if "id" in ticket:
            ticket_ids.append(ticket["id"])

    if not ticket_ids:
        return 1001

    return max(ticket_ids) + 1

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
        "id": get_next_ticket_id(),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "issue": issue,
        "category": category,
        "priority": priority,
        "status": "Open",
        "response": response
    }


def save_tickets():
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)

def display_ticket(ticket):
    print("\n--- Ticket ---")
    print("Ticket ID:", ticket.get("id", "No ID"))
    print("Created At:", ticket.get("created_at", "No timestamp"))
    print("Issue:", ticket["issue"])
    print("Category:", ticket["category"])
    print("Priority:", ticket["priority"])
    print("Status:", ticket.get("status", "Open"))
    print("Suggested Response:", ticket["response"])


def view_all_tickets():
    if not tickets:
        print("\nNo tickets found.")
        return

    print("\n--- All Tickets ---")

    for ticket in tickets:
        display_ticket(ticket)

    print("\nTotal Tickets Stored:", len(tickets))


# New function to close a ticket
def close_ticket():
    ticket_id = input("Enter the Ticket ID to close: ")

    if not ticket_id.isdigit():
        print("Invalid Ticket ID. Please enter a number.")
        return

    ticket_id = int(ticket_id)

    for ticket in tickets:
        if ticket.get("id") == ticket_id:
            ticket["status"] = "Closed"
            save_tickets()
            print("Ticket", ticket_id, "has been closed.")
            return

    print("Ticket ID not found.")

# New function to search tickets
def search_tickets():
    search_term = input("Enter a search term: ").lower()
    matches = []

    for ticket in tickets:
        issue = ticket["issue"].lower()
        category = ticket["category"].lower()
        priority = ticket["priority"].lower()
        status = ticket.get("status", "Open").lower()

        if (
            search_term in issue
            or search_term in category
            or search_term in priority
            or search_term in status
        ):
            matches.append(ticket)

    if not matches:
        print("\nNo matching tickets found.")
        return

    print("\n--- Search Results ---")

    for ticket in matches:
        display_ticket(ticket)

    print("\nTotal Matches:", len(matches))


while True:
    print("\n=== AI Ticket Assistant ===")
    print("1. Create Ticket")
    print("2. View All Tickets")
    print("3. Close Ticket")
    print("4. Search Tickets")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        user_issue = input("Enter the support issue: ")

        ticket = ticket_response(user_issue)
        tickets.append(ticket)
        save_tickets()

        print("\n--- Ticket Created ---")
        print("Ticket ID:", ticket["id"])
        print("Created At:", ticket["created_at"])
        print("Issue received:", ticket["issue"])
        print("Category:", ticket["category"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])
        print("Suggested Response:", ticket["response"])
        print("Total Tickets Stored:", len(tickets))

    elif choice == "2":
        view_all_tickets()

    elif choice == "3":
        close_ticket()

    elif choice == "4":
        search_tickets()

    elif choice == "5":
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, 4, or 5.")

print("\nSession ended.")
print("Final ticket count:", len(tickets))
print("Tickets saved to:", FILE_NAME)