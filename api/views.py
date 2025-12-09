from django.http import JsonResponse

# --- DATOS (Simulando una Base de Datos) ---

# Estudiantes: id, nombre, apellido
STUDENTS_DATA = [
    {"id": 1, "nombre": "Juan", "apellido": "Pérez"},
    {"id": 2, "nombre": "Ana", "apellido": "Gómez"},
    {"id": 3, "nombre": "Carlos", "apellido": "López"},
]

# Tareas: id, nombre, descripción
TASKS_DATA = [
    {"id": 101, "nombre": "Investigación DevOps", "descripcion": "Investigar sobre ArgoCD y Kubernetes"},
    {"id": 102, "nombre": "Desarrollo API", "descripcion": "Crear endpoints en Django"},
    {"id": 103, "nombre": "Pruebas", "descripcion": "Verificar feature flags con LaunchDarkly"},
]

# --- VISTAS (ENDPOINTS) ---

def get_students(request):
    """Retorna la lista de todos los estudiantes"""
    return JsonResponse(STUDENTS_DATA, safe=False)

def get_tasks(request):
    """Retorna la lista de todas las tareas"""
    # Más adelante aquí agregaremos la lógica de LaunchDarkly
    return JsonResponse(TASKS_DATA, safe=False)