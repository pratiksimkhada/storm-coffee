from django import forms


class ContactForm(forms.Form):
	full_name = forms.CharField(max_length = 200)
	email_address = forms.EmailField(max_length = 200)
	message = forms.CharField(widget = forms.Textarea(attrs={'class':'materialize-textarea'}))
