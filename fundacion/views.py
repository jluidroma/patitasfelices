from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from .models import SolicitudAdopcion, Mascota
from .forms import SolicitudAdopcionForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Administrador, Mascota, SolicitudAdopcion

from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        password = request.POST['password']
        
        # Buscar en la tabla Administrador por el nombre
        try:
            admin = Administrador.objects.get(nombre=nombre)
            # Validar si la contraseña ingresada es correcta
            if admin.password == password:
                # Si la validación es exitosa, se guarda al usuario como un administrador
                request.session['is_admin'] = True  # Establecer una variable de sesión
                return redirect('administrador-list')  # Redirigir al dashboard de administrador
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Administrador.DoesNotExist:
            messages.error(request, 'El usuario no existe')
    
    return render(request, 'home.html')
# Vistas para Administrador
class homeView(ListView):
    model = Administrador
    template_name = 'administrador/home.html'
# Vistas para Administrador
class AdministradorListView(ListView):
    model = Mascota
    template_name = 'administrador/administrador-list.html'

class AdministradorDetailView(DetailView):
    model = Administrador
    template_name = 'administrador/administrador-detail.html'

class AdministradorCreateView(CreateView):
    model = Administrador
    fields = '__all__'
    template_name = 'administrador/administrador-create.html'

class AdministradorUpdateView(UpdateView):
    model = Administrador
    fields = '__all__'
    template_name = 'administrador/administrador-update.html'


# Vistas para Mascota
class MascotaListView(ListView):
    model = Mascota
    template_name = 'mascota/mascota-list.html'

class MascotaDetailView(DetailView):
    model = Mascota
    template_name = 'mascota/mascota-detail.html'

class MascotaCreateView(CreateView):
    model = Mascota
    fields = '__all__'
    template_name = 'mascota/mascota-create.html'
    success_url = reverse_lazy('administrador-list')


class MascotaUpdateView(UpdateView):
    model = Mascota
    fields = '__all__'
    template_name = 'mascota/mascota-update.html'
    success_url = reverse_lazy('administrador-list')

class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota-delete.html'
    success_url = reverse_lazy('administrador-list')

# Vistas para SolicitudAdopcion
class SolicitudAdopcionListView(ListView):
    model = SolicitudAdopcion
    template_name = 'solicitud/solicitudadopcion-list.html'

class SolicitudAdopcionDetailView(DetailView):
    model = SolicitudAdopcion
    template_name = 'solicitud/solicitudadopcion-detail.html'



class SolicitudAdopcionCreateView(CreateView):
    model = SolicitudAdopcion
    form_class = SolicitudAdopcionForm
    template_name = 'solicitud/solicitudadopcion-create.html'
    success_url = reverse_lazy('mascota-list')  # Redirige a la lista de mascotas después de crear

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mascota_id = self.kwargs.get('mascota_id')  # Obtiene el id de la URL
        mascota = get_object_or_404(Mascota, pk=mascota_id)  # Busca la mascota en la BD
        context['mascota'] = mascota
        return context

    def form_valid(self, form):
        mascota_id = self.kwargs.get('mascota_id')
        mascota = get_object_or_404(Mascota, pk=mascota_id)
        form.instance.mascota = mascota  # Asocia la mascota con la solicitud
        return super().form_valid(form)



# class SolicitudAdopcionUpdateView(UpdateView):
#     model = SolicitudAdopcion
#     template_name = 'solicitud/solicitud-update.html'
#     fields = '__all__'
    
class SolicitudAdopcionUpdateView(UpdateView):
    model = SolicitudAdopcion
    template_name = 'solicitud/solicitudadopcion-update.html'
    fields = ['estado_solicitud']  # Solo vamos a permitir la edición de este campo

    def get_success_url(self):
        # Después de aceptar la solicitud, redirigir a la lista de solicitudes
        return reverse_lazy('solicitudadopcion-list')

    def form_valid(self, form):
        # Comprobamos si el formulario fue enviado con la acción de "Aceptar" o "Rechazar"
        if 'aceptar' in self.request.POST:
            form.instance.estado_solicitud = 'Aprobada'  
        elif 'rechazar' in self.request.POST:
            form.instance.estado_solicitud = 'Rechazada'  
        return super().form_valid(form)

class SolicitudAdopcionDeleteView(DeleteView):   
    model = SolicitudAdopcion
    template_name = 'solicitud/solicitudadopcion-delete.html'
    success_url = reverse_lazy('solicitudadopcion-list')  # Redirige después de eliminar


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Mascota, SolicitudAdopcion
from .forms import SolicitudAdopcionForm

def solicitud_adopcion(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)  # Obtiene la mascota seleccionada
    
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.mascota = mascota  # Asigna la mascota a la solicitud
            solicitud.save()  # Guarda la solicitud en la base de datos
            messages.success(request, "¡Solicitud de adopción enviada con éxito!")
            return redirect('home')  # Redirige al usuario a la página principal después de guardar
    else:
        form = SolicitudAdopcionForm()

    return render(request, 'solicitud_adopcion.html', {'form': form, 'mascota': mascota})
