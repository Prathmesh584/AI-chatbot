import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
print("******************************************************************")
while True:
    chat = input("you: ")

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(chat)

    print("chat bot: ",response.text)
    if chat == "exit":
        break
print("*******************************************************************")