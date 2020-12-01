from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Paciente
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password1", "sector"]

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        field = '__all__'


        