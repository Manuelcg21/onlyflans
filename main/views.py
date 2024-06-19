from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.flanes import flanes
from main.forms import ContactForm, RegisterForm
from main.models import Contact, Flan
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User

class LoginViewPropia(SuccessMessageMixin, LoginView):
    success_message = "Has ingresado correctamente"

# Create your views here.
def index(req):
    #muestra solo los productos publicos de la BDD
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {'flanes_publicos': flanes}
    return render(req, 'index.html', context)
def about(req):
    return render(req, 'about.html')
def contact(req):
    if req.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render(req, 'contact.html', context)
    else:
        form = ContactForm(req.POST)
        if form.is_valid():
            # Esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
            Contact.objects.create(
                **form.cleaned_data
            )
            return redirect('/success')
        context = {'form': form}
        return render(req, 'contact.html', context)

@login_required
def welcome(req):
    #muestra solo los productos privados de la BDD
    flanes_publicos = Flan.objects.filter(is_private=True)
    context = {'flanes_publicos': flanes_publicos}
    return render(req, 'welcome.html', context)

def success(req):
    return render(req, 'success.html')
# def login(req):
#     return render(req, 'login.html')
def register(req):
    #return render(req, 'register.html')
    form = RegisterForm()
    context = {'form': form}
    if req.method == 'GET':
        return render(req, 'registration/register.html', context)
    form = RegisterForm(req.POST)
    if form.is_valid():
        data = form.cleaned_data
        if data['password'] != data['passRepeat']:
            messages.warning(req, "Deben coincidir las contraseñas!")
            return redirect('/accounts/register/')
        User.objects.create_user(data['username'], data['email'], data['password'])
        messages.success(req, "Usuario registrado con éxito!")
    return redirect('/')
