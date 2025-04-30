import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")


client = openai.OpenAI(api_key=api_key)
job_id = "ftjob-ApPJci6AhEp0mMLP942yNtMi"
job = client.fine_tuning.jobs.retrieve(job_id)

print("\nFine-tuning Job Status:")
print("---------------------")
print(f"Job ID: {job.id}")
print(f"Status: {job.status}")
print(f"Model: {job.fine_tuned_model if job.fine_tuned_model else 'Not available yet'}")

if hasattr(job, 'trained_tokens'):
    print(f"Trained tokens: {job.trained_tokens}")

if job.status == "failed":
    print(f"\nError: {job.error}")
elif job.status == "succeeded":
    print("\nFine-tuning completed successfully!")
    print(f"Fine-tuned model ID: {job.fine_tuned_model}")
    print("\nYou can now use this model for completions.") 