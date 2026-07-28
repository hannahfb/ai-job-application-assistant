# AI Job Application Assistant

A command-line tool that matches your CVs against a job description and uses
Claude to suggest and generate tailored edits.

## How it works

1. Loads all `.tex` CVs from `data/cvs/`
2. Prompts you to paste in a job description
3. Scores each CV against the job description by keyword overlap and ranks them
4. Sends the best-matching CV to Claude for suggested edits
5. Lets you approve the suggestions, or describe feedback to revise them (loops until approved)
6. On approval, generates the updated CV and shows a preview
7. Asks whether to save it — if so, prompts for a role name and saves
   to `data/generated_cvs/<cv_name>_<role_name>.tex`

## Project structure

```
src/
├── main.py           # CLI entry point / orchestration
├── ai_client.py       # Anthropic API wrapper
├── cv_loader.py       # Loads .tex CVs from data/cvs/
├── job_input.py       # Collects the job description from stdin
├── cv_matcher.py      # Keyword-overlap scoring
├── prompts.py         # Prompt templates
├── cv_reviewer.py     # Revises suggestions based on user feedback
├── generate_cv.py     # Generates the final updated CV
└── approval.py        # y/n/exit confirmation prompts

data/
├── cvs/               # Your source CVs (.tex) — gitignored, not committed
└── generated_cvs/     # AI-generated CV output — gitignored, not committed
```

## Setup

1. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your-key-here
   ```
4. Create a `data/cvs/` folder and add your CV(s) as `.tex` files to it
   (this folder is gitignored and won't exist on a fresh clone):
   ```
   mkdir data\cvs
   ```

## Usage

Run from the project root (not from inside `src/`) so the relative `data/`
paths resolve correctly:

```
python src/main.py
```

Paste the job description, type `END` on a new line, then follow the prompts.

## Status

Core workflow is functional: CV loading, keyword-based matching, AI-assisted
review with a feedback loop, and CV generation with file output are all
implemented.
