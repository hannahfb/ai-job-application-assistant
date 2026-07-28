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

    print("CV Ranking:")

    for result in scores:
        print(
            f"{result['name']}: {result['score']} matches"
        )

    prompt = f"""
    Analyse this job description and recommend CV improvements.

    Job description:
    {job_description}
    """

    response = ask_ai(prompt)

    print("\nAI Recommendation:")
    print(response)

if __name__ =="__main__":
    main()