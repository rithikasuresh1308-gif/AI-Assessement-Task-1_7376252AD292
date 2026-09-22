import json

from config import EXPENSES, COURSE_BUDGET
from tools import get_expense, calculate, get_remaining_budget


def run_agent(question):
    print("\nQuestion:", question)

    question_lower = question.lower()

    if "books" in question_lower:
        print("Tool: get_expense")
        result = get_expense("Books")
        print("Result:", result)
        print("Final answer: You spent Rs.", result, "on Books.")

    elif "total" in question_lower:
        print("Tool: calculate")
        expression = " + ".join(str(value) for value in EXPENSES.values())
        result = calculate(expression)
        print("Result:", result)
        print("Final answer: Your total expense is Rs.", result)

    elif "remaining" in question_lower or "budget" in question_lower:
        print("Tool: get_remaining_budget")
        result = get_remaining_budget()
        print("Result:", result)
        print("Final answer: Your remaining budget is Rs.", result)

    else:
        print("Final answer: I need a suitable tool to answer this question.")


questions = [
    "How much did I spend on Books?",
    "What is my total expense?",
    "How much budget is remaining?"
]

print("SmartSpend - AI Agent")

for question in questions:
    run_agent(question)