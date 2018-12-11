from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
# Create your views here.
def signup(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request,'signup.html',{'form':form})

def logout_view(request):
	if request.method =='POST':
		logout(request)
		return redirect('home')