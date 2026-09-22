from config import EXPENSES, COURSE_BUDGET


def total_expense():
    return sum(EXPENSES.values())


def highest_expense():
    category = max(EXPENSES, key=EXPENSES.get)
    return category, EXPENSES[category]


def remaining_budget():
    return COURSE_BUDGET - total_expense()


print("SmartSpend - Rule-Based Workflow")

print("\nTotal expense: Rs.", total_expense())

category, amount = highest_expense()
print("Highest expense:", category, "Rs.", amount)

print("Remaining budget: Rs.", remaining_budget())