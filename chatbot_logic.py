def get_bot_response(user_text):
    # Basic keyword-based logic for illustration
    user_text_lower = user_text.lower()

    if "track" in user_text_lower or "modify" in user_text_lower:
        return "Sure! Please provide your order ID and the details you want to modify."
    elif "complaint" in user_text_lower:
        return "I'm sorry you're facing an issue. Please provide more details about the complaint."
    elif "warranty" in user_text_lower:
        return "You can register your product warranty here: <URL>."
    elif "sleep advice" in user_text_lower:
        return "We have experts to guide you! Could you share what sleep issues you're facing?"
    elif "faq" in user_text_lower:
        return "Here are some frequently asked questions: <link>"

    # Fallback
    return "I'm not quite sure. Could you rephrase or provide more details?"