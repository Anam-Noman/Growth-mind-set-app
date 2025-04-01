import streamlit as st
import pandas as pd
import random

def get_random_challenge():
    challenges = [
        "Think of a time you faced a challenge and overcame it. How did you do it?",
        "Learn something new today and write down three key takeaways.",
        "List three things you are grateful for today.",
        "Reframe a recent failure as a learning opportunity.",
        "Set a small, achievable goal for today and track your progress.",
        "Teach something new to someone today.",
        "Write down one fear that holds you back and plan a small step to overcome it.",
        "Give yourself positive feedback for an effort you made today.",
        "Read or watch a motivational story about resilience and reflect on it.",
        "Identify one limiting belief you have and replace it with a growth mindset belief."
    ]
    return random.choice(challenges)

# Streamlit App Layout
st.title("🌱 Growth Mindset Challenge")
st.write("**Embrace challenges and develop a growth mindset!**")

if st.button("Get a New Challenge! 🎯"):
    challenge = get_random_challenge()
    st.write(f"**Your Challenge:** {challenge}")

st.write("### Why Growth Mindset?")
st.write("A growth mindset helps us learn, improve, and embrace challenges rather than fear them. Keep pushing forward!")

st.title("📊 Data Analysis with Pandas")

# CSV file upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.write(df.head())  # Pehli 5 rows show karega

    st.write("### Data Statistics")
    st.write(df.describe())  # Data summary dikhayega

st.markdown("<h5 style='text-align: center;'>Developed By Anam Noman 👩‍💻</h5>", unsafe_allow_html=True)	
