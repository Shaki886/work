from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from django.core.mail import send_mail
from .forms import KontaktForm

def kontakt(request):
    kontakt_form = KontaktForm
    # if request is not post, initialize an empty form
    form = kontakt_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
			email = kontakt_form.cleaned_data['email']
			title = kontakt_form.cleaned_data['title']
			text = kontakt_form.cleaned_data['text']

            send_mail('Subject here', msg, email, ['testmail@gmail.com'], fail_silently=False)
            return HttpResponseRedirect('blog/kontakt/')
    return render(request, 'index', {'form': form})

