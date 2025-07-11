from openai import OpenAI, RateLimitError

from dotenv import load_dotenv
import os

# Load file .env
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        try:
            response = chat_with_gpt(user_input)
            print("Chatbox:", response)
        except RateLimitError as e:
            print(
                "❌ Kuota API habis atau kamu belum mengaktifkan billing. Coba cek dashboard OpenAI kamu.")
            print(e)
            break
