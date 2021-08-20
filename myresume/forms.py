from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    messages = forms.CharField(max_length=1000)



