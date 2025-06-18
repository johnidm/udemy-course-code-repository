from openai import OpenAI
import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="OpenAI API Example", page_icon=":robot_face:")
st.title("OpenAI API Example")

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = None

def complete_setup():
    st.session_state.setup_complete = True
    st.success("Setup completed successfully!")

def show_feedback():
    st.session_state.feedback_shown = True
    st.success("Feedback shown successfully!")


if not st.session_state.setup_complete:
    st.subheader("Personal information", divider="rainbow")

    if "name" not in st.session_state:
        st.session_state.name = ""
    if "experience" not in st.session_state:
        st.session_state.experience = ""
    if "skills" not in st.session_state:
        st.session_state.skills = ""

    st.session_state.name = st.text_input(
        label="Enter your name:",
        placeholder="Enter your name here",
    )
    st.session_state.experience = st.text_input(
        label="Enter your experience:",
        placeholder="Enter your experience here",
    )
    st.session_state.skills = st.text_input(
        label="Enter your skills:",
        placeholder="Enter your skills here (Python, TensorFlow, PyTorch, OpenAI API)",
    )

    st.subheader("Company and position", divider="rainbow")

    if "position" not in st.session_state:
        st.session_state.position = ""
    if "level" not in st.session_state:
        st.session_state.level = ""
    if "company" not in st.session_state:
        st.session_state.company = ""

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.position = st.selectbox(
            label="Select your position:",
            options=[
                "Software Engineer",
                "Data Scientist",
                "Machine Learning Engineer",
                "AI Researcher",
            ],
        )
    with col2:
        st.session_state.level = st.selectbox(
            label="Select your level:",
            options=["Intern", "Junior", "Mid-level", "Senior", "Lead"],
        )
    st.session_state.company = st.selectbox(
        label="Select your company:",
        options=["Google", "Microsoft", "Amazon", "Facebook", "Apple"],
    )

    if st.button("Complete Setup", on_click=complete_setup):
        st.write("Setup completed successfully!")



if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.info(
        """
        Start by introducing yourself and your experience.
        """, 
        icon="🤖"
    )

    if "openai_model" not in st.session_state:
        st.session_state.openai_model = "gpt-4o"

    if not st.session_state.messages:
        st.session_state.messages = [
            {
                "role": "system",
                "content": f"You are a HR executive that interviews an interviewee named {st.session_state.name}, "
                           f"who has {st.session_state.experience} of experience, "
                           f"and whose skills include {st.session_state.skills}. "
                           f"They work as a {st.session_state.position} at {st.session_state.company} "
                           f"at the {st.session_state.level} level.",
            }
        ]

    for message in st.session_state.messages:
        if message["role"] in ["user", "assistant"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    if st.session_state.user_message_count < 5:

        st.subheader("Chat with the HR Executive", divider="rainbow")

        if prompt := st.chat_input("Enter your prompt:"):
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("user"):
                st.markdown(prompt)

            if st.session_state.user_message_count < 4:
                with st.chat_message("assistant"):
                    with st.spinner("Generating response..."):
                        stream = client.chat.completions.create(
                            model=st.session_state.openai_model,
                            messages=[
                                {"role": m["role"], "content": m["content"] } for m in st.session_state.messages
                            ],
                            stream=True,
                        )

                        response = st.write_stream(stream)

                st.session_state.messages.append({"role": "assistant", "content": response})

            st.session_state.user_message_count += 1

    if st.session_state.user_message_count >= 5:
        st.session_state.chat_complete = True
        st.success("Chat completed! You can now provide feedback.")

if st.session_state.chat_complete and not st.session_state.feedback_shown:
    if st.button("Get Feedback", on_click=show_feedback):
        st.write("Fetching feedback...")

# Show feedback screen
if st.session_state.feedback_shown:
    st.subheader("Feedback")

    conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])

    # Initialize new OpenAI client instance for feedback
    feedback_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Generate feedback using the stored messages and write a system prompt for the feedback
    feedback_completion = feedback_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """You are a helpful tool that provides feedback on an interviewee performance.
             Before the Feedback give a score of 1 to 10.
             Follow this format:
             Overal Score: //Your score
             Feedback: //Here you put your feedback
             Give only the feedback do not ask any additional questins.
              """},
            {"role": "user", "content": f"This is the interview you need to evaluate. Keep in mind that you are only a tool. And you shouldn't engage in any converstation: {conversation_history}"}
        ]
    )

    st.write(feedback_completion.choices[0].message.content)

    # Button to restart the interview
    if st.button("Restart Interview", type="primary"):
            streamlit_js_eval(js_expressions="parent.window.location.reload()") # pip install streamlit-js-eval
