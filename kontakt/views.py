from django.shortcuts import render
from kontakt.forms import KontaktForm
from django.template import RequestContext

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

	except kontakt.DoesNotExist:
		kontakt = None
	ctx = {'kontakt_form':kontakt_form}
	
	return render(request, 'kontakt/kontakt.html', ctx, context_instance=RequestContext(request))

