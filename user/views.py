from django.shortcuts import render, render, redirect, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, FormView
from django.urls import reverse_lazy
from .forms import  UserForm, PacienteForm
from .models import User, Paciente
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout as do_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate


# Create your views here.

# home de la pagina


class home(TemplateView):
    template_name = 'home.html'

class Registro(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/registro.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('casa')

    def get_success_url(self):

        rol = int(self.request.user.sector)
        if rol ==  'secretaria':
            return reverse_lazy('secretaria')
        elif rol == 'gerencia':
            return reverse_lazy('gerencia')
        elif rol == 'ventas':
            return reverse_lazy('ventas')
        elif rol == 'taller':
            return reverse_lazy('taller')
        elif rol == 'profesional':
            return reverse_lazy('profesional')

        return reverse_lazy('casa')


class LoginPage(LoginView):
    model = User
    form_class = UserForm
    template_name = 'registration/login.html'

    def get_success_url(self):

        rol = int(self.request.user.sector)
        if rol ==  'secretaria':
            return reverse_lazy('secretaria')
        elif rol == 'gerencia':
            return reverse_lazy('gerencia')
        elif rol == 'ventas':
            return reverse_lazy('ventas')
        elif rol == 'taller':
            return reverse_lazy('taller')
        elif rol == 'profesional':
            return reverse_lazy('profesional')

        return reverse_lazy('casa')


# views de las paginas 

class SecretariaView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'secretaria.html'
    success_url = reverse_lazy('lista_paciente')

class ListaPaciente(ListView):
    model = Paciente
    template_name = 'lista_paciente'
    context_object_name = 'Paciente'

class ProfesionalesView(TemplateView):
    template_name = 'profesionales.html'

class TallerView(TemplateView):
    template_name = 'taller.html'

class GerenciaView(TemplateView):
    template_name = 'Gerencia.html'

class VentasView(TemplateView):
    template_name = 'ventas.html'


def logout(request):
    do_logout(request)
    return redirect('/')
