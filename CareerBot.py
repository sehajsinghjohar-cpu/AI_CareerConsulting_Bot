import streamlit as st
from groq import Groq

st.set_page_config(page_title="Career Counsellor Bot", layout ="centered")
st.title("AI Career Counsellor")
st.caption("Your personal career advisor. Ask anythong about jobs, skills and growth")

with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Groq API Key", type="password", placeholder="gsk..")
    st.divider()
    persona = st.selectbox("I am a...", ["Student", "Working Professional", "Career Switcher"])
    if st.button("Clear Chat"):
        st.session_state.message = []
        st.rerun()

if not api_key:
    st.warning("Enter your Groq API key in the sidebar to begin")
    st.stop()

persona_context = {
    "Student": "The user is a student exploring career options. Focus on internhsips, entry-level jobs, skill building, and college-to-career transition",
    "Working Professional": "The user is employed and seeking growth. Focus on promotion, upskilling, salary negotiation, and leadership",
    "Career Switcher": "The user wants to change career. Focus on transferable skills, rebranding, roadmaps, and managing the transition risk"
}

SYSTEM_PROMPT = f"""You are an expert career counsellor with 20 years of experience across tech, business, and creative fields.
{persona_context[persona]}
Be concise, empathetic, and actionable. Use bullet points where helpful. Never give generic advice — tailor everything to what the user shares."""

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything about your career..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
                max_tokens=600,
                stream=True
            )
            reply = st.write_stream(chunk.choices[0].delta.content or "" for chunk in response)

    st.session_state.messages.append({"role": "assistant", "content": reply})
