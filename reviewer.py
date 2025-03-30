# reviewer.py

import ast

def analyze_code(code):
    feedback = {
        "summary": "",
        "issues": [],
        "suggestions": []
    }

    try:
        tree = ast.parse(code)
    except SyntaxError:
        feedback["summary"] = "Invalid Python code."
        return feedback

    # Basic summary
    if "factorial" in code:
        feedback["summary"] = "This function calculates the factorial of a number recursively."
    else:
        feedback["summary"] = "Function found. Performs operations depending on the logic."

    # Issue checks
    if "input(" in code and "int(" not in code:
        feedback["issues"].append("Input might not be properly converted to integer.")

    if "factorial(n - 1)" in code and "if n == 0" in code:
        feedback["issues"].append("No check for negative input. Could cause infinite recursion.")

    # Suggestions
    if "factorial" in code and "math.factorial" not in code:
        feedback["suggestions"].append("Consider using math.factorial() for efficiency.")

    if "return" in code and "print" not in code:
        feedback["suggestions"].append("Add print statements to visualize the output during testing.")

    return feedback
