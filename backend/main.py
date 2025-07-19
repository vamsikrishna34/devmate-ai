import argparse
import json
from backend.code_input import sample_code, load_code_from_file
from backend.reviewer import analyze_code

def display_feedback(feedback: dict) -> None:
    print("\ Summary:\n")
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
    parser = argparse.ArgumentParser(description="Run Devmate AI reviewer.")
    parser.add_argument("--file", type=str, help="Path to your code file")
    parser.add_argument("--save", action="store_true", help="Save feedback to review_output.json")
    args = parser.parse_args()

    # Load code sample
    if args.file:
        code = load_code_from_file(args.file)
    else:
        code = sample_code()

    feedback = analyze_code(code)
    display_feedback(feedback)

    if args.save:
        with open("review_output.json", "w") as f:
            json.dump(feedback, f, indent=2)
        print("\n Feedback saved to review_output.json")

if __name__ == "__main__":
    main()
