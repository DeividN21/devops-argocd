# Imagen base ligera de Python
FROM python:3.9-slim

# Evita que Python escriba archivos .pyc y fuerza la salida por consola (logs) en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Se establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Se copia el archivo de requerimientos
COPY requirements.txt /app/

# Se instalan las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Se copia el resto del código del proyecto
COPY . /app/

# Se expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
# 0.0.0.0 es necesario para que sea accesible desde fuera del contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]