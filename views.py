from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def jarrbo_home(request):
    return render(request, 'jarrbo_home.html',)
    
def ContactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            content = name + ' heeft het Jarrbo contact formulier ingevuld' + '\n' + \
                        'email adres: ' + email + '\n' + \
                        'onderwerp: ' + subject + '\n' + \
                        message
            try:
                send_mail(subject, content, 'contact@jarrbo.nl', ['contact@jarrbo.nl'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('thanks/')
    
    return render(request, 'contact.html', {
        'form': form,
    })
    
def ThanksView(request):
    return render(request, 'contact_thanks.html',)
    
def ProfileView(request):
    return render(request, 'profile.html',)
