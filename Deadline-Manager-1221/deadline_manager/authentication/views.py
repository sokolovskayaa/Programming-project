from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegisterUserForm


def register_request(request):
	if request.user.is_authenticated and request.method == "GET":
		messages.success(request, "You are already logged in." )
		return redirect("/")
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			subject = 'Thank you for registering'
			message = 'Set up your deadlines'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.POST['email'],]
			send_mail( subject, message, email_from, recipient_list, fail_silently=False)
			messages.success(request, "Registration successful." )
			return redirect("register")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.user.is_authenticated and request.method == "GET":
		messages.success(request, "You are already logged in." )
		return redirect("/")
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				subject = 'You\'ve logged successfully'
				message = 'Check up your deadlines'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [user.email,]
				send_mail( subject, message, email_from, recipient_list, fail_silently=False)
				return redirect("login")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.success(request, "You've logged out successfully." )
	return redirect("/")
