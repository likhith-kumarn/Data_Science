from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Chatbot ✅ | Type 'exit' to quit")

messages = [{"role": "system", "content": "You are a helpful chatbot assistant."}]

while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit", "bye"]:
        print("Bot: ✅ Session Ended! Goodbye 👋")
        break

    messages.append({"role": "user", "content": user})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ updated model
            messages=messages
        )

        bot_reply = response.choices[0].message.content
        print("Bot:", bot_reply)
        messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print(f"Bot: ❌ Error:", e)
