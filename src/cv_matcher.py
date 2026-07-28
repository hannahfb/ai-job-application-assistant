def score_cv(cv_content, job_description):
    """Score a CV against a job description using keyword overlap."""

    cv_words = set(cv_content.lower().split())
    job_words = set(job_description.lower().split())

    matching_words = cv_words.intersection(job_words)

    return len(matching_words)
