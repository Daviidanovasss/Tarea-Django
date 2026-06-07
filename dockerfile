#Se define el sistema operativo y la imagen base
FROM python:3.13-slim

#Se especificael directorio de la carpeta de trabajo
WORKDIR /Tarea_django

#Se copia el fichero de requirements
COPY requirements.txt /Tarea_django/

RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential

#Se instala las dependencias necesarios para el proyecto
RUN pip install --no-cache-dir -r requirements.txt

#Se copia el resto del código en la carpeta de trabajo
COPY . /Tarea_django/

#Se define el puerto donde se ejecuta Django
EXPOSE 8000

#Se despliega el servidor de Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]