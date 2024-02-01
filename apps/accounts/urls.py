# apps.accounts.urls.py

# Django and third parties modules
from django.urls import path

# Locals
from apps.accounts import views 

# App namespace
app_name = 'accounts'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
]
