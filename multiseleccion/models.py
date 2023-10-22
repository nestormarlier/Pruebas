from django.db import models
from django import forms

class TareasFilterForm(forms.Form):
    ESTADO_TAREA = (
        ('PENDIENTE', 'Pendiente'),
        ('PROCESO', 'En proceso'),
        ('COMPLETADA', 'Completada')
    )
    estado = forms.MultipleChoiceField(
        choices=ESTADO_TAREA,
        required=False,  # Permite que el campo sea opcional
        widget=forms.CheckboxSelectMultiple  # Utiliza checkboxes para la selección múltiple
    )

class Tareas(models.Model):
    ESTADO_TAREA = (
        ('PENDIENTE', 'Pendiente'),
        ('PROCESO', 'En proceso'),
        ('COMPLETADA', 'Completada')
                    )
    nombre=models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=10, choices=ESTADO_TAREA, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='Tareas'