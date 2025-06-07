import streamlit as st
from openai import OpenAI

# Set page title and icon
st.set_page_config(page_title="Math Problem Solver", page_icon="📐")

st.title("📐 Universal Math Problem Solver")
st.markdown("Type **any math or statistics question** below and get a detailed solution powered by GPT!")

# Load API key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai_api_key"])

# Input box for user's question
question = st.text_area("🧠 Enter your math/statistics question here:")

# Solve button
if st.button("Solve"):
    if question.strip() == "":
        st.warning("❗ Please enter a valid question.")
    else:
        with st.spinner("Solving your problem..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4-turbo",  # Or "gpt-3.5-turbo" if needed
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful and accurate math expert. "
                                "Solve the user's math/statistics problem step-by-step "
                                "and format the answer clearly using Markdown and LaTeX where needed."
                            )
                        },
                        {"role": "user", "content": question}
                    ],
                    temperature=0.3
                )
                answer = response.choices[0].message.content.strip()
                st.markdown("### ✅ Solution:")
                st.markdown(answer)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
