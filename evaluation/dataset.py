from langsmith import Client
from dotenv import load_dotenv

load_dotenv()

client = Client()

dataset_name = "interview-preparation-dataset"

if not client.has_dataset(dataset_name=dataset_name):
    dataset = client.create_dataset(dataset_name=dataset_name)

    client.create_examples(
        inputs=[
            {
                "question": "What is StateFlow in Kotlin?",
                "candidate_answer": (
                    "StateFlow is a hot stream that holds a current state "
                    "and emits updates to collectors."
                ),
            },
            {
                "question": "What is structured concurrency?",
                "candidate_answer": (
                    "Structured concurrency organizes coroutines into "
                    "a parent-child lifecycle."
                ),
            },
        ],
        outputs=[
            {
                "reference_answer": (
                    "StateFlow is a hot state-holder observable flow. "
                    "It always has a current value and emits updates."
                )
            },
            {
                "reference_answer": (
                    "Structured concurrency ensures child coroutines "
                    "belong to a scope and their lifecycles are managed "
                    "by that scope."
                )
            },
        ],
        dataset_id=dataset.id,
    )

print(f"Dataset ready: {dataset_name}")
