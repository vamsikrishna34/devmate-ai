import logging
import re
from transformers import pipeline

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_feedback(generated: str) -> dict:
    lines = generated.strip().split("\n")
    summary_lines, issue_lines, suggestion_lines = [], [], []

    for line in lines:
        line_lower = line.lower()
        if "summary" in line_lower:
            summary_lines.append(re.sub(r"(?i)^summary:?", "", line).strip())
        elif "issue" in line_lower:
            issue_lines.append(re.sub(r"(?i)^issue:?", "", line).strip())
        elif "suggest" in line_lower:
            suggestion_lines.append(re.sub(r"(?i)^suggest(ion)?:?", "", line).strip())

    return {
        "summary": " ".join(summary_lines) or "No summary extracted.",
        "issues": issue_lines or ["No issues detected."],
        "suggestions": suggestion_lines or ["No suggestions provided."]
    }

def analyze_code(code: str) -> dict:
    logger.info("Received code for review.")
    prompt = f"Review this Python code:\n{code}\nProvide a summary, identify issues, and suggest improvements."

    try:
        # Lazy-load the smaller model
        review_model = pipeline("text2text-generation", model="Salesforce/codet5-small")
        result = review_model(prompt, max_length=512, do_sample=False)
        generated_text = result[0].get("generated_text", "").strip()

        if not generated_text:
            logger.warning("Empty feedback from model.")
            return {
                "summary": "No feedback generated.",
                "issues": [],
                "suggestions": []
            }

        feedback = parse_feedback(generated_text)
        logger.info("Feedback extracted successfully.")
        return feedback

    except Exception as e:
        logger.error(f"Error during code analysis: {e}")
        return {
            "summary": "Error generating feedback.",
            "issues": [],
            "suggestions": []
        }
