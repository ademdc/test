from django import forms
from django.contrib.auth.models import User

class contact_form(forms.Form):
	name	= forms.CharField()
	email 	= forms.CharField()
	phone 	= forms.CharField()
	message = forms.CharField()

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']