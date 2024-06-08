from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Inmueble, Perfil
from .forms import UserForm, CustomAuthenticationForm, PerfilForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'index.html', {'inmuebles': inmuebles})

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')  
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            ultimo_usuario_creado = authenticate(request, username=username, password=password)
            login(request, ultimo_usuario_creado)
            return redirect('profile')  
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required    
def bienvenido(request):
    return render(request, 'welcome.html')

@login_required
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile(request):
    perfil = Perfil.objects.get(usuario=request.user)
    return render(request, 'profile.html', {'perfil': perfil})

def register_profile(request):
    usuario = request.user 
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            usuario = usuario
            tipo = form.cleaned_data['tipo_usuario']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            correo = usuario.email
            
            datos = Perfil(
                usuario=usuario,
                tipo_usuario=tipo,
                rut=rut,
                direccion=direccion,
                telefono=telefono,
                correo=correo,
                )
            datos.save()
            return HttpResponseRedirect('/profile/')
            
    else:
    #si es que tenemos el metodo get
        form = PerfilForm()
        context = {
            'form':form,
            'title':'Crear perfil'
        }
    return render(request, 'register_profile.html', context)
    

def update_profile(request):
    usuario = request.user
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = Perfil.objects.filter(usuario=usuario).update(**form.cleaned_data)
            return redirect('profile')
    else: 
        perfil = Perfil.objects.filter(usuario=usuario)
        if perfil.exists():
            perfil = perfil.first()
            form = PerfilForm(instance=perfil)
            context = {
                'form':form,
                'title':'Actualizar Perfil'
            }

        return render(request, 'update_profile.html', context)