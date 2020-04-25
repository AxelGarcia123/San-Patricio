# San-Patricio

Sistema de control para colegio de artes y deportes.

### Introducción

Servidor web creado en Flask para controlar y gestionar datos de un colegio de artes y deportes.

### Pre-requisitos

* [Python](https://www.python.org/downloads/release/python-382/) - Necesario para ejecutar Flask
* [Git](https://git-scm.com/downloads) - Para gestionar repositorios

### Instrucciones para ejecutar el servidor

#### Clonar el repositorio

A través de la línea de comandos o Powershell ejecuta:

```
git clone https://github.com/ranchTrash/San-Patricio.git
```

Ingresa a la carpeta de la repo clonada, y después hasta la carpeta _src_:

```
cd San-Patricio
cd src
```

Activa el entorno virtual para cargar las dependencias de Python:

```
venv\Scripts\activate
```

Indica desde dónde iniciará el servidor web:

* ##### Línea de comandos (cmd, Command prompt)
```
> set FLASK_APP=main.py
```

* ##### Powershell
```
PS > $env:FLASK_APP="main.py"
```

Ejecuta el servidor:

* ##### Sólo máquina local
```
flask run
```

* ##### Para acceder al servidor a través de un dispositivo que no sea el equipo local:
```
flask run --host=0.0.0.0
```
