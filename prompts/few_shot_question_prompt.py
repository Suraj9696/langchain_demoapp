# from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# examples = [
#     {
#         "profile": "Android Developer, 3 years, Kotlin, Medium",
#         "question": "What is the difference between StateFlow and LiveData?",
#     },
#     {
#         "profile": "Android Developer, 8 years, Kotlin, Hard",
#         "question": (
#             "Design an offline-first Android architecture using Room, "
#             "Flow and WorkManager."
#         ),
#     },
#     {
#         "profile": "Android Developer, 10 years, Kotlin, Hard",
#         "question": (
#             "How would you diagnose and resolve memory leaks in a "
#             "large-scale Android application?"
#         ),
#     },
# ]


# example_prompt = PromptTemplate(
#     template="Profile: {profile}\nQuestion: {question}",
#     input_variables=["profile", "question"],
# )


# few_shot_question_prompt = FewShotPromptTemplate(
#     example_prompt=example_prompt,
#     examples=examples,
#     prefix=(
#         "You are an expert technical interviewer. Generate a relevant "
#         "interview question based on the candidate profile."
#     ),
#     suffix="Profile: {profile}",
#     input_variables=["profile"],
# )
