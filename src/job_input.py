def get_job_description():
    """Collect the job description from the user."""

    print("Paste the job description below.")
    print("When finished, type END on a new line.")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    return "\n".join(lines)