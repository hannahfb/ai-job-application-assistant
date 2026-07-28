from ai_client import ask_ai
from prompts import create_cv_generation_prompt

def generate_cv(
        cv,
        job_description,
        approved_changes
):
    prompt = create_cv_generation_prompt(cv, job_description, approved_changes)
    response = ask_ai(prompt, max_tokens=10000)
    return extract_latex(response)


def extract_latex(text):
    text = text.strip()
    if "```" in text:
        parts = text.split("```")
        if len(parts) >= 2:
            fenced = parts[1].splitlines()
            if fenced and fenced[0].strip().lower() in ("latex", "tex"):
                fenced = fenced[1:]
            return "\n".join(fenced).strip()
    return text