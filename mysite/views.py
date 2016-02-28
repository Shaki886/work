from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import

def logowanie(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('logowanie.html', c)
	
def auth_view(request):
	email = request.POST.get('email', '')
	haslo = request.POST.get('haslo', '')
	user = auth.authenticate(email=email, haslo=haslo)
	
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/user/index')
	else:
        return HttpResponseRedirect('/user/invalid')
		
def loggedin(request):
    return render_to_response('index.html',
	                         {'full_name': request.user.username})
							 
def invalid_login(request):
	auth.logout(request)
	return render_to_response('logout.html')