# DevMate AI – Code Reviewer and Explainer

DevMate AI is a beginner-friendly static code analysis tool that takes in a Python function, summarizes its purpose, identifies common issues, and suggests basic improvements. It simulates the kind of lightweight review assistance an AI-based learning tool could provide for new developers.

## Features

- Accepts Python code as input
- Provides a high-level summary of what the function does
- Flags possible coding issues (e.g., missing checks, inefficiencies)
- Suggests improvements based on pattern recognition and code structure

## Technologies Used

- Python
- Abstract Syntax Tree (`ast` module)

## How to Run

```bash
python main.py
```

The app will analyze a predefined Python function and print the summary, issues, and suggestions.

## Why This Project

This project was created to explore how natural language explanations and basic static code analysis can help beginners understand and improve their code. It simulates a basic version of an AI assistant for code review.

## Future Improvements

- Accept user input from CLI or text file
- Integrate with large language models (e.g., CodeBERT, GPT) for richer feedback
- Build a Streamlit version for web-based interaction
