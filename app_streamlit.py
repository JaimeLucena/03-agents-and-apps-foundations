import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"  # Local default

st.set_page_config(page_title="Streamlit + FastAPI", page_icon="🛰️")
st.title("Streamlit UI → FastAPI /chat")

if "history" not in st.session_state:
    st.session_state.history = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "demo-user-1"

user_msg = st.text_input("Your message", key="msg_input_api")
send = st.button("Send to API")

def call_api(message: str, thread_id: str | None = None) -> str:
    payload = {"message": message}
    if thread_id:
        payload["thread_id"] = thread_id
    try:
        r = requests.post(API_URL, json=payload, timeout=20)
        r.raise_for_status()
        data = r.json()
        return data.get("reply", "(no reply field)")
    except Exception as e:
        return f"Error calling API: {e}"

if send and user_msg.strip():
    st.session_state.history.append(("user", user_msg))
    reply = call_api(user_msg, st.session_state.thread_id)
    st.session_state.history.append(("assistant", reply))
    st.rerun()

st.subheader("Conversation")
for role, text in st.session_state.history:
    st.markdown(f"**{role.title()}:** {text}")

with st.expander("Config"):
    st.write("API_URL:", API_URL)
    st.write("thread_id:", st.session_state.thread_id)

st.caption("This variant keeps business logic in FastAPI and uses Streamlit only for UI.")