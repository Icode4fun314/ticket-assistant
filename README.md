# AI Ticket Assistant

A Python-based IT support workflow application that simulates a real-world ticketing system with automated categorization, priority assignment, searchable ticket management, and persistent JSON storage.

Built as part of an AI Automation Engineering learning roadmap focused on workflow systems, automation, and AI integration.

---

## Features

- Create IT support tickets
- Automatically categorize support issues
- Automatically assign priority levels
- Generate suggested troubleshooting responses
- Save tickets using persistent JSON storage
- Assign unique ticket IDs
- Add timestamps to new tickets
- Track ticket status
- Close tickets
- View all saved tickets
- Search tickets by issue, category, priority, or status
- Use a menu-driven terminal workflow

---

## Technologies Used

- Python
- JSON
- VS Code
- Git
- GitHub
- Terminal / Command Line

---

## Skills Demonstrated

- Python functions
- Lists and dictionaries
- Conditional logic
- Loops
- User input handling
- JSON file storage
- Data persistence
- Search and filtering logic
- Workflow state management
- Basic backend application structure
- Git/GitHub version control
- Technical documentation

---

## Project Structure

```text
ticket-assistant/
├── ticket_assistant.py
├── tickets.json
└── README.md
# AI Ticket Assistant

A Python-based AI-powered IT support ticket assistant that simulates a real help desk workflow.

The application allows users to create, view, search, and close IT support tickets while using Azure OpenAI to analyze support issues, assign categories, set priority levels, and generate suggested troubleshooting responses.

---

## Features

- Create IT support tickets
- Generate unique ticket IDs
- Add timestamps to tickets
- Track ticket status
- Close tickets
- View all saved tickets
- Search tickets by issue, category, priority, or status
- Save tickets using JSON persistent storage
- Connect to Azure OpenAI through an API
- Use GPT-4.1-mini for AI-generated ticket analysis
- Use fallback Python rules if Azure AI is unavailable
- Store ticket data locally in `tickets.json`

---

## Technologies Used

- Python
- JSON
- Azure AI Foundry
- Azure OpenAI
- GPT-4.1-mini
- OpenAI Python SDK
- VS Code
- Git
- GitHub
- Terminal / Command Line

---

## Skills Demonstrated

- Python functions
- Lists and dictionaries
- Conditional logic
- Loops
- JSON file handling
- Data persistence
- API integration
- Environment variables
- Azure OpenAI deployment
- AI-generated structured responses
- Search/filter logic
- Workflow automation
- Basic backend application structure
- Technical documentation
- Git/GitHub version control

---

## Project Workflow

```text
User creates ticket
↓
Python sends support issue to Azure OpenAI
↓
AI returns category, priority, and response
↓
Python parses AI response
↓
Ticket is saved to tickets.json
↓
User can view, search, or close tickets
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

### 3. Install Required Packages

```bash
pip3 install openai requests
```

### 4. Set Azure Environment Variables

```bash
export AZURE_OPENAI_ENDPOINT="your_endpoint_here"
export AZURE_OPENAI_API_KEY="your_api_key_here"
export AZURE_OPENAI_DEPLOYMENT="gpt-4.1-mini"
```

### 5. Run the Application

```bash
python3 ticket_assistant.py
```

---

## Menu Options

```text
=== AI Ticket Assistant ===

1. Create Ticket
2. View All Tickets
3. Close Ticket
4. Search Tickets
5. Test API Connection
6. Test POST Request
7. Quit
```

---

## Current Development Stage

Version 1 is complete.

This version includes:

- Python ticket workflow system
- JSON storage
- ticket IDs
- timestamps
- status tracking
- ticket search
- close ticket workflow
- Azure OpenAI integration
- AI-generated ticket analysis
- fallback logic

---

## Why I Built This

I built this project to connect my IT support experience with AI automation and workflow development.

The goal was to create a practical project that demonstrates how AI can support real help desk workflows by analyzing support issues, generating suggested responses, and improving ticket triage.

This project is part of my larger roadmap toward AI automation, workflow engineering, and Microsoft Azure AI tools.

---

## Future Improvements

- Add Azure AI Search
- Add knowledge base retrieval
- Add semantic ticket search
- Add Flask web interface
- Add analytics dashboard
- Add Microsoft Teams or Copilot integration
- Add database support
- Deploy online