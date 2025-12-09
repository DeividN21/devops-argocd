import os
import ldclient
from ldclient.config import Config
from ldclient import Context
from django.http import JsonResponse

# --- CONFIGURACIÓN LAUNCHDARKLY ---
SDK_KEY = os.environ.get('LD_SDK_KEY')

if SDK_KEY:
    ldclient.set_config(Config(SDK_KEY))
else:
    print("ADVERTENCIA: LD_SDK_KEY no configurada.")

# --- DATOS ---
STUDENTS_DATA = [
    {"id": 1, "nombre": "Juan", "apellido": "Pérez"},
    {"id": 2, "nombre": "Ana", "apellido": "Gómez"},
    {"id": 3, "nombre": "Carlos", "apellido": "López"},
]

TASKS_DATA = [
    {"id": 101, "nombre": "Investigación DevOps", "descripcion": "Investigar sobre ArgoCD y Kubernetes"},
    {"id": 102, "nombre": "Desarrollo API", "descripcion": "Crear endpoints en Django"},
    {"id": 103, "nombre": "Pruebas", "descripcion": "Verificar feature flags con LaunchDarkly"},
]

# --- VISTAS ---

def get_students(request):
    return JsonResponse(STUDENTS_DATA, safe=False)

def get_tasks(request):
    """
    Endpoint protegido por LaunchDarkly (vía Context).
    """
    if not SDK_KEY:
        return JsonResponse({"error": "LaunchDarkly no configurado"}, status=503)

    # Constructor Context.builder()
    context = Context.builder('user-anonimo').name('Anonimo').build()

    # Consultar la flag pasando el objeto 'context'
    show_feature = ldclient.get().variation("show-tasks", context, False)

    if show_feature:
        return JsonResponse(TASKS_DATA, safe=False)
    else:
        return JsonResponse(
            {"mensaje": "El servicio de tareas está deshabilitado temporalmente por mantenimiento (LaunchDarkly)."}, 
            status=503
        )