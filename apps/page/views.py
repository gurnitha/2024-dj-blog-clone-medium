# apps/page/viewss.py

# Django and third parties modules
from django.shortcuts import render

# Locals

# Create your views here.

def home_page(request):
	return render(request, 'page/index.html')
