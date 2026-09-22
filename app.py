import streamlit as st
from groq import Groq


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            text-align: center;
            color: #6b7280;
            margin-bottom: 2rem;
        }

        .stButton > button {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🤖 AI Learning Assistant</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Learn anything with your personal AI tutor."
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# GET GROQ API KEY
# ============================================================

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error(
        "❌ Groq API key is not configured.\n\n"
        "Add GROQ_API_KEY to your Streamlit secrets."
    )
    st.stop()


# ============================================================
# CREATE GROQ CLIENT
# ============================================================

client = Groq(api_key=api_key)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Settings")

    learning_level = st.selectbox(
        "Learning Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
        index=0,
    )

    st.divider()

    st.subheader("📚 Learning Mode")

    learning_mode = st.selectbox(
        "Choose a mode",
        [
            "General Learning",
            "Explain Concept",
            "Code Tutor",
            "Study Notes",
            "Quiz Me",
        ],
    )

    st.divider()

    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Powered by Groq + GPT OSS")


# ============================================================
# SYSTEM PROMPT
# ============================================================

system_prompt = f"""
You are an AI Learning Assistant and personal tutor.

The student's learning level is: {learning_level}.

The selected learning mode is: {learning_mode}.

Your job is to help the student understand topics clearly.

General rules:

1. Explain concepts clearly and accurately.
2. Adjust explanations to the student's learning level.
3. Use simple language when appropriate.
4. Give examples whenever they improve understanding.
5. Break complicated concepts into smaller steps.
6. Do not unnecessarily overwhelm beginners.
7. Encourage the student to understand the reasoning rather than
   simply memorizing answers.
8. If the student asks a programming question, provide clear,
   readable code and explain the important parts.
9. If the student asks for study notes, organize them using
   headings and bullet points.
10. If the student asks for a quiz, ask questions appropriate
    for their learning level.
11. If the student's question is ambiguous, ask a concise
    clarification when necessary.
12. Never claim that you performed an action that you did not perform.

For the selected learning mode:

General Learning:
Help the student learn and understand the topic naturally.

Explain Concept:
Focus on intuitive explanations, examples, analogies, and
step-by-step understanding.

Code Tutor:
Focus on programming concepts, debugging, code examples,
and explanations of how the code works.

Study Notes:
Create concise, well-organized notes with headings,
definitions, important points, and examples.

Quiz Me:
Act as a tutor conducting a quiz. Ask one question at a time
unless the student explicitly asks for multiple questions.
After the student's answer, explain whether it is correct and
why.
"""


# ============================================================
# CHAT SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# WELCOME MESSAGE
# ============================================================

if len(st.session_state.messages) == 0:

    st.info(
        "👋 **Welcome!** Ask me anything you want to learn.\n\n"
        "For example:\n"
        "- Explain Python in simple words\n"
        "- What is machine learning?\n"
        "- Teach me Python loops\n"
        "- Create study notes about databases\n"
        "- Quiz me about HTML"
    )


# ============================================================
# DISPLAY PREVIOUS MESSAGES
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_question = st.chat_input(
    "Ask your AI tutor something..."
)


# ============================================================
# PROCESS USER QUESTION
# ============================================================

if user_question:

    # Add user message to session
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question,
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_question)

    # Prepare messages for Groq
    messages_for_api = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]

    messages_for_api.extend(
        st.session_state.messages
    )

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=messages_for_api,
                    temperature=0.7,
                    max_tokens=2048,
                )

                assistant_answer = (
                    response.choices[0].message.content
                )

                st.markdown(assistant_answer)

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_answer,
                    }
                )

            except Exception as error:

                st.error(
                    "❌ Sorry, something went wrong while "
                    "generating the answer."
                )

                st.caption(
                    f"Error details: {error}"
                )
```
