import streamlit as st
import requests

st.set_page_config(page_title="DataSmith AI Agent", layout="wide")

# ---------------- STATE ---------------- #
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------- CLEAN RESPONSE FILTER ---------------- #
def clean_response(data: dict):
    """
    Remove empty multimodal fields
    """
    if not isinstance(data, dict):
        return data

    cleaned = {}

    for k, v in data.items():
        if isinstance(v, dict):
            nested = {i: j for i, j in v.items() if j}
            if nested:
                cleaned[k] = nested
        elif v not in [[], {}, "", None]:
            cleaned[k] = v

    return cleaned


# ---------------- UI TITLE ---------------- #
st.title("🤖 DataSmith AI Agent")

# ---------------- CHAT DISPLAY ---------------- #
st.markdown("## 💬 Chat")

chat_container = st.container()

with chat_container:
    for role, msg in st.session_state.chat:

        if role == "user":
            st.markdown(
                f"""
                <div style="
                    text-align:right;
                    background:#1e293b;
                    padding:10px;
                    margin:5px;
                    border-radius:10px;
                    color:white;">
                    🧑 {msg}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"""
                <div style="
                    text-align:left;
                    background:#111827;
                    padding:10px;
                    margin:5px;
                    border-radius:10px;
                    color:#d1d5db;">
                    🤖 {msg}
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- FIXED INPUT AT BOTTOM ---------------- #
st.markdown("---")

query = st.text_input("Ask something...", key="input_box")

file = st.file_uploader(
    "Upload file (PDF / Image / Audio)",
    type=["pdf", "txt" ,"png", "jpg", "jpeg", "mp3", "wav", "mp4"]
)

col1, col2 = st.columns([1, 1])

with col1:
    send = st.button("🚀 Send")

with col2:
    clear = st.button("🧹 Clear Chat")

# ---------------- CLEAR CHAT ---------------- #
if clear:
    st.session_state.chat = []
    st.rerun()

# ---------------- SEND REQUEST ---------------- #
if send and query:

    st.session_state.chat.append(("user", query))

    files_payload = None

    if file:
        files_payload = {
            "file": (file.name, file.getvalue())
        }

    response = requests.post(
        "http://127.0.0.1:8000/run-agent",
        data={"query": query},
        files=files_payload
    )

    result = response.json()

    # # CLEAN OUTPUT (IMPORTANT FIX)
    # result = clean_response(result)

    # # show only meaningful output
    # final_output = ""

    # if "final_state" in result:
    #     final_output = result["final_state"]
    # elif "summary" in result:
    #     final_output = result["summary"]
    # else:
    #     final_output = result

    # st.session_state.chat.append(("bot", final_output))
    bot_reply = result.get("response", "No response generated")

    st.session_state.chat.append(("bot", bot_reply))
    st.rerun()