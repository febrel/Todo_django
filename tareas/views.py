from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.


def index(request):

    # Query SQL consulta
    tareas = Tarea.objects.all()

    # Llamo a los formularios
    forms = TareaForm()

    # Si llega algo mediante post
    if (request.method == 'POST'):
        forms = TareaForm(request.POST)

        # Si el formulario es valido
        if(forms.is_valid()):

            # Guardo en la DB
            forms.save()

        # Redirecciono a  /
        return redirect('/')

    contexto = {'tareas': tareas, 'forms': forms}

    return render(request, 'tareas/lista.html', contexto)


def updateTarea(request, pk):

    # Capturo el id de la DB
    tarea = Tarea.objects.get(id=pk)

    # Llamo a los formularios
    forms = TareaForm(instance=tarea)

    if(request.method == 'POST'):

        forms = TareaForm(request.POST, instance=tarea)

        # Si el formulario es valido
        if(forms.is_valid()):

            # Guardo en la DB
            forms.save()

            # Redirecciono a  /
            return redirect('/')

    contexto = {'forms': forms}

    return render(request, 'tareas/update_tareas.html', contexto)


def deleteTarea(request, pk):

    item = Tarea.objects.get(id=pk)

    contexto = {'item': item}

    if(request.method == 'POST'):

        # Elimino de la DB
        item.delete()

        # Redirecciono a  /
        return redirect('/')

    return render(request, 'tareas/delete.html', contexto)
