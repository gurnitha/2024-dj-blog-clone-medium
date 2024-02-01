# apps/accounts/viewss.py

# Django and third parties modules
from django.shortcuts import render, redirect 
from apps.accounts.forms import NewUserForm
from django.contrib.auth import login 
from django.contrib import messages 

# Locals

# Create your views here.

def user_register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Sign up successfull.")
			return redirect("page:home_page")
		messages.error(request, "Unsuccessful sign up. Invalid information.")
	form = NewUserForm()
	data = { "register_form":form }
	return render(request, 'accounts/register.html', data)
