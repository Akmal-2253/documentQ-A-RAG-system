import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(question: str, chunks: list[str]) -> str:
    if not chunks:
        return "I could not find this in the uploaded document."

    context = "\n\n".join(chunks)

    prompt = f"""
You are a document question-answering assistant.

Use ONLY the provided document context to answer the question.

Instructions:
1. Answer only from the context.
2. If the answer is not in the context, say:
   "I could not find this in the uploaded document."
3. Do not add assumptions or outside knowledge.
4. Keep the answer concise and clear.

Document Context:
{context}

User Question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You answer questions strictly from uploaded document context."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=500
        )

        content = response.choices[0].message.content
        return content.strip() if content else "Error: Empty response from model"

    except Exception as e:
        return f"Error generating answer: {str(e)}"