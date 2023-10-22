from django.contrib import admin
from .models import Tareas
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter

class TareasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'state']
    list_filter = (
        ('state', MultiSelectFieldListFilter),
        )

admin.site.register(Tareas, TareasAdmin)