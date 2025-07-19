from backend.code_input import sample_code
from backend.reviewer import analyze_code

def display_feedback(feedback: dict) -> None:
    print("\n Summary:\n")
    print(feedback.get('summary', 'No summary available.'))

    print("\n Issues:\n")
    issues = feedback.get('issues', [])
    if issues:
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No major issues found.")

    print("\n Suggestions:\n")
    suggestions = feedback.get('suggestions', [])
    if suggestions:
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("No suggestions at this time.")

def main():
    code = sample_code()
    feedback = analyze_code(code)
    display_feedback(feedback)

if __name__ == "__main__":
    main()
