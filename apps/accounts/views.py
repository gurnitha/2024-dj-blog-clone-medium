# apps/accounts/viewss.py

# Django and third parties modules
from django.shortcuts import render, redirect 
from apps.accounts.forms import NewUserForm
from django.contrib.auth import login, authenticate  
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm

# Locals

# Create your views here.

def user_register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, f'{request.user.username } Sign up successfull.')
			return redirect("page:home_page")
		# messages.error(request, "Unsuccessful sign up. Invalid information.")
		messages.error(request, 'Unsuccessful sign up. Invalid information.')
	form = NewUserForm()
	data = { "register_form":form }
	return render(request, 'accounts/register.html', data)


def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("page:home_page")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()

	data = {'login_form':form}
	return render(request, 'accounts/login.html', data)

