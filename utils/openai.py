import os
from openai import OpenAI

def gen_answer():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "generate a python question with 1 correct answer, and 3 wrong answer. generate explanations for each answer",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print('chat_completion: ', chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content