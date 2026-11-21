from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpenseForm
from .models import Expense
from .services import totals_by_category


def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense.delete()
    return redirect("expense_list")


def expense_list(request):
    expenses = Expense.objects.all().order_by("-date_of_expenditure", "-id")
    form = ExpenseForm()
    edit_form = ExpenseForm(auto_id="edit_%s")
    stats = totals_by_category(expenses)
    total = sum(stats.values())
    categories = (
        Expense.objects.values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )
    selected_category = request.GET.get('category')
    filtered = expenses
    search = request.GET.get('q', '')
    if search:
        filtered = filtered.filter(title__icontains=search)
    if selected_category:
        filtered = filtered.filter(category=selected_category)
    return render(
        request,
        "expenses/expenses_list.html",
        {
            "expenses": filtered,
            "form": form,
            "stats": stats,
            "selected_category": selected_category,
            "categories": categories,
            "edit_form": edit_form,
            "total": total,
            'search': search,
        },
    )


def expense_add(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense added.")
    else:
        for field, errors in form.errors.item():
            messages.error(request, f"{field}: {''.join(errors)}")
    return redirect("expense_list")


def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated.")
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {''.join(errors)}")
    return redirect("expense_list")
