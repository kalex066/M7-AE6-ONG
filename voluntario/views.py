from django.shortcuts import render, redirect, get_object_or_404
from .models import Voluntario
from .forms import VoluntarioForm, EventoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Evento
from django.urls import reverse_lazy

# LOS VOLUNTARIOS SE  MANEJARAN CON VISTAS BASADAS EN FUNCIONES
# en home mostrare el listado de voluntarios, Read del CRUD
def home(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'home.html', {"voluntarios":voluntarios})


# Registro ode Voluntarios, Create del CRUD
def registrar(request):
    form = VoluntarioForm()
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'formulario.html', {"form": form})

# Edicion de Voluntarios, Update del CRUD
def editar(request,id):
    voluntarios = get_object_or_404(Voluntario, id=id)
    form = VoluntarioForm(instance=voluntarios)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntarios)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render (request, 'formulario.html', {"form":form})

#Eliminar Voluntario, Delete del CRUD
def eliminar(request,id):
    voluntarios = get_object_or_404(Voluntario, id=id)
    voluntarios.delete()
    return redirect('home')

# Vista de datos de los voluntarios
def datos(request, id):
    voluntarios = get_object_or_404(Voluntario, id=id)
    return render(request, 'datos.html', {"voluntarios": voluntarios})

# LOS EVENTOS SE MANEJARAN CON VISTAS BASADAS EN CLASES

# Ver listado de eventos. Read del CRUD
class EventoListView(ListView):
    model = Evento
    template_name = "eventos.html"
    context_object_name = "eventos"

# Crear nuevo evento, Create del CRUD
class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "formulario_eventos.html"
    success_url = reverse_lazy("ver_eventos")

# Actualizar un evento, Update del CRUD
class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = "formulario_eventos.html"
    success_url = reverse_lazy("ver_eventos")

# Borrar un evento, Delete del CRUD
class EventoDeleteView(DeleteView):
    model = Evento
    template_name = "confirmar_borrado_eventos.html"
    success_url = reverse_lazy("ver_eventos")

#Detalle de los eventos
class EventoDetailView(DetailView):
    model = Evento
    template_name = "detalle_evento.html"
    context_object_name = "eventos"

