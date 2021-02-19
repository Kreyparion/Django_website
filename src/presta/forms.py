from django import forms
from .models import Presta


class PrestaForm(forms.ModelForm):
    class Meta:
        model = Presta
        exclude = ('pub_date',)


'''
class PrestaForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    date_presta = forms.DateTimeField(label='Date')
'''


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
