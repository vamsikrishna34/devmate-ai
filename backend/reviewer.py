from transformers import pipeline

# Load CodeT5 model from Hugging Face
review_model = pipeline("text2text-generation", model="Salesforce/codet5-base")

def analyze_code(code: str) -> dict:
    prompt = f"Review this Python code:\n{code}\nProvide a summary, identify issues, and suggest improvements."
    result = review_model(prompt, max_length=512, do_sample=False)

    generated = result[0]['generated_text']

    # Mock parser to split the response (you can upgrade this with regex or tags)
    lines = generated.split('\n')
    summary_lines = [line for line in lines if 'Summary:' in line or 'summary' in line.lower()]
    issue_lines = [line for line in lines if 'Issue' in line or 'issue' in line.lower()]
    suggestion_lines = [line for line in lines if 'Suggest' in line or 'suggestion' in line.lower()]

    feedback = {
        "summary": "\n".join(summary_lines).strip() or "No summary extracted.",
        "issues": issue_lines or ["No issues detected."],
        "suggestions": suggestion_lines or ["No suggestions provided."]
    }

    return feedback
