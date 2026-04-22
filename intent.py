import os
from dotenv import load_dotenv

load_dotenv()

USE_OPENAI = os.getenv("OPENAI_API_KEY") is not None

if USE_OPENAI:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_intent(user_input):
    text = user_input.lower()

    # 🔁 Fallback (always works)
    def rule_based():
        if any(w in text for w in ["hi", "hello", "hey"]):
            return "greeting"
        if any(w in text for w in ["buy", "subscribe", "try", "i want"]):
            return "high_intent"
        if any(w in text for w in ["price", "pricing", "plan", "cost"]):
            return "inquiry"
        return "unknown"

    # 🤖 Try OpenAI
    if USE_OPENAI:
        try:
            prompt = f"""
Classify the intent:
greeting / inquiry / high_intent

Message: {user_input}
Return one word only.
"""
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip().lower()

        except Exception as e:
            print("⚠️ OpenAI failed, using fallback:", e)
            return rule_based()

    # 🔁 No API → fallback
    return rule_based()