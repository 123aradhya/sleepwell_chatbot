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
    elif user_text_lower == "mattresses":
        return "You selected Mattresses. Please choose between Foam Mattress or Spring Mattress."
    elif user_text_lower == "foam mattress":
        return "Foam Mattress: Known for its comfort and support."
    elif user_text_lower == "spring mattress":
        return "Spring Mattress: Offers great support and durability."
    elif user_text_lower == "beds":
        return "You selected Beds. Please choose between Metal Bed or Wooden Bed."
    elif user_text_lower == "metal bed":
        return "Metal Bed: Durable and stylish."
    elif user_text_lower == "wooden bed":
        return "Wooden Bed: Classic and sturdy."
    elif user_text_lower == "pillows":
        return "You selected Pillows. Please choose between Snuggle Pillow, Cloud Pillow, or Cuddle Pillow."
    elif user_text_lower == "snuggle pillow":
        return "Snuggle Pillow: Soft and cozy for a good night's sleep."
    elif user_text_lower == "cloud pillow":
        return "Cloud Pillow: Light and fluffy, like sleeping on a cloud."
    elif user_text_lower == "cuddle pillow":
        return "Cuddle Pillow: Perfect for side sleepers and cuddling."

    # Fallback
    return "I'm not quite sure. Could you rephrase or provide more details?"