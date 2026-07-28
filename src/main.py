from cv_loader import load_cvs
from job_input import get_job_description
from cv_matcher import score_cv

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

if __name__ =="__main__":
    main()