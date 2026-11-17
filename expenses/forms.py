from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'amount', 'category', 'date_of_expenditure']
        widgets = {
            'date_of_expenditure' : forms.DateInput(attrs={'type': 'date'}),
            'category': forms.TextInput(attrs={'list': 'category-list', 'autocomplete': 'off'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError('Amount must be greater than zero.')
        return amount

