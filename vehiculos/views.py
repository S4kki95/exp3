from django.shortcuts import render,redirect
from .models import Vehiculo
from .forms import VehiculoForm,RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
     return render(request, 'index.html')

@login_required
def otra(request):
     vehiculos = Vehiculo.objects.raw('select * from vehiculos_vehiculo')
     datos={
          'autitos':vehiculos
     }
     return render(request, 'otra.html', datos)

     '''
     vehiculos = Vehiculo.objects.all() #similar a select * from vehiculo
     datos ={'autitos':vehiculos}
     return render(request, 'otra.html',datos)
     '''
@login_required
def crear(request):
     if request.method=="POST":    
          vehiculoform = VehiculoForm(request.POST, request.FILES)    #creamos un objeto de tipo Formulario
          if vehiculoform.is_valid():
               vehiculoform.save()      #similar al insert de sql en función 
               return redirect('otra')
     else: 
          vehiculoform=VehiculoForm()
     return render(request, 'crear.html', {'vehiculo_form':vehiculoform})



@login_required
def eliminar(request, id):
     vehiculoEliminado = Vehiculo.objects.get(patente=id)   #select * from Vehiculo where patente=id
     vehiculoEliminado.delete()
     return redirect ('otra')

@login_required
def modificar(request, id):
     vehiculoModificado=Vehiculo.objects.get(patente=id)
     datos = {
          'form' : VehiculoForm(instance=vehiculoModificado)
     }
     if request.method=='POST':
          formulario = VehiculoForm(data=request.POST, instance=vehiculoModificado)
          if formulario.is_valid:
               formulario.save()
               return redirect('otra')
     return render(request, 'modificar.html', datos)


def registrar(request):
     data={
          'form' : RegistroUserForm()
     }
     if request.method=="POST":
          formulario = RegistroUserForm(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user=authenticate(username=formulario.cleaned_data["username"],
                                 password=formulario.cleaned_data["password1"])
               login(request, user)
               return redirect('index')
          data["form"]=formulario
     return render(request, 'registration/registrar.html',data)

@login_required
def mostrar(request):
     autitos = Vehiculo.objects.all()
     datos={
          'autitos':autitos
     }
     return render(request, 'mostrar.html', datos)
