from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from .formulaire import ClientAdminForm


# Create your views here.
def index(request):
    templates = loader.get_template('index.html')
    return HttpResponse(templates.render())


def about(request):
    templates = loader.get_template('about.html')
    return HttpResponse(templates.render())


def service(request):
    templates = loader.get_template('service.html')
    return HttpResponse(templates.render())


def project(request):
    templates = loader.get_template('project.html')
    return HttpResponse(templates.render())


def team(request):
    templates = loader.get_template('team.html')
    return HttpResponse(templates.render())


def contact(request):
    templates = loader.get_template('contact.html')
    return HttpResponse(templates.render())


def appointment(request):
    templates = loader.get_template('appointment.html')
    return HttpResponse(templates.render())


def inscription(request):
    if request.methode == "POST":
        form = ClientAdminForm(request.POST).save()
        return redirect('/')
    else:
        form = ClientAdminForm()
        return render(request, 'inscription.html', {'form': form})
