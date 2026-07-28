from ai_client import ask_ai
from prompts import create_revision_prompt

def revise_suggestions(suggested_edits, feedback):
    prompt = create_revision_prompt(suggested_edits, feedback)
    return ask_ai(prompt, max_tokens=4000)