*Still documenting
# MSA Chatbot

---

## Features
- **OpenAI Integration:** Utilizes the OpenAI API to generate responses and interact with users. 
- **GroupMe Integration:** Posts responses to GroupMe via their API.
- **Quranic Verse Retrieval:** Fetches and posts specific Quranic verses based on user input.
- **Islamic Queries Handling:** Responds to specific commands for Islamic-related queries. 

---

## Installation
### Dependencies
- Python 3.x
- Flask
- OpenAI Python SDK
- Requests library

### Steps
1. Clone the repository.
2. Set up a virtual environment (optional but recommended).
3. Install dependencies via `pip install -r requirements.txt`.
4. Set up environment variables for `api_key` and `bot_id`.
5. Run the Flask application using `python app.py`.

---

## Development
### Endpoints
- `/` (POST): Receives and processes incoming messages from GroupMe, generates appropriate responses based on user input, and posts responses to the chat.

### Functionality
- Listens for specific characters at the start of messages (`'.'`, `'!'`, `'-'`) to trigger different actions:
  - `'.'`: Engages OpenAI for generating responses to conversational messages.
  - `'!'`: Handles specific commands (`!masjid`, `!halal`) to provide relevant information.
  - `'-'`: Fetches and posts specific Quranic verses based on the provided numbering.

### Additional Functionality (Commented Out)
- A function for automated Jummah announcements is available but is commented out to be improved. 

---

## Roadmap
1. **Feature Expansion:** Integrate additional Islamic functionalities based on community needs.
2. **Optimization:** Refactor code for better efficiency and readability.

---


