# from django.shortcuts import render
from django.shortcuts import render_to_response

from principal.models import Bebida

# Create your views here.
def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	return render_to_response('lista_bebidas.html', {'lista':bebidas})