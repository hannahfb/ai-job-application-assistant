import os
from dotenv import load_dotenv
from anthropic import Anthropic, APIError

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


def ask_ai(prompt, max_tokens=3000):
    try:
        response = client.messages.create(
            model="claude-sonnet-5",
            max_tokens=max_tokens,
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
    except APIError as e:
        raise RuntimeError(f"Claude request failed: {e}") from e

    for block in response.content:
        if block.type == "text":
            if response.stop_reason == "max_tokens":
                print("\nWarning: response was cut off at the max_tokens limit. Output may be incomplete.")
            return block.text

    raise ValueError("Claude response contained no text content.")