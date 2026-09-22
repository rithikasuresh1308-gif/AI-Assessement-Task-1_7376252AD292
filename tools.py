from config import EXPENSES, COURSE_BUDGET


def get_expense(category):
    category = category.title()

    if category in EXPENSES:
        return EXPENSES[category]

    return f"Unknown category: {category}"


def calculate(expression):
    return eval(expression)


def get_remaining_budget():
    total = sum(EXPENSES.values())
    return COURSE_BUDGET - total