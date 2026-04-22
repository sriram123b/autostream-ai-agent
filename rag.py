import json
import os
from dotenv import load_dotenv

load_dotenv()

USE_OPENAI = os.getenv("OPENAI_API_KEY") is not None

if USE_OPENAI:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("knowledge_base.json") as f:
    data = json.load(f)

def get_answer(query):
    query_lower = query.lower()

    # 🔁 Fallback RAG
    def rule_based():
        if any(w in query_lower for w in ["price", "pricing", "plan"]):
            return f"""
Basic Plan: $29/month
Pro Plan: $79/month (4K + AI captions)
"""
        if "refund" in query_lower:
            return data["policies"]["refund"]
        return "Sorry, I couldn't find that information."

    # 🤖 Try OpenAI
    if USE_OPENAI:
        try:
            context = json.dumps(data, indent=2)

            prompt = f"""
Answer using ONLY this data:
{context}

Question: {query}
"""
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content

        except Exception as e:
            print("⚠️ OpenAI failed, using fallback:", e)
            return rule_based()

    return rule_based()