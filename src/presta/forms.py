from django import forms
from .models import Presta
import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]


class PrestaForm(forms.ModelForm):
    class Meta:
        model = Presta
        exclude = ('pub_date',)
        widgets = {
            # 'presta_date': forms.DateTimeInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'presta_date': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={
                'class': 'form-control', 'placeholder': 'Select Date', 'type': 'datetime-local'}),
            # Il faudrait assurer que c'est plus grande que presta_date
            'presta_end': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={
                'class': 'form-control', 'placeholder': 'Select Date', 'type': 'datetime-local'}),
            # 'presta_start': forms.Select(choices=HOUR_CHOICES),
            # 'presta_end': forms.Select(choices=HOUR_CHOICES),
        }


'''
class PrestaForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    date_presta = forms.DateTimeField(label='Date')
'''


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
