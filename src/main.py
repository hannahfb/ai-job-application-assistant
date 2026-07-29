import os
from cv_loader import load_cvs
from job_input import get_job_description
from cv_matcher import score_cv
from ai_client import ask_ai
from generate_cv import generate_cv
from cv_reviewer import revise_suggestions
from approval import get_confirmation
from prompts import create_cv_review_prompt
from pathlib import Path

def main():
    cvs = load_cvs()

    if not cvs:
        print("No CVs found.")
        return

    print(f"Found {len(cvs)} CVs")

    job_description = get_job_description()

    print("\nMatching CVs...\n")

    scores = []

    for cv in cvs:
        score = score_cv(
            cv["content"],
            job_description
        )

        scores.append(
            {
                "name": cv["name"],
                "score": score,
            }
        )

    scores.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    best_cv = next(
        cv for cv in cvs
        if cv["name"] == scores[0]["name"]
    )

    print("CV Ranking:")

    for result in scores:
        print(
            f"{result['name']}: {result['score']} matches"
        )

    prompt = create_cv_review_prompt(
        job_description,
        best_cv["content"]
    )

    suggested_edits = ask_ai(prompt, max_tokens=5000)

    print("\nAI Recommendation:")
    print(suggested_edits)

    while True:
        approval = get_confirmation("Approve changes?")

        if approval == "y":
            break

        if approval == "exit":
            print("Exiting CV workflow.")
            return

        feedback = input(
            "\nDescribe what you would like changed."
        )

        suggested_edits = revise_suggestions(
            suggested_edits,
            feedback
        )

        print("\nRevised suggestions:")
        print(suggested_edits)

    print("\nConfirmed changes:")
    print(suggested_edits)

    updated_cv = generate_cv(
        best_cv["content"],
        job_description,
        suggested_edits
    )

    print("\nCV Preview:")
    print(updated_cv)

    save_cv = get_confirmation("Save this CV?")

    if save_cv == "y":
        role_name = input("\nEnter a role name for this CV: ").strip()
        safe_role_name = role_name.lower().replace(" ", "_")

        raw_user_name = os.getenv("USER_NAME")
        if not raw_user_name:
            print("\nWarning: USER_NAME not set in .env — using 'cv' as a placeholder in the filename.")
            raw_user_name = "cv"

        user_name = raw_user_name.lower().replace(" ", "_")

        output_dir = Path("data/generated_cvs")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / f"{user_name}_{safe_role_name}.tex"
        output_path.write_text(updated_cv, encoding="utf-8")

        print(f"\nUpdated CV saved to {output_path}")
        return

    if save_cv == "n":
        print("CV not saved.")
        return

    if save_cv == "exit":
        print("Exiting CV workflow.")
        return

if __name__ =="__main__":
    main()