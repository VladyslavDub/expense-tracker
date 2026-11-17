from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def totals_by_category(expenses):
    total_expenses = {}
    for expense in expenses:
        if expense.category in total_expenses:
            total_expenses[expense.category] = total_expenses[expense.category] + expense.amount
        else:
            total_expenses[expense.category] = expense.amount
    return total_expenses

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date_of_expenditure', '-id')
    form = ExpenseForm()
    stats = totals_by_category(expenses)
    return render(request, 'expenses/expenses_list.html', {'expenses': expenses, 'form': form, 'stats': stats})

def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add.html', {'form': form})