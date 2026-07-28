from cv_loader import load_cvs
from job_input import get_job_description
from cv_matcher import score_cv
from ai_client import ask_ai

def main():
    cvs = load_cvs()

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

    prompt = f"""
    You are a CV optimisation assistant.

    Analyse this job description against the selected CV.

    Job description:
    {job_description}

    Selected CV:
    {best_cv["content"]}

    Suggest specific improvements to better match the role.
    Do not invent experience.
    """

    response = ask_ai(prompt)

    print("\nAI Recommendation:")
    print(response)

if __name__ =="__main__":
    main()