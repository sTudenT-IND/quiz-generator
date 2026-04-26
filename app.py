import streamlit as st

st.set_page_config(page_title="Quiz Generator", layout="centered")

st.title("🧠 AI Quiz Generator")

# Input
topic = st.text_input("Enter topic for quiz")

# Button
if st.button("Generate Quiz"):
    st.write("Generating quiz for:", topic)

    # TEMP DEMO (replace later with repo logic)
    questions = [
        {"q": "What is Python?", "options": ["Snake", "Language", "Car", "Food"], "ans": "Language"},
        {"q": "AI stands for?", "options": ["Artificial Intelligence", "Auto Input", "None", "Ask Internet"], "ans": "Artificial Intelligence"}
    ]

    score = 0

    for i, q in enumerate(questions):
        st.subheader(q["q"])
        choice = st.radio("Choose:", q["options"], key=i)

        if st.button(f"Submit {i}"):
            if choice == q["ans"]:
                st.success("Correct ✅")
                score += 1
            else:
                st.error("Wrong ❌")

    st.write("Final Score:", score)
