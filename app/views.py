from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from app.Carrito import Carrito

# Create your views here.


def base (request):
    return render(request, 'app/base/base.html')

def home (request):
    productos = Producto.objects.all()
    data ={
        'productos': productos
    }
    return render(request, 'app/index.html', data)

def login (request):
    return render(request, 'app/login.html')

def contacto (request):
    data ={
        'form': contactoForm()
    }
    return render(request, 'app/contacto.html',data)

def listadeseos (request):
    return render(request, 'app/listadeseos.html')

def otakumascota (request):
    return render(request, 'app/otakumascota.html')

def cosmujer (request):
    return render(request, 'app/cosmujer.html')

def pago (request):
    return render(request, 'app/pago.html')





@permission_required('app.add_producto')
def agregar_producto(request):

    data ={
''      'form':ProductoForm()

    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Cosplay Registrado")

        else:
            data["form"]= formulario

    return render(request, 'app/crud/agregar.html',data)


@permission_required('app.view_producto')
def listar_producto(request):

    cproductos = Producto.objects.all()
    data ={
        'producto':cproductos
        
    }

 
    return render(request, 'app/crud/listar.html',data)



@permission_required('app.change_producto')
def modificar_producto(request, id):

 
        mproducto = get_object_or_404(Producto, codigo=id)

        data = {
                'form': ProductoForm(instance=mproducto)

            }

        if request.method =='POST':
            formulario = ProductoForm(data=request.POST, instance=mproducto, files =request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request,"Modificado Correctamente")
                return redirect(to="listar_producto")
            data['form'] = formulario


 
        return render(request, 'app/crud/modificar.html',data)


@permission_required('app.delete_producto')
def eliminar_producto(request,id):
    eproducto = get_object_or_404(Producto, codigo=id)
    eproducto.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="listar_producto")


###CARRITO

def carrito (request):
    return render(request, 'app/carrito/carrito.html')


def cagregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("home")


def celiminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def crestar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def climpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")