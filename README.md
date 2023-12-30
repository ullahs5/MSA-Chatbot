*Still documenting

MSA Chatbot
Features
OpenAI Integration: Utilizes the OpenAI API for generating responses.
Flask Integration: Utilizes Flask to create API endpoints for interaction.
GroupMe Integration: Posts responses to GroupMe via their API.
Quranic Verse Retrieval: Fetches and posts specific Quranic verses based on user input.
Islamic Queries Handling: Responds to specific commands for Islamic-related queries (!masjid, !halal).
Installation
Dependencies
Python 3.x
Flask
OpenAI Python SDK
Requests library
Steps
Clone the repository.
Set up a virtual environment (optional but recommended).
Install dependencies via pip install -r requirements.txt.
Set up environment variables for api_key and bot_id.
Run the Flask application using python app.py.
Development
Endpoints
/ (GET): Returns a simple "hi" message.
/ (POST): Receives and processes incoming messages from GroupMe, generates appropriate responses based on user input, and posts responses to the chat.
Functionality
Listens for specific characters at the start of messages ('.', '!', '-') to trigger different actions:
'.': Engages OpenAI for generating responses to conversational messages.
'!': Handles specific commands (!masjid, !halal) to provide relevant information.
'-': Fetches and posts specific Quranic verses based on the provided numbering.
Additional Functionality (Commented Out)
A function for automated Jummah announcements is available but currently commented out.
Roadmap
Enhanced Conversation Handling: Improve conversation context handling and AI response accuracy.
Feature Expansion: Integrate additional Islamic functionalities based on community needs.
Optimization: Refactor code for better efficiency and readability.
Automated Testing: Implement testing procedures for robustness and stability.
Deployment: Prepare for deployment on a hosting service for continual use.
Feel free to expand or modify the documentation as needed, adding specific instructions or additional sections based on your project requirements.
