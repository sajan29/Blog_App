from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def signup(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/blog')
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{'form':form})

# def profile(request):
# 	return redirect('/blog')

# def password_change_done(request):
# 	return render(request,'registration/password_change_done.html')