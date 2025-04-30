from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:gsdevvs::BRuwB749",
        messages=[
            {"role": "user", "content": "main bored ho gaya hoo"}
        ]
    )
    
    print(response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {str(e)}")
