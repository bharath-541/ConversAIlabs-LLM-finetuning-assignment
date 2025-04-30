import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = openai.OpenAI(api_key=api_key)

with open("training_data.jsonl", "rb") as f:
    file = client.files.create(
        file=f,
        purpose="fine-tune"
    )

print("\nFile Upload Details:")
print("-------------------")
print(f"File ID: {file.id}")
print(f"Purpose: {file.purpose}")
print(f"Filename: {file.filename}")
print(f"Bytes: {file.bytes}")
print(f"Created at: {file.created_at}")
print(f"Status: {file.status}")
