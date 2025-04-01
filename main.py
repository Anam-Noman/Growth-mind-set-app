import streamlit as st

def main():
    st.title("🌟 Growth Mindset Quiz 🌟")
    st.markdown("""
    ### What is a Growth Mindset?
    A **growth mindset** is the belief that abilities and intelligence can be developed through effort, learning, and persistence. 
    Unlike a **fixed mindset** (believing skills are static), a growth mindset helps you embrace challenges and learn from failures.
    """)

    st.header("📝 Take the Quiz!")
    st.write("Answer the following questions to see if you have a growth mindset:")

    # Quiz Questions (Agree = Growth, Disagree = Fixed)
    questions = [
        "1. Intelligence is something you can develop, not just something you're born with.",
        "2. I avoid challenges because I'm afraid of failing.",
        "3. When I make a mistake, I see it as a learning opportunity.",
        "4. Effort is just as important as talent in achieving success.",
        "5. I feel threatened by the success of others.",
    ]

    choices = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    answers = []

    # Display questions and collect answers
    for question in questions:
        answer = st.radio(question, choices, horizontal=True)
        answers.append(answer)

    # Calculate Growth Mindset Score
    if st.button("📊 Get My Results!"):
        score = 0
        for i, answer in enumerate(answers):
            points = choices.index(answer)  # 0-4 (Strongly Disagree to Strongly Agree)
            if i in [1, 4]:  # Reverse score for fixed mindset questions (2 & 5)
                points = 4 - points
            score += points

        total_possible = 4 * len(questions)  # Max score per question = 4
        growth_percentage = (score / total_possible) * 100

        st.subheader("🎯 Your Results")
        st.write(f"**Your Growth Mindset Score: {growth_percentage:.0f}%**")

        if growth_percentage >= 70:
            st.success("🎉 Amazing! You have a strong growth mindset!")
            st.balloons()
        elif growth_percentage >= 40:
            st.warning("👍 You're on the right track! Keep learning and embracing challenges.")
        else:
            st.error("💡 You may lean toward a fixed mindset. Try reframing challenges as learning opportunities!")

        # Tips for Improvement
        st.subheader("🔍 Tips to Develop a Growth Mindset:")
        st.markdown("""
        - **Embrace challenges** as opportunities to grow.  
        - **Learn from mistakes** instead of fearing them.  
        - **Effort matters**—keep practicing and improving.  
        - **Seek feedback** and use it to get better.  
        - **Celebrate progress**, not just results.  
        """)

if __name__ == "__main__":
    main()