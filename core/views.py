from django.shortcuts import render
from core.models import Evento
# Create your views here.

# def index(request):
#     return redirect('/agenda/')
#importar redirect dos shortcuts tbm

def lista_eventos (request):
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

