from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICE = [
        ('School Expense', 'School Expense'),
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Rent and Utilities', 'Rent and Utilities'),
        ('Other', 'Other')
        
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 50, choices = CATEGORY_CHOICE)
    amount = models.DecimalField(max_digits = 10, decimal_places=2)
    note = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def _str__(self):
        return f"{self.category} - ${self.amount}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"