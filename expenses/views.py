from django.shortcuts import render
from .models import Expense

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date_of_expenditure')
    return render(request, 'expenses/expenses_list.html', {'expenses': expenses})