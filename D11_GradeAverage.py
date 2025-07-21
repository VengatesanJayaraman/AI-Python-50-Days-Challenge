import streamlit as st

# App title
st.title("🎓 Test Score Average Checker (with Subject Pass Requirement)")

st.write("Enter the scores for 5 subjects (each out of 100):")

# Input fields for 5 test scores
score1 = st.number_input("Subject 1 Score", min_value=0, max_value=100, step=1)
score2 = st.number_input("Subject 2 Score", min_value=0, max_value=100, step=1)
score3 = st.number_input("Subject 3 Score", min_value=0, max_value=100, step=1)
score4 = st.number_input("Subject 4 Score", min_value=0, max_value=100, step=1)
score5 = st.number_input("Subject 5 Score", min_value=0, max_value=100, step=1)

# Button to calculate result
if st.button("Calculate Result"):
    scores = [score1, score2, score3, score4, score5]
    average = sum(scores) / len(scores)

    st.subheader(f"📊 Average Score: {average:.2f}")

    # Check for individual subject pass and overall average
    if all(score >= 40 for score in scores) and average >= 40:
        st.success("✅ Result: Pass")
    else:
        st.error("❌ Result: Fail (Must score 40+ in all subjects and average ≥ 40)")
