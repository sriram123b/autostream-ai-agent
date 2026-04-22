from intent import detect_intent
from rag import get_answer
from tools import mock_lead_capture

class AgentState:
    def __init__(self):
        self.intent = None
        self.step = None
        self.name = None
        self.email = None
        self.platform = None

state = AgentState()

def agent_response(user_input):
    global state

    # Detect intent if not in lead flow
    if state.intent != "high_intent":
        state.intent = detect_intent(user_input)
        print("DEBUG:", state.intent)

    # Greeting
    if state.intent == "greeting":
        return "Hey! 👋 I can help you with AutoStream pricing or get you started."

    # Inquiry → RAG
    if state.intent == "inquiry":
        return get_answer(user_input)

    # High Intent Flow
    if state.intent == "high_intent":

        if state.step is None:
            state.step = "ask_name"
            return "Awesome! Let's get you started 🚀 What's your name?"

        elif state.step == "ask_name":
            state.name = user_input
            state.step = "ask_email"
            return "Great! What's your email?"

        elif state.step == "ask_email":
            state.email = user_input
            state.step = "ask_platform"
            return "Nice! Which platform do you create content on? (YouTube, Instagram, etc.)"

        elif state.step == "ask_platform":
            state.platform = user_input

            mock_lead_capture(state.name, state.email, state.platform)

            # Reset
            state.intent = None
            state.step = None
            state.name = None
            state.email = None
            state.platform = None

            return "🎉 You're all set! Our team will reach out shortly."

    return "Hmm, I didn't get that. Can you rephrase?"