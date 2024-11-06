from django.contrib import admin
from django.urls import path
from fundacion import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    # URL para home
    path('home/', views.homeView.as_view(), name='home'),
    # URLs para Administrador
    path('administradores/', views.AdministradorListView.as_view(), name='administrador-list'),
    path('administrador/<int:pk>/detail/', views.AdministradorDetailView.as_view(), name='administrador-detail'),
    path('administrador/create/', views.AdministradorCreateView.as_view(), name='administrador-create'),
    path('administrador/<int:pk>/update/', views.AdministradorUpdateView.as_view(), name='administrador-update'),
    
    # URLs para Mascota
    path('mascotas/', views.MascotaListView.as_view(), name='mascota-list'),
    path('mascota/<int:pk>/detail/', views.MascotaDetailView.as_view(), name='mascota-detail'),
    path('mascota/create/', views.MascotaCreateView.as_view(), name='mascota-create'),
    path('mascota/<int:pk>/update/', views.MascotaUpdateView.as_view(), name='mascota-update'),
    path('mascota/<int:pk>/delete/', views.MascotaDeleteView.as_view(), name='mascota-delete'),
    
    # URLs para SolicitudAdopcion
    path('solicitudes/', views.SolicitudAdopcionListView.as_view(), name='solicitudadopcion-list'),
    path('solicitud/<int:pk>/detail/', views.SolicitudAdopcionDetailView.as_view(), name='solicitudadopcion-detail'),
    path('solicitud/create/<int:mascota_id>/', views.SolicitudAdopcionCreateView.as_view(), name='solicitudadopcion-create'),
    path('solicitud/<int:pk>/update/', views.SolicitudAdopcionUpdateView.as_view(), name='solicitudadopcion-update'),
    path('solicitud/<int:pk>/delete/', views.SolicitudAdopcionDeleteView.as_view(), name='solicitudadopcion-delete'),
]

