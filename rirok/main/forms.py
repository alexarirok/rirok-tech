from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 30, required=True, help_text='optional')
    email = forms.EmailField(max_length=100, required=True, help_text='required')
    subject = forms.CharField(max_length=50, help_text='optional')
    message = forms.CharField(widget=forms.Textarea, required=True)