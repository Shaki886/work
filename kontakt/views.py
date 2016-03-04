from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from django.core.mail import send_mail
from .forms import KontaktForm

def kontakt(request):
	form_class = KontaktForm
	# if request is not post, initialize an empty form
	form = form_class(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			email = request.POST.get('email')
			title = request.POST.get('title')
			text = request.POST.get('text')
			send_mail('Subject here', text, email, ['testmail@gmail.com'], fail_silently=False)
			return HttpResponseRedirect('/kontaktok/')
	return render(request, 'kontakt/kontakt.html', {'form': form})

