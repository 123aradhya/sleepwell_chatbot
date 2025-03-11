import streamlit as st
from chatbot_logic import get_bot_response  # Your chatbot logic function
from db_config import insert_chat_data     # Your DB insert function (example)

# Optional: set page config
st.set_page_config(
    page_title="Sleepy Chatbot",
    layout="centered",  # or "wide"
    initial_sidebar_state="collapsed"
)

# In chatbot_app.py
st.markdown("""
    <style>
    .chat-container {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 8px;
        max-width: 600px;
        margin: auto;
    }
    .user-message {
        background-color: #DCF8C6; /* Light green bubble (WhatsApp style) */
        border-radius: 8px;
        padding: 8px;
        margin-bottom: 5px;
        text-align: left;
    }
    .bot-message {
        background-color: #FFF;
        border-radius: 8px;
        padding: 8px;
        margin-bottom: 5px;
        text-align: left;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Sleep Chatbot")  # or hide the default title & create custom UI
    
    # Container or placeholder for chat messages
    chat_container = st.container()

    # If you want to maintain chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Display existing chat history
    with chat_container:
        for message in st.session_state["chat_history"]:
            if message["sender"] == "user":
                st.markdown(f"*You:* {message['text']}")
            else:
                st.markdown(f"*Sleepy (Bot):* {message['text']}")

    # Quick reply options (like buttons)
    st.write("### Quick Actions:")
    col1, col2, col3 = st.columns(3)
    if col1.button("Mattress Finder"):
        handle_user_input("Mattress Finder")
    if col2.button("Track/Modify Order"):
        handle_user_input("Track/Modify Order")
    if col3.button("Raise a complaint"):
        handle_user_input("Raise a complaint")

    col4, col5, col6 = st.columns(3)
    if col4.button("Warranty registration"):
        handle_user_input("Warranty registration")
    if col5.button("Get Sleep Advice"):
        handle_user_input("Get Sleep Advice")
    if col6.button("FAQs"):
        handle_user_input("FAQs")

    # Free-form text input
    user_input = st.text_input("Type your message here...", "")
    if st.button("Send"):
        handle_user_input(user_input)

def handle_user_input(user_text):
    # Add user message to chat history
    st.session_state["chat_history"].append({"sender": "user", "text": user_text})

    # Get bot response
    bot_response = get_bot_response(user_text)

    # Add bot response to chat history
    st.session_state["chat_history"].append({"sender": "bot", "text": bot_response})

    # Save to DB if needed
    insert_chat_data(user_text, bot_response)

    # Rerun to display updated chat
    st.experimental_rerun()

if __name__ == "__main__":
    main()