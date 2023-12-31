*Still documenting
# MSA Chatbot for GroupMe

---

## Features
- **OpenAI Integration:** Utilizes the OpenAI API to generate responses and interact with users. 
- **Quranic Verses:** Posts specific Quranic verses given a chapter and verse number by the user.
- **Islamic Queries Handling:** Responds to specific commands for Islamic-related queries, for example getting local masjids or halal eating options.
- **Announcements:** Posts scheduled announcements, for example Jummah announcements.   

---

## Installation
### Dependencies
- Python 3.x
- Flask
- OpenAI Python SDK
- Requests library

### Steps
1. Clone the repository.
2. Install dependencies via `pip install -r requirements.txt`.
3. Set up environment variables for `api_key` and `bot_id`.

### Deployment
- Cloud Service Requirement: This application requires a cloud service for deployment, in my case I used Heroku.
  1. Create an App on heroku.
  2. Install the CLI: https://devcenter.heroku.com/articles/heroku-cli
  3. Login and clone repository
     - $ heroku login
     - $ heroku git:clone -a [app name]
     - $ cd [app name]
   4. Deploy changes
     - $ git add .
     - $ git commit -am "make it better"
     - $ git push heroku main


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


