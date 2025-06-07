import streamlit as st
import openai

# Set the page config
st.set_page_config(page_title="Math Problem Solver", page_icon="📐")

# Load API key securely from secrets
client = openai.OpenAI(api_key=st.secrets["openai_api_key"])

# UI
st.title("📐 Universal Math Problem Solver")
st.markdown("Type **any math or statistics question** below and get a detailed solution powered by GPT!")

# User input
question = st.text_area("🧠 Enter your math/statistics question here:")

if st.button("Solve"):
    if question.strip() == "":
        st.warning("❗ Please enter a valid question.")
    else:
        with st.spinner("Solving your problem..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful and accurate math expert. "
                                "Solve the user's math/statistics problem step-by-step. "
                                "Use Markdown and LaTeX formatting where appropriate."
                            ),
                        },
                        {"role": "user", "content": question}
                    ],
                    temperature=0.3
                )
                answer = response.choices[0].message.content
                st.markdown("### ✅ Solution:")
                st.markdown(answer)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
                   
