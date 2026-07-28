def create_cv_review_prompt(job_description, cv):

    return f"""
    You are a CV optimisation assistant.

    Analyse this job description against the selected CV.

    Job description:
    {job_description}

    Selected CV:
    {cv}

    Suggest specific CV edits to better match the role.

    Organise suggestions under:
    - Profile
    - Skills
    - Experience

    Do not invent experience.
    """

def create_revision_prompt(suggested_edits, feedback):

    return f"""
    Revise the CV suggestions based on the user's feedback.

    Original suggestions:
    {suggested_edits}

    User feedback:
    {feedback}

    Return only revised suggestions.
    Do not invent experience.
    """

def create_cv_generation_prompt(cv, job_description, approved_changes):

    return f"""
    You are a CV writing assistant.

    Update the CV using only the approved changes.

    Do not invent experience.

    Job description
    {job_description}

    Original CV:
    {cv}

    Approved changes:
    {approved_changes}

    Return only the raw LaTeX source for the updated CV.
    Do not include any explanation, commentary, or markdown code fences.
    Your response must start with \\documentclass and contain nothing else.
    """