#encoding: utf-8

#from django.shortcuts import render

from django.http import HttpResponse, Http404
from preguntasyrespuestas.models import Pregunta
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

#imports para el formulario
from django.template import RequestContext
from preguntasyrespuestas.form import PreguntaForm

# Create your views here.
def index(request):
	preguntas = Pregunta.objects.all()

	# respuesta_string = "Preguntas <br/>"
	# respuesta_string += "<br/>".join(["id: %s, asunto: %s"%(p.id, p.asunto) for p in preguntas])

	# return HttpResponse(respuesta_string)

	return render_to_response( 'preguntasyrespuestas/index.html', 
                               {'preguntas': preguntas} ) #preguntas es el diccionario que le pasamos a la template

def pregunta_detalle(request, pregunta_id):
	# Podemos quitar este modo de tratar el erro usando un shortcuts de Django
	# en concreto get_object_or_404

	# try:
	# 	pregunta = Pregunta.objects.get(pk=pregunta_id) #Con este método .get, buscamos un registro por su id (pk - clave principal)
	# except Pregunta.DoesNotExist:
	# 	raise Http404

	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

	# return HttpResponse("%s" % pregunta.asunto)

	return render_to_response( 'preguntasyrespuestas/pregunta_detalle.html', 
                               {'pregunta': pregunta} ) #pregunta es el diccionario que le pasamos a la template

@login_required # Esto es para obligar a esta vista a que el usuario esté registrado
def pregunta_crear(request)	:
	if request.method == 'POST':
		form = PreguntaForm(request.POST)
		if form.is_valid():
			# Todo el codigo de abajo ya no hace falta por que usamos ModelForm
			# pregunta = Pregunta( asunto = form.cleaned_data['asunto'],
   			#                      descripcion = form.cleaned_data['descripcion'],
   			#                      fecha_publicacion = timezone.now() )
			# pregunta.save()
			form.save()
			return redirect('preguntas')
	else:
		form = PreguntaForm()

	return render_to_response( 'preguntasyrespuestas/pregunta_crear.html', 
                               {'form': form},
                               context_instance = RequestContext(request) )

@login_required # Esto es para obligar a esta vista a que el usuario esté registrado
def pregunta_editar(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	if request.method == 'POST':
		form = PreguntaForm(request.POST, instance=pregunta)
		if form.is_valid():
			form.save()
			return redirect('pregunta_detalle', pregunta_id)
	else:
		form = PreguntaForm(instance=pregunta)

	return render_to_response( 'preguntasyrespuestas/pregunta_editar.html', 
                               {'form': form},
                               context_instance = RequestContext(request) )

