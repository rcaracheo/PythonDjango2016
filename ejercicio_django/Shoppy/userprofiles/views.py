from django.shortcuts import render, redirect
#imports para crear login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#funcion view de login
def authentication(request):
	if request.method == 'POST':
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		if action == 'signup':
			user = User.objects.create_user(username=username, password=password)
			user.save()
		elif action == 'login':
			user = authenticate(username=username, password=password)
			login(request, user)
		return redirect('/hello')

	return render(request, 'login.html', {})

def hello(request):
	return render(request, 'hello.html', {})