# AI Ticket Assistant

A Python-based IT support ticket triage assistant that categorizes support issues, assigns priority levels, stores tickets permanently, and simulates real help desk workflow automation.

This project was built to combine IT support experience with practical AI and automation concepts.

---

## Features

- Accepts support issues from the terminal
- Categorizes support tickets automatically
- Assigns ticket priority levels
- Generates suggested support responses
- Supports multiple tickets per session
- Saves tickets permanently using JSON storage
- Loads previous tickets automatically when the program starts
- Uses structured ticket data with Python dictionaries
- Includes basic error handling

---

## Technologies Used

- Python
- JSON
- VS Code
- GitHub
- Terminal / Command Line

---

## Skills Demonstrated

- Python functions
- Variables
- Conditional logic: `if`, `elif`, `else`
- Loops: `while`
- Lists and dictionaries
- User input handling
- File reading and writing
- JSON data storage
- Basic application structure
- Workflow automation logic

---

## Project Structure

```text
ticket-assistant/
├── ticket_assistant.py
├── tickets.json
└── README.md
# AI Ticket Assistant

A Python-based IT support ticket triage assistant that categorizes support issues, assigns priority levels, stores tickets permanently, and simulates real help desk workflow automation.

This project was built to combine IT support experience with practical AI and automation concepts.

---

## Features

- Accepts support issues from the terminal
- Categorizes support tickets automatically
- Assigns ticket priority levels
- Generates suggested support responses
- Supports multiple tickets per session
- Saves tickets permanently using JSON storage
- Loads previous tickets automatically when the program starts
- Uses structured ticket data with Python dictionaries
- Includes basic error handling

---

## Technologies Used

- Python
- JSON
- VS Code
- GitHub
- Terminal / Command Line

---

## Skills Demonstrated

- Python functions
- Variables
- Conditional logic: `if`, `elif`, `else`
- Loops: `while`
- Lists and dictionaries
- User input handling
- File reading and writing
- JSON data storage
- Basic application structure
- Workflow automation logic

---

## Project Structure

```text
ticket-assistant/
├── ticket_assistant.py
├── tickets.json
└── README.md
```

---

## How To Run

### 1. Clone the Repository

```bash
git clone https://github.com/Icode4fun314/ticket-assistant.git
```

### 2. Navigate Into the Project Folder

```bash
cd ticket-assistant
```

### 3. Run the Application

```bash
python3 ticket_assistant.py
```

---

## Example Usage

### Example Input

```text
printer is down urgent
forgot my password
computer is freezing
quit
```

### Example Output

```text
--- Ticket Created ---
Issue received: printer is down urgent
Category: Printer Issue
Priority: High
Suggested Response: Check printer connection and restart the printer.
Total Tickets Stored: 1
```

---

## Current Workflow

```text
User enters issue
→ Application analyzes text
→ Category assigned
→ Priority assigned
→ Suggested response generated
→ Ticket stored in memory
→ Ticket saved to JSON file
```

---

## Future Improvements

- Azure AI Foundry integration
- AI-generated support responses
- Improved ticket classification
- Severity scoring
- CSV export support
- Web interface/dashboard
- Analytics and reporting
- Microsoft Teams integration

---

## Why I Built This

I built this project to strengthen my Python, automation, and AI workflow development skills while connecting them to real-world IT support scenarios.

The long-term goal is to evolve this project into an AI-powered support workflow assistant using Microsoft Azure AI tools.