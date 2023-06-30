from django.urls import path
from .views import *

#Se linkean todas las paginas

urlpatterns = [
    path('base', base, name="base"),
    path('', home, name="home"),
    path('login/',login, name ="login" ),
    path('contacto/',contacto, name ="contacto"),
    path('listadeseos/',listadeseos, name="listadeseos"),
    path('otakumascota/',otakumascota, name="otakumascota"),
    path('cosmujer/',cosmujer, name="cosmujer"),
    path ('agregar-producto/', agregar_producto, name="agregar_producto"),
    path ('listar-producto/', listar_producto, name="listar_producto"),
    path ('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path ('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    
    

    
    

]
