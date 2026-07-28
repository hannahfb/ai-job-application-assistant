import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


def ask_ai(prompt):
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1000,
        thinking={
            "type": "disabled"
        },
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    for block in response.content:
        if block.type == "text":
            return block.text