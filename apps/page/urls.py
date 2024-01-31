# apps.page.urls.py

# Django and third parties modules
from django.urls import path

# Locals
from apps.page import views 

# App namespace
app_name = 'page'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
