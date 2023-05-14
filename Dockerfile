# Utiliza una imagen de Python como base
FROM python:3.10.4

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instala las dependencias del sistema requeridas para pycairo
RUN apt-get update && apt-get install -y \
    libcairo2-dev \
    pkg-config

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt
# Copia todo el contenido del directorio actual al contenedor
COPY . .

# Resto de las instrucciones...

# Ejecuta el comando para iniciar tu aplicación (sustituye el comando según tus necesidades)
CMD [ "python", "envia_fms/manage.py", "runserver", "0.0.0.0:8000" ]
