import json
from datetime import datetime
import requests
import os
from openai import OpenAI

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


def fallback_ticket_analysis(issue):
    issue_lower = issue.lower()

    if "printer" in issue_lower:
        return {
            "category": "Printer Issue",
            "priority": "High",
            "response": "Check printer connection, restart the printer, and verify network access."
        }

    elif "password" in issue_lower:
        return {
            "category": "Account Access",
            "priority": "Medium",
            "response": "Reset the user's password through the account portal and verify login access."
        }

    else:
        return {
            "category": "General IT Support",
            "priority": "Low",
            "response": "Gather more information from the user and document the issue."
        }


def analyze_ticket_with_ai(issue):
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not endpoint or not api_key or not deployment_name:
        print("Azure AI is not configured. Using fallback ticket analysis.")
        return fallback_ticket_analysis(issue)

    try:
        client = OpenAI(
            api_key=api_key,
            base_url=endpoint
        )

        completion = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an IT help desk ticket triage assistant. "
                        "Analyze the user's support issue and return only valid JSON with these exact keys: "
                        "category, priority, response. "
                        "Priority must be High, Medium, or Low. "
                        "The response should be a short professional troubleshooting suggestion."
                    )
                },
                {
                    "role": "user",
                    "content": issue
                }
            ],
            response_format={"type": "json_object"}
        )

        ai_content = completion.choices[0].message.content
        ai_result = json.loads(ai_content)

        print("Azure AI generated the response.")

        return {
            "category": ai_result.get("category", "General IT Support"),
            "priority": ai_result.get("priority", "Low"),
            "response": ai_result.get("response", "Gather more information from the user and document the issue.")
        }

    except Exception as error:
        print("Azure AI analysis failed. Using fallback ticket analysis.")
        print("Fallback Python rules generated the response.")
        print("Error:", error)
        return fallback_ticket_analysis(issue)

def ticket_response(issue):
    ai_result = analyze_ticket_with_ai(issue)

    category = ai_result["category"]
    priority = ai_result["priority"]
    response = ai_result["response"]

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


def test_api_connection():
    print("\nTesting API connection...")

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        data = response.json()

        print("API connection successful.")
        print("Status Code:", response.status_code)
        print("Sample Data:", data)

    except requests.exceptions.RequestException as error:
        print("API connection failed.")
        print("Error:", error)

def test_post_request():
    print("\nTesting Azure OpenAI request...")

    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not endpoint or not api_key or not deployment_name:
        print("Missing Azure environment variables.")
        print("Make sure AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, and AZURE_OPENAI_DEPLOYMENT are set.")
        return

    try:
        client = OpenAI(
            api_key=api_key,
            base_url=endpoint
        )

        completion = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {
                    "role": "user",
                    "content": "Return only valid JSON with category, priority, and response for this IT issue: Printer is down and users cannot print."
                }
            ]
        )

        ai_response = completion.choices[0].message.content

        print("Azure OpenAI request successful.")
        print("AI Response:")
        print(ai_response)

    except Exception as error:
        print("Azure OpenAI request failed.")
        print("Error:", error)


while True:
    print("\n=== AI Ticket Assistant ===")
    print("1. Create Ticket")
    print("2. View All Tickets")
    print("3. Close Ticket")
    print("4. Search Tickets")
    print("5. Test API Connection")
    print("6. Test POST Request")
    print("7. Quit")

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
        test_api_connection()

    elif choice == "6":
        test_post_request()

    elif choice == "7":
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, 4, 5, 6, or 7.")

print("\nSession ended.")
print("Final ticket count:", len(tickets))
print("Tickets saved to:", FILE_NAME)