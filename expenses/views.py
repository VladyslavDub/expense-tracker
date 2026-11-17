from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date_of_expenditure', '-id')
    form = ExpenseForm()
    return render(request, 'expenses/expenses_list.html', {'expenses': expenses, 'form': form})

def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add.html', {'form': form})