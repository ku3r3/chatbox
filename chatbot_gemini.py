import google.generativeai as ai
from google.api_core.exceptions import ResourceExhausted
from dotenv import load_dotenv
import os

# Load file .env
load_dotenv()
# Akses variabel dari .env
API_KEY = os.getenv("GEMINI_API_KEY")
# Configure the API
ai.configure(api_key=API_KEY)

# Initialize the model
model = ai.GenerativeModel("models/gemini-2.5-flash")

chat = model.start_chat()

# Start a conversation
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break
    try:
        response = chat.send_message(message)
        print('Chatbot:', response.text)
    except ResourceExhausted as e:
        print("❗ Kuota sudah habis atau terlalu sering mengirim request.")
        print("⏳ Coba lagi nanti atau upgrade akun.")
        print(e.message)
        break
