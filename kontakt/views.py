from django.shortcuts import render_to_response

from kontakt.forms import KontaktForm

def kontakt(request):
	if request.method == "POST":
		kontakt_forms = KontaktForm(request.POST)
		if kontact_form.is_valid():
			success = True
			email = kontact_form.cleaned_data['email']
			title = kontact_form.cleaned_data['title']
			text = kontact_form.cleaned_data['text']
		else:
			kontact_form = KontactForm()

	ctx = {'kontakt_form':kontact_form}
	return render_to_response(request, 'kontakt/kontakt.html', {})