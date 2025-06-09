from django.contrib import admin
from .models import Tutor, Vet, Cadastro  # Ajuste conforme seus modelos

admin.site.register(Tutor)
admin.site.register(Vet)
admin.site.register(Cadastro)