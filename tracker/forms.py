from django import forms
from .models import Expense, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'note']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['monthly_budget']
        labels = {
            'monthly_budget': 'Monthly Budget ($)',
        }