import re

STOPWORDS = {
    "the", "and", "a", "an", "of", "to", "in", "on", "for", "with",
    "is", "are", "at", "as", "by", "or", "be", "this", "that", "it",
}

def score_cv(cv_content, job_description):
    """Score a CV against a job description using keyword overlap."""

    cv_words = extract_words(cv_content)
    job_words = extract_words(job_description)

    matching_words = cv_words.intersection(job_words)

    return len(matching_words)

def extract_words(text):
    words = re.findall(r"[a-z]+", text.lower())
    return {word for word in words if word not in STOPWORDS}
