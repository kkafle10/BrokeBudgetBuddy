from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login
from .models import Expense, UserProfile
from .forms import ExpenseForm, SignUpForm, BudgetForm
from decimal import Decimal

@login_required
def expense_list(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if profile.monthly_budget is None:
        return redirect('set_budget')

    expenses = Expense.objects.filter(user=request.user)
    total = sum(exp.amount for exp in expenses)
    budget = profile.monthly_budget
    balance = budget - total
    balance_class = "alert alert-danger" if balance < 0 else ""

    if total > budget:
        status = "You’re over budget!"
        status_class = "alert alert-danger"
    elif total > budget * Decimal('0.8'):
        status = "Almost there — watch your spending!"
        status_class = "alert alert-warning"
    else:
        status = "Nice job, you’re on track!"
        status_class = "alert alert-good"


    
    
    #Handle form submission
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('/')
    else:
        form = ExpenseForm()

    return render(request, 'expense_list.html', {
        'expenses': expenses,
        'total':total,
        'form': form,
        'status': status,
        'status_class': status_class,
        'budget': budget,
        'balance': balance,
        'balance_class': balance_class
        })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def set_budget(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BudgetForm(instance=profile)
    return render(request, 'set_budget.html', {'form': form})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect('/')