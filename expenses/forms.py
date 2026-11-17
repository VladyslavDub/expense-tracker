from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'amount', 'category', 'date_of_expenditure']
        widgets = {
            'date_of_expenditure' : forms.DateInput(attrs={'type': 'date'}),
        }