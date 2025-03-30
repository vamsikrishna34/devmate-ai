# main.py

from code_input import sample_code
from reviewer import analyze_code

def display_feedback(feedback):
    print("\nSummary:")
    print(feedback['summary'])

    print("\nIssues:")
    if feedback['issues']:
        for issue in feedback['issues']:
            print(f"- {issue}")
    else:
        print("No major issues found.")

    print("\nSuggestions:")
    if feedback['suggestions']:
        for suggestion in feedback['suggestions']:
            print(f"- {suggestion}")
    else:
        print("No suggestions at this time.")

def main():
    code = sample_code()
    feedback = analyze_code(code)
    display_feedback(feedback)

if __name__ == "__main__":
    main()
