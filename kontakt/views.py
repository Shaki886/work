from django.shortcuts import render_to_response

from kontakt.forms import KontaktForm

def kontakt(request):
	if request.method == "POST":
		kontakt_forms = KontaktForm(request.POST)
		if kontakt_form.is_valid():
			success = True
			email = kontakt_form.cleaned_data['email']
			title = kontakt_form.cleaned_data['title']
			text = kontakt_form.cleaned_data['text']
		else:
			kontakt_form = KontactForm()

	ctx = {'kontakt_form':kontakt_form}
	return render_to_response(request, 'kontakt/kontakt.html', {})