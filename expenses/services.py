def totals_by_category(expenses):
    total_expenses = {}
    for expense in expenses:
        if expense.category in total_expenses:
            total_expenses[expense.category] = total_expenses[expense.category] + expense.amount
        else:
            total_expenses[expense.category] = expense.amount
    return total_expenses