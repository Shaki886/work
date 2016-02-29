# _*_ coding: utf-8 _*_
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from users.forms import FormularzLogowania
def logowanie(request):
    if request.method == 'POST':
        form = FormularzLogowania(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            login(request,user)
            template = get_template("logowanie.html")
            variables = RequestContext(request,{'user':user})
            output = template.render(variables)
            return HttpResponseRedirect("/")                         
    else: 
        form = FormularzLogowania()
    template = get_template("logowanie.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)