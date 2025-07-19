import os

def sample_code() -> str:
    # Option 1: Hardcoded sample
    return """
def calculate_total(price, tax_rate):
    total = price + price * tax_rate
    return total
"""

    # Option 2: Load from file (uncomment if needed)
    # try:
    #     with open("examples/sample_code.py", "r") as f:
    #         return f.read()
    # except FileNotFoundError:
    #     return "print('File not found')"
