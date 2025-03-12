import streamlit as st
from chatbot_logic import get_bot_response  
from db_config import insert_chat_data  

# Page configuration
st.set_page_config(page_title="Sleepy Chatbot", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for Floating Chat UI
st.markdown("""
    <style>
        /* Floating chat container */
        .chat-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            max-width: 600px;
            margin: auto;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            position: relative;
        }

        /* Bot message styling */
        .bot-message {
            background-color: #E3F2FD;
            border-radius: 10px;
            padding: 12px;
            margin-bottom: 10px;
            text-align: left;
            border: 1px solid #ddd;
            max-width: 80%;
            word-wrap: break-word;
            display: flex;
            align-items: center;
        }

        /* User message styling */
        .user-message {
            background-color: #DCF8C6;
            border-radius: 10px;
            padding: 12px;
            margin-bottom: 10px;
            text-align: right;
            border: 1px solid #ddd;
            max-width: 80%;
            word-wrap: break-word;
            display: flex;
            align-items: center;
            justify-content: flex-end;
        }

        /* Avatar styling */
        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }

        .user-avatar {
            margin-left: 10px;
        }

        /* Welcome box */
        .welcome-box {
            background-color: #FFF;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 14px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }

        /* Quick Action Buttons */
        .quick-actions {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
        }

        .quick-actions button {
            background-color: #E3F2FD;
            border: none;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 14px;
            cursor: pointer;
        }

        .quick-actions button:hover {
            background-color: #BBDEFB;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    # Bot avatar using a URL
    st.image("bot_avatar.png", width=50)  # Placeholder bot avatar
    st.title("Sleepy Chatbot 💤")

    # Welcome message
    st.markdown("""
        <div class='welcome-box'>
            <strong>Welcome to Sleepy – Your AI Sleep Assistant! 😴✨</strong><br>
            I'm Nidrā, your AI shopping sidekick 🛍️💡.<br>
            Need help with the perfect mattress, order tracking, or sleep magic? I've got you covered! 🌙💤
        </div>
    """, unsafe_allow_html=True)

    # Quick Actions
    st.write("### Quick Actions:")
    col1, col2, col3 = st.columns(3)
    if col1.button("Mattress Finder 🛏️"):
        handle_user_input("Mattress Finder")
    if col2.button("Track/Modify Order 📦"):
        handle_user_input("Track/Modify Order")
    if col3.button("Raise a Complaint ⚠️"):
        handle_user_input("Raise a Complaint")

    col4, col5, col6 = st.columns(3)
    if col4.button("Warranty Registration 📝"):
        handle_user_input("Warranty Registration")
    if col5.button("Get Sleep Advice 💤"):
        handle_user_input("Get Sleep Advice")
    if col6.button("FAQs ❓"):
        handle_user_input("FAQs")

    # Additional row
    if st.button("Track Your Complaint 🛠️"):
        handle_user_input("Track Your Complaint")

    # Chat history container
    chat_container = st.container()

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Display chat history
    with chat_container:
        for message in st.session_state["chat_history"]:
            if message["sender"] == "user":
                st.markdown(f"""
                    <div class='user-message'>
                        <span class='user-avatar'><img src='bot_avatar.png' class='avatar'></span>
                        {message['text']}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class='bot-message'>
                        <span><img src='bot_avatar.png' class='avatar'></span>
                        {message['text']}
                    </div>
                """, unsafe_allow_html=True)

    # User input field
    user_input = st.text_input("Type your message here...", "")
    if st.button("Send"):
        handle_user_input(user_input)

def handle_user_input(user_text):
    st.session_state["chat_history"].append({"sender": "user", "text": user_text})

    # Check for sub-intents
    if user_text == "Mattress Finder":
        st.session_state["chat_history"].append({"sender": "bot", "text": "Mattresses, Beds, or Pillows."})
    elif user_text == "Mattresses":
        st.session_state["chat_history"].append({"sender": "bot", "text": "Please select a type: Foam Mattress or Spring Mattress."})
    elif user_text == "Beds":
        st.session_state["chat_history"].append({"sender": "bot", "text": "Please select a type: Metal Bed or Wooden Bed."})
    elif user_text == "Pillows":
        st.session_state["chat_history"].append({"sender": "bot", "text": "Please select a type: Snuggle Pillow, Cloud Pillow, or Cuddle Pillow."})
    else:
        bot_response = get_bot_response(user_text)
        st.session_state["chat_history"].append({"sender": "bot", "text": bot_response})
        insert_chat_data(user_text, bot_response)

if __name__ == "__main__":
    main()

    # Add sub-intent buttons
    if "Mattress Finder" in [msg["text"] for msg in st.session_state["chat_history"] if msg["sender"] == "user"]:
        st.write("### Select a Category:")
        if st.button("Mattresses"):
            handle_user_input("Mattresses")
        if st.button("Beds"):
            handle_user_input("Beds")
        if st.button("Pillows"):
            handle_user_input("Pillows")

    if "Mattresses" in [msg["text"] for msg in st.session_state["chat_history"] if msg["sender"] == "user"]:
        st.write("### Select a Type:")
        if st.button("Foam Mattress"):
            handle_user_input("Foam Mattress")
        if st.button("Spring Mattress"):
            handle_user_input("Spring Mattress")

    if "Beds" in [msg["text"] for msg in st.session_state["chat_history"] if msg["sender"] == "user"]:
        st.write("### Select a Type:")
        if st.button("Metal Bed"):
            handle_user_input("Metal Bed")
        if st.button("Wooden Bed"):
            handle_user_input("Wooden Bed")

    if "Pillows" in [msg["text"] for msg in st.session_state["chat_history"] if msg["sender"] == "user"]:
        st.write("### Select a Type:")
        if st.button("Snuggle Pillow"):
            handle_user_input("Snuggle Pillow")
        if st.button("Cloud Pillow"):
            handle_user_input("Cloud Pillow")
        if st.button("Cuddle Pillow"):
            handle_user_input("Cuddle Pillow")
