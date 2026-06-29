
import streamlit as st
import requests

# ── 1. Page Configuration & Theme ────────────────────────────
st.set_page_config(
    page_title="GramSahayak AI",
    page_icon="🏛️",
    layout="wide"
)

# Earthy Terracotta, Forest Green, and Soft Cream Color Theme
CUSTOM_CSS = """
<style>
    /* Main Background color */
    .stApp {
        background-color: #FDFBF7;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #F5EFEB !important;
        border-right: 1px solid #E6D8D0;
    }
    
    /* Title coloring */
    h1, h2, h3 {
        color: #D35400 !important;
    }
    
    /* Highlight buttons and cards */
    div.stButton > button {
        background-color: #1B5E20 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #2E7D32 !important;
        color: #FDFBF7 !important;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── 2. Configuration & State ─────────────────────────────────
BACKEND_URL = "http://127.0.0.1:8000/chat"

# Initialize conversation history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# ── 3. Sidebar Layout ──────────────────────────────────────────
with st.sidebar:
    st.title("Panchayat Directory")
    st.write("Need to visit or call the office?")
    
    # Expanders for clean info layouts
        
    with st.expander("⏱️ Office Timings"):
        st.write("Monday to Friday: 10:00 AM - 5:00 PM")
        st.write("Saturday: 10:00 AM - 1:00 PM")
        st.write("Sunday: Closed")

    st.divider()
    
    # Accessibility toggle
    large_font = st.checkbox("Large Text Mode (for easy reading)")
    if large_font:
        st.markdown("<style>p, span, input { font-size: 1.2rem !important; }</style>", unsafe_allow_html=True)

# ── 4. Main UI Header ─────────────────────────────────────────
st.title(" GramSahayak AI (ഗ്രാംസഹായക്)")
st.caption("AI-powered assistant for Kerala Gram Panchayat Services & Schemes")

# ── 5. Helper Function to Call Backend ────────────────────────
def ask_assistant(question):
    payload = {
        "question": question,
        "chat_history": st.session_state.history
    }
    try:
        response = requests.post(BACKEND_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("answer", "Error reading response.")
        else:
            return f"Error: Received status code {response.status_code} from server."
    except requests.exceptions.ConnectionError:
        return "⚠️ Connection Error: Unable to connect to the backend. Please ensure the backend is running at http://127.0.0.1:8000"

# ── 6. Welcome Banner & Quick Start Cards ───────────────────
if len(st.session_state.history) == 0:
    st.info("👋 Namaste! Ask me about certificates, welfare schemes, fees, timelines, or application procedures.")
    
    # 2x2 grid for common questions
    st.write("### Quick Questions:")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 What documents are required for an Income Certificate?"):
            st.session_state.temp_prompt = "What documents are required for applying for an Income Certificate?"
            
        if st.button("💍 What is the procedure for Marriage Registration?"):
            st.session_state.temp_prompt = "What is the procedure for Marriage Registration?"
            
    with col2:
        if st.button("💰 What are the fees for a Widow Certificate?"):
            st.session_state.temp_prompt = "What are the fees for a Widow Certificate?"
            
        if st.button("⏱️ How long does it take to get a Birth Certificate?"):
            st.session_state.temp_prompt = "How long does it take to get a Birth Certificate?"

# ── 7. Render Chat History ────────────────────────────────────
for msg in st.session_state.history:
    role = "user" if msg["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.write(msg["content"])

# ── 8. Chat Input & Processing ────────────────────────────────
# Use prompt from either chat_input or a click from the quick action cards
prompt = st.chat_input("Ask a question about Panchayat services...")

if hasattr(st.session_state, "temp_prompt"):
    prompt = st.session_state.temp_prompt
    del st.session_state.temp_prompt

if prompt:
    # Display user query
    with st.chat_message("user"):
        st.write(prompt)
    
    # Add to history
    st.session_state.history.append({"role": "user", "content": prompt})
    
    # Get and display bot response with spinner loading animation
    with st.chat_message("assistant"):
        with st.spinner("Searching Panchayat records..."):
            bot_answer = ask_assistant(prompt)
            st.write(bot_answer)
            
    # Add bot answer to history
    st.session_state.history.append({"role": "bot", "content": bot_answer})
    st.rerun()
