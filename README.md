

# ConversAI Labs – Hinglish Voice-AI Fine-Tuning Project

##  Overview
This project demonstrates a mini fine-tuning workflow for adapting OpenAI’s GPT-3.5-turbo model to understand and respond in **code-switched Hinglish** (Hindi + English). It involves:
- Preparing a small dataset of Hinglish dialogues
- Fine-tuning a base LLM using OpenAI's API
- Inference via a fine-tuned model


---

##  Repository Structure

```
├── dataset.jsonl        # Hinglish training data (20 examples)
├── fileupload.py        # Script to upload dataset to OpenAI API
├── fine_tune.py         # Script to fine-tune model
├── check_status.py      # Script to check fine tuning 
├── inference.py         # Script to query fine-tuned model
├── .env                 # Stores API key securely 
└── README.md            # This file
```

---

##  Setup Instructions

1. **Clone Repo**
   ```bash
   git clone https://github.com/bharath-541/ConversAIlabs-LLM-finetuning-assignment.git
   cd ConversAIlabs-LLM-finetuning-assignment
   ```

2. **Set API Key**
   Create a `.env` file in your folder with your OpenAI key:
   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
   ```

---

##  Dataset – `dataset.jsonl`
<img width="1235" alt="Screenshot 2025-04-30 at 3 18 25 PM" src="https://github.com/user-attachments/assets/276f2d7c-f10f-4a0d-a202-15818de1338a" />




###  Format
The dataset consists of 20 conversational Hinglish pairs in the OpenAI fine-tuning chat format:

###  Why these examples?
- **Tone**: Friendly, human-like replies
- **Style**: Code-switched Hindi-English mix
- **Domains**: Daily conversations + basic customer support 
- **Length**: Short, conversational (~1–2 lines)

---

## Uploading_dataset – `fileupload.py`
<img width="1470" alt="Screenshot 2025-04-30 at 3 23 44 PM" src="https://github.com/user-attachments/assets/33728c02-6f34-45f6-82d3-588e6a3393cf" />

python script to upload datset to openAI API and it generates training file id

## Fine-Tuning – `fine_tune.py`
<img width="1470" alt="Screenshot 2025-04-30 at 3 28 18 PM" src="https://github.com/user-attachments/assets/1e8d7df1-69d1-4c23-980b-d7a3ac9c225d" />
using training file id given by fileupload.py and selecting required model we can start fine tuning process




### Why these choices?
- **Model**: `gpt-3.5-turbo` was chosen for speed, cost-efficiency, and good chat understanding.
- **Epochs**:The default number of epochs was used for training, as it is generally optimized for most tasks. You can adjust this value for specific use cases if needed.


---

## Inference – `inference.py`
<img width="1470" alt="Screenshot 2025-04-30 at 3 42 14 PM" src="https://github.com/user-attachments/assets/d3a07703-f43d-4c26-9597-f8e829257485" />
<img width="1470" alt="Screenshot 2025-04-30 at 3 45 10 PM" src="https://github.com/user-attachments/assets/94024057-69ce-4f81-ad51-1f7fd3516a18" />
python script to interact with fine tunned modeln





### Generation Settings
- **Temperature**: Default (1.0) to allow expressive replies
- **Prompt Format**: Standard OpenAI Chat API format

---

## Evaluation Strategy

To evaluate the fine-tuned model:
- **Human Review**: Compare responses vs actual human assistants.
- **Coherence Check**: Logical, relevant replies in Hinglish.
- **Diversity**: Model doesn't repeat the same phrasing often.

---

## Sample Output

**Prompt**: "Mujhe ek coffee pilao."  
**Response**: "Zaroor, ek coffee aapke liye banati hoon"

**Prompt**: "kal meeting arrange kae sakthe ye kya?"  
**Response**: "Haan, ek minute dena, main check karke batata hoon."

---

## Author
- Bharath ([@bharath-541](https://github.com/bharath-541))

---

