from django.shortcuts import render, HttpResponse # views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def reportes(request):
    return render(request, 'reportes.html')



def login_view(request):
    # Si el usuario ya está autenticado, redirigir a home
    if request.user.is_authenticated:
        return redirect('home')
    
    # Solo procesar el formulario si es una petición POST
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')
        
        # Intentar autenticar al usuario
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Si el usuario existe y las credenciales son correctas
            login(request, user)
            
            # Configurar la duración de la sesión según "recuérdame"
            if not remember_me:
                request.session.set_expiry(0)
            
            # Redirigir a la página principal
            return redirect('home')
        else:
            # Si las credenciales son incorrectas
            messages.error(request, 'Correo o contraseña incorrectos')
    
    # Si es GET o si falló el POST, mostrar el formulario
    return render(request, 'login.html')


def home_view(request):
    return render(request, 'home.html')