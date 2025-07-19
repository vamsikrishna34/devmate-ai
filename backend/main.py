import argparse
import json
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.code_input import sample_code, load_code_from_file
from backend.reviewer import analyze_code

#  FastAPI app for deployment
app = FastAPI()

#  Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Data model for POST requests
class CodeRequest(BaseModel):
    code: str

@app.get("/")
def root():
    return {"message": "Devmate AI backend is running."}

@app.post("/review")
def review(request: CodeRequest):
    return analyze_code(request.code)

# 🧪 CLI logic (safe to run locally)
def display_feedback(feedback: dict) -> None:
    print("\nSummary:\n")
    print(feedback.get('summary', 'No summary available.'))

    print("\nIssues:\n")
    issues = feedback.get('issues', [])
    if issues:
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No major issues found.")

    print("\nSuggestions:\n")
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
    code = load_code_from_file(args.file) if args.file else sample_code()
    feedback = analyze_code(code)
    display_feedback(feedback)

    if args.save:
        with open("review_output.json", "w") as f:
            json.dump(feedback, f, indent=2)
        print("\nFeedback saved to review_output.json")

if __name__ == "__main__":
    main()
