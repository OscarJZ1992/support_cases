# support_cases_app_server

## Requisitos previos

1. **pip**: Versión `24.2` instalada.
2. **python**: Versión `3.12` instalada.

## Pasos para correr la API

### 1. Crear el entorno virtual

Cuando estés en el directorio raíz del proyecto, abre la consola y ejecuta el siguiente comando para crear el entorno virtual en donde correra la API:
```
python -m venv venv
```

### 2. Activar los scripts
1. En el directorio raíz del proyecto, ejecuta el siguiente comando:
```
venv\Scripts\activate
```

### 3. Instalar las dependencias
1. Instala las dependencias que están en el archivo requirements.txt con el siguiente comando: 
```
pip install -r requirements.txt
```

### 4. Instalar las dependencias manualmente (SOLO si no te funciona el paso 3)
Instala las siguientes dependencias de forma manual
```
pip install psycopg2
pip install fastapi
pip install invoke uvicorn
pip install fastapi-cors
``` 

### 5. Modificar los datos en el archivo setup.sh
Dirigete al archivo `setup.sh` y modifica los valores de las siguientes variables que tengas configurado en tu ORM con PostgreSQL y el nombre de base de datos que deseas asignar.
```
DB_USER
DB_PASSWORD
DB_NAME
```

### 6. Crear e inicializar la base de datos
Una vez completados los pasos anteriores, abre la consola en el directorio raíz del proyecto y ejecuta el siguiente comando para inicializar el proceso de creación de la base de datos:
```
setup.sh
```
**NOTA**
En este paso **5**, si estás en windows es recomendable abrir la consola de `git bash` ubicate en el root del proyecto y ejecutar el comando `./setup.sh`


### 7. Recomendaciones
1. Una vez creada la base de datos, verifica en un ORM que se creó la base de datos y tenga información.
2. Finalmente cuando hayas verificado que si creó la base de datos con las tablas e información, ubicate nuevamente desde tu terminal en el root del proyecto y ejecuta el siguiente comando:
`invoke run` para levantar el ***API***.