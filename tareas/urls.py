from django.urls import path
# Llamamos a las urls creadas
from . import views


urlpatterns = [
    path('', views.index, name='lista'),
    path('update_tareas/<str:pk>/', views.updateTarea, name='update_tareas'),
    path('delete_tareas/<str:pk>/', views.deleteTarea, name='delete_tareas'),
]
