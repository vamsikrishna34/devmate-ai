from backend.api_wrapper import load_model, generate_feedback

def analyze_code(code: str) -> dict:
    """
    Analyze the given code using the model pipeline and return structured feedback.
    """

    # Step 1: Load model (can be swapped with external API or hosted endpoint)
    model = load_model()

    # Step 2: Generate raw feedback text
    raw_output = generate_feedback(code, model)

    # Step 3: Simple parsing — can be upgraded with regex, tags, or structured JSON prompts
    lines = raw_output.split('\n')
    summary_lines = [line for line in lines if 'summary' in line.lower()]
    issue_lines = [line for line in lines if 'issue' in line.lower()]
    suggestion_lines = [line for line in lines if 'suggest' in line.lower() or 'improvement' in line.lower()]

    return {
        "summary": "\n".join(summary_lines).strip() or "No summary provided.",
        "issues": issue_lines or ["No issues detected."],
        "suggestions": suggestion_lines or ["No suggestions available."]
    }
