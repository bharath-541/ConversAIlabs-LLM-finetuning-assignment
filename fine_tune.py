import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
client = openai.OpenAI(api_key=api_key)


response = client.fine_tuning.jobs.create(
    training_file="file-1SDrr42vg4DvVS8NanxVqs",
    model="gpt-3.5-turbo"
)

print("\nFine-tuning Job Details:")
print("----------------------")
print(f"Job ID: {response.id}")
print(f"Status: {response.status}")
print(f"Model: {response.model}")
print(f"Created at: {response.created_at}")
print(f"Training file: {response.training_file}")

print("\nUse this command to check the status:")
print(f"python check_status.py")