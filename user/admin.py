from django.contrib import admin
from .models import User, Paciente, Producto, Pedido, Turno, Profesional, Secretaria, Ventas, Gerencia, Taller

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    field = '__all__'

class ProfesionalAdmin(admin.ModelAdmin):
    model = Profesional
    field = '__all__'

class SecretariaAdmin(admin.ModelAdmin):
    model = Secretaria
    field = '__all__'

class VentasAdmin(admin.ModelAdmin):
    model = Ventas
    field = '__all__'

class GerenciaAdmin(admin.ModelAdmin):
    model = Gerencia
    field = '__all__'

class TallerAdmin(admin.ModelAdmin):
    model = Taller
    field = '__all__'


# models 
class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    field = '__all__'

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    field = '__all__'

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    field = '__all__'

class TurnoAdmin(admin.ModelAdmin):
    model = Turno
    field = '__all__'

admin.site.register(User, UserAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Turno, TurnoAdmin)

# usuarios
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Secretaria, SecretariaAdmin)
admin.site.register(Ventas, VentasAdmin)
admin.site.register(Gerencia, GerenciaAdmin)
admin.site.register(Taller, TallerAdmin)

