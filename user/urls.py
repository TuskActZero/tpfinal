from django.urls import path
from .views import Registro, LoginPage, home, SecretariaView, ProfesionalesView, GerenciaView, VentasView, TallerView


urlpatterns = [
    path('accounts/singup', Registro.as_view(), name="registrate"),
    path('', home.as_view(), name="casa"),
    path('accounts/login', LoginPage.as_view(), name="login"),
    path('secretaria/', SecretariaView.as_view(), name="secretaria"),
    path('profesional/', ProfesionalesView.as_view(), name="profesional"),
    path('gerencia/', GerenciaView.as_view(), name="gerencia"),
    path('ventas/', VentasView.as_view(), name="Ventas"),
    path('taller/', TallerView.as_view(), name="taller"),

]