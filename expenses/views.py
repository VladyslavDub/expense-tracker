from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm
from .services import totals_by_category

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
    return redirect('expense_list')

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date_of_expenditure', '-id')
    form = ExpenseForm()
    edit_form = ExpenseForm(auto_id='edit_%s')
    stats = totals_by_category(expenses)
    categories = Expense.objects.values_list('category', flat=True).distinct().order_by('category')
    return render(request, 'expenses/expenses_list.html', {'expenses': expenses, 'form': form, 'stats': stats, 'categories': categories, 'edit_form': edit_form})

def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense added.')
    else:
        for field, errors in form.errors.item():
            messages.error(request, f'{field}: {"".join(errors)}')
    return redirect('expense_list')

def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated.')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f'{field}: {"".join(errors)}')
    return redirect('expense_list')