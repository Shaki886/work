# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
 
class ContactForm(forms.Form):
	subject = forms.CharField(max_length=255, label=u'Temat', required=True, widget=forms.TextInput(attrs={'size':'40'}))
	msg_content = forms.CharField(widget=forms.Textarea, label=u'Treść wiadomości', required=True)
	sender = forms.EmailField(label=u'Twój adres email', required=True, widget=forms.TextInput(attrs={'size':'40'}))
	cc_sender = forms.BooleanField(required=False, label=u'Wyślij mi kopię tego emaila')
 
def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			msg_content = form.cleaned_data['msg_content']
			sender = form.cleaned_data['sender']
			cc_sender = form.cleaned_data['cc_sender']
			odbiorcy = ['example@example.example']
			if cc_sender:
				odbiorcy.append(sender)
			send_mail(subject, msg_content, sender, odbiorcy)
			return HttpResponseRedirect('/contact/success/')
	else:
		form = ContactForm()
 
	return render_to_response('kontakt.html', {'form': form})
 
def contact_ok(request):
	try:
		referer = request.META['HTTP_REFERER']
	except KeyError:
		return HttpResponseRedirect('/contact/')
	else:
		if referer == 'http://adres/contact/':
			return render_to_response('contact_ok.html', {})
	return HttpResponseRedirect('/contact/')