#!/usr/bin/env python3
"""
symptom_chatbot.py

A rule-based AI Symptom Checker Chatbot (Console-Based)
-------------------------------------------------------

✔ Uses ONLY Python built-in libraries
✔ Beginner-friendly but professionally structured
✔ Keyword-based symptom detection
✔ Indian/desi tone with light humor
✔ Includes safety disclaimer
✔ Infinite loop until user types "exit" or "bye"

Run with:
    python symptom_chatbot.py
"""

# =========================
# Symptom Advice Database
# =========================

SYMPTOM_DATA = {
    "fever": {
        "keywords": ["fever", "temperature", "high temp", "viral"],
        "advice": [
            "Drink plenty of fluids like water, coconut water, or ORS.",
            "Take proper rest — your body is fighting a mini war.",
            "You may use paracetamol if needed (as per doctor guidance).",
            "Try light food like khichdi, soup, or dal-chawal.",
            "If fever lasts more than 2–3 days, consult a doctor."
        ],
        "humor": "Looks like your body turned into a heater without permission 😅"
    },

    "headache": {
        "keywords": ["headache", "migraine", "head pain"],
        "advice": [
            "Stay hydrated — dehydration is a very common cause.",
            "Take rest and avoid screen exposure for some time.",
            "Gentle head massage with oil may help.",
            "Try steam inhalation if sinus-related.",
            "If severe or frequent, consult a doctor."
        ],
        "humor": "Too much overthinking or too much mobile scrolling? Be honest 😄"
    },

    "stomach pain": {
        "keywords": ["stomach pain", "abdomen pain", "gas pain", "belly pain"],
        "advice": [
            "Drink warm water or jeera water.",
            "Avoid spicy and oily food for some time.",
            "Eat light food like curd rice or khichdi.",
            "Check if it is due to gas, acidity, or food infection.",
            "If pain is severe or persistent, see a doctor."
        ],
        "humor": "Your stomach is protesting like it's on strike 🚫🍟"
    },

    "cough": {
        "keywords": ["cough", "cold", "throat irritation"],
        "advice": [
            "Drink warm fluids and herbal tea.",
            "Honey with ginger can help soothe throat.",
            "Steam inhalation is very effective.",
            "Avoid cold drinks and ice cream for now.",
            "If cough persists more than a week, consult a doctor."
        ],
        "humor": "Your cough is trying to become the lead singer of a band 🎤"
    },

    "back pain": {
        "keywords": ["back pain", "lower back", "spine pain"],
        "advice": [
            "Maintain proper sitting posture.",
            "Do gentle stretching exercises.",
            "Apply hot compress or heating pad.",
            "Avoid lifting heavy items suddenly.",
            "If pain radiates or persists, consult a doctor."
        ],
        "humor": "Laptop + bad posture = back pain partnership deal 🤝"
    },

    "acidity": {
        "keywords": ["acidity", "acid reflux", "heartburn", "gastric"],
        "advice": [
            "Avoid spicy, oily, and junk food.",
            "Drink cold milk or buttermilk.",
            "Eat smaller meals instead of large heavy meals.",
            "Avoid lying down immediately after eating.",
            "If frequent, consult a doctor."
        ],
        "humor": "Looks like your stomach became a mini volcano 🌋"
    }
}


DISCLAIMER = "⚠ I am not a real doctor. This is basic guidance only. Please consult a qualified medical professional if symptoms persist."


# =========================
# Helper Functions
# =========================

def greet():
    """Display chatbot greeting message."""
    print("\n==============================")
    print("🩺 Desi Symptom Checker Bot")
    print("==============================")
    print("Namaste! Tell me your symptoms and I’ll try to help.")
    print("Type 'exit' or 'bye' to quit.\n")


def detect_symptom(user_input):
    """
    Detect symptom using keyword matching.

    Args:
        user_input (str): User message

    Returns:
        str or None: Detected symptom key
    """
    user_input = user_input.lower()

    for symptom, data in SYMPTOM_DATA.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return symptom

    return None


def respond(symptom):
    """Print structured response for detected symptom."""
    data = SYMPTOM_DATA[symptom]

    print("\n👉 Possible Issue:", symptom.title())
    print("💬", data["humor"])

    print("\n✅ Suggestions:")
    for tip in data["advice"]:
        print("•", tip)

    print("\n💧 Reminder: Stay hydrated and get enough rest.")
    print(DISCLAIMER)
    print()


def unknown_response():
    """Response when symptom not recognized."""
    print("\nHmm… I couldn’t clearly understand the symptom 🤔")
    print("Could you describe it in a bit more detail?")
    print("Example: 'I have fever and headache'")
    print(DISCLAIMER)
    print()


# =========================
# Main Chat Loop
# =========================

def main():
    """Main chatbot execution loop."""
    greet()

    while True:
        user_input = input("You: ").strip().lower()

        # Exit condition
        if user_input in ["exit", "bye"]:
            print("\nTake care! Stay healthy and drink water 💧")
            print("Goodbye! 👋\n")
            break

        symptom = detect_symptom(user_input)

        if symptom:
            respond(symptom)
        else:
            unknown_response()


# =========================
# Script Entry Point
# =========================

if __name__ == "__main__":
    main()