import streamlit as st
from dotenv import load_dotenv

from chains.question_generator import question_chain
from chains.answer_evaluator import evaluation_chain
from chains.feedback_branch import feedback_branch
from chains.final_answer import final_chain


load_dotenv()

# llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# response = llm.invoke("What is the capital of France?")

# print(response.text)


st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="",
    layout="wide",
)

st.title("AI Interview Preparation")
st.caption("Generate questions, answer them, and receive AI-powered coaching.")


# -----------------------------
# Candidate profile
# -----------------------------

st.subheader("1. Candidate Profile")

role = st.text_input(
    "Target Job Role",
    placeholder="e.g. Android Developer",
)

experience = st.selectbox(
    "Experience Level",
    ["0-2 Years", "3-5 Years", "6-8 Years", "9+ Years"],
)

technology = st.text_input(
    "Technology / Skill",
    placeholder="e.g. Kotlin",
)

difficulty = st.selectbox(
    "Interview Difficulty",
    ["Easy", "Medium", "Hard"],
)

question_count = st.slider(
    "Number of Questions",
    1,
    10,
    3,
)


# -----------------------------
# Generate questions
# -----------------------------

if st.button("Generate Interview"):
    if not role or not technology:
        st.warning("Please enter the target role and technology/skill.")
    else:
        with st.spinner("Generating interview questions..."):
            questions_text = question_chain.invoke(
                {
                    "role": role,
                    "experience": experience,
                    "technology": technology,
                    "difficulty": difficulty,
                    "count": question_count,
                }
            )

        questions = [
            q.strip()
            for q in questions_text.splitlines()
            if q.strip()
        ]

        st.session_state.questions = questions
        st.session_state.evaluation = None
        st.session_state.feedback = None
        st.session_state.final_answer = None


# -----------------------------
# Question selection
# -----------------------------

if st.session_state.get("questions"):
    st.subheader("2. Select an Interview Question")

    selected_question = st.radio(
        "Choose one question",
        st.session_state.questions,
    )

    answer = st.text_area(
        "Your Answer",
        height=220,
        placeholder="Write your interview answer here...",
    )

    if st.button("Evaluate Answer"):
        if not answer.strip():
            st.warning("Please enter an answer before evaluating.")
        else:
            with st.spinner("Evaluating your answer..."):
                evaluation = evaluation_chain.invoke(
                    {
                        "question": selected_question,
                        "answer": answer,
                        "role": role,
                        "experience": experience,
                        "technology": technology,
                        "difficulty": difficulty,
                    }
                )

            with st.spinner("Generating personalized feedback..."):
                feedback = feedback_branch.invoke(
                    {
                        "question": selected_question,
                        "answer": answer,
                        "evaluation": evaluation,
                    }
                )

            with st.spinner("Generating improved answer..."):
                final_answer = final_chain.invoke(
                    {
                        "question": selected_question,
                        "answer": answer,
                        "evaluation": evaluation,
                        "feedback": feedback,
                        "role": role,
                        "experience": experience,
                        "technology": technology,
                    }
                )

            st.session_state.evaluation = evaluation
            st.session_state.feedback = feedback
            st.session_state.final_answer = final_answer


# -----------------------------
# Results
# -----------------------------

evaluation = st.session_state.get("evaluation")

if evaluation:
    st.divider()
    st.subheader("3. Evaluation")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Correctness", evaluation.correctness)
    c2.metric("Completeness", evaluation.completeness)
    c3.metric("Clarity", evaluation.clarity)
    c4.metric("Technical Depth", evaluation.technical_depth)

    st.metric("Overall Score", f"{evaluation.overall_score}/10")

    classification = evaluation.classification.replace("_", " ").title()
    st.info(f"Result: {classification}")

    st.subheader("Strengths")
    for item in evaluation.strengths:
        st.write(f"• {item}")

    st.subheader("Improvement Areas")
    for item in evaluation.improvement_areas:
        st.write(f"• {item}")

    st.subheader("Missing Concepts")
    for item in evaluation.missing_concepts:
        st.write(f"• {item}")

    st.subheader("AI Coach Feedback")
    st.write(st.session_state.feedback)

    st.subheader(" Improved Sample Answer")
    st.write(st.session_state.final_answer)