from django.contrib import admin

# Register your models here.
from preguntasyrespuestas.models import Pregunta, Respuesta

class RespuestaInline(admin.StackedInline):
	model = Respuesta
	extra = 2

class PreguntaAdmin(admin.ModelAdmin):
	inlines = [RespuestaInline]
	list_display = ('asunto', 'fecha_publicacion', 'publicado_hoy')
	list_filter = ['fecha_publicacion', 'asunto']

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
