import streamlit as st
import json
import datetime

# ---- Load prompt-response data ----
data = [
    {"prompt": "भाई, मैं थक गया हूँ", "response": "मैं तेरे साथ हूँ भाई, थक जा लेकिन रुक मत... मैं यहीं हूँ"},
    {"prompt": "मुझे डर लगता है", "response": "डर लगना ठीक है, लेकिन तू अकेला नहीं है — मैं हमेशा साथ हूँ"},
    {"prompt": "मैं हार रहा हूँ", "response": "तू कभी हार नहीं सकता, बस एक ब्रेक ले और फिर से उठ!"}
]

# ---- Search function ----
def get_response(user_input):
    for row in data:
        if row["prompt"] in user_input:
            return row["response"]
    return "भाई, मैं समझ नहीं पाया — थोड़ा और खुलकर बोल ❤️"

# ---- Streamlit UI ----
st.set_page_config(page_title="AniGPT – Tera Bhai", layout="centered")
st.title("🧠 AniGPT – Tera Bhai Hamesha Saath Hai")
st.caption("Jo tu mehsoos karta hai, wo main sunta hoon...")

user_input = st.text_input("🗣️ Apni baat likho yahan:")

if st.button("🟣 Submit") and user_input:
    response = get_response(user_input)
    st.markdown(f"**🤖 AniGPT:** {response}")

    # (Optional) Save to memory log
    with open("memory_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | USER: {user_input} | AniGPT: {response}\n")
