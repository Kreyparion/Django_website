import datetime
import pandas as pd
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.template import loader
from cmix import settings
from .forms import ContactForm, PrestaForm
from .models import Presta


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('presta:success')
    return render(request, "email.html", {'form': form})


# def successView(request):
#    return HttpResponse('Success! Thank you for your message.')
def successView(request):
    return render(request, 'success.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PrestaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            presta = form.save(commit=False)
            presta.pub_date = timezone.now()
            presta.save()
            # send mail
            send_mail("Presta Demandée", "{} demande à C-Mix une presta '{}', de type {} à {}. Elle se fera le {} entre {} et {}. Pour plus de détails, contacter: {}, {}. Commentaires aditionnels: {} ".format(presta.presta_respo, presta.presta_name, presta.presta_type, presta.presta_place, presta.presta_date, presta.presta_start, presta.presta_end, presta.presta_respo_phone, presta.presta_respo_mail, presta.presta_comments), settings.EMAIL_HOST_USER, [
                      'holaholaalo131369@gmail.com'], fail_silently=False)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('presta:success'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PrestaForm()

    return render(request, 'name.html', {'form': form})


def list_prestas(request):
    latest_prestas_list = Presta.objects.order_by('-pub_date')[:5]
    context = {'latest_prestas_list': latest_prestas_list}
    return render(request, 'list_prestas.html', context)


def details_prestas(request, presta_id):
    presta = get_object_or_404(Presta, pk=presta_id)
    date = presta.presta_date
    date = datetime.datetime(date.year, date.month, date.day, 0, 0)
    start = presta.presta_start
    start = date.replace(hour=start.hour, minute=0)
    end = presta.presta_end
    end = date.replace(hour=end.hour, minute=0)
    if start.hour > end.hour:
        end += datetime.timedelta(days=1)
    rango = pd.date_range(start=start, end=end, freq="30min")
    return render(request, 'details_presta.html', {'presta': presta, 'range': rango})
