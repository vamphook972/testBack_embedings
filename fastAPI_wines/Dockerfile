# Usa una imagen ligera de Python 3.13
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala dependencias del sistema necesarias para compilación
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto donde corre FastAPI
EXPOSE 8000

# Asegurar que Python busque módulos en /app y arrancar uvicorn apuntando a app.main
ENV PYTHONPATH=/app

# Comando de arranque por defecto (apunta al paquete `app` dentro del directorio de trabajo)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
