import streamlit as st

from pathlib import Path
import sys
from dotenv import load_dotenv
import os

load_dotenv()

sys.path.append(str(Path(__file__).resolve().parent.parent))
from chatGPT.GPT import ChatGPT


st.set_page_config(page_title="Low-Fi Nance Band - Lyrics Generator", page_icon="🎸")
st.title("STEMist Hackathon - Project")
st.subheader("Low-Fi Nance Band - Lyrics Generator")
st.markdown(
    "Unleash your imagination and set your creativity free with our revolutionary lyrics generator!",
)

session_token = os.environ.get("SESSION_TOKEN") or ""
conversation_id = os.environ.get("CONVERSATION_ID") or ""
song = st.text_input(
    "Enter Song Name or Genre or Artist Name",
    key="message",
)


def generate_lyrics():
    try:
        my_label = st.text("Generating Lyrics...")
        conversation = ChatGPT(
            session_token=session_token, conversation_id=conversation_id
        )
        message_to_send = "You are a lyrics generator bot. Generate lyrics for " + song
        conversation.send_message(message_to_send)
        msg = conversation.send_message("")
        conversation.__del__()
        my_label.empty()
        return msg
    except Exception as e:
        return {"message": "Unable to generate lyrics. Try again later."}


button = st.button("Generate Lyrics", key="generate")

if button:
    lyrics = generate_lyrics()
    st.text("Lyrics")
    st.text(lyrics.get("message", ""))
