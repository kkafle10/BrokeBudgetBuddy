from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('signup/', views.signup_view, name='signup'),
    path('set-budget/', views.set_budget, name='set_budget'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]