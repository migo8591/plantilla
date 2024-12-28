# Parametros de configuración de un proyecto Flask
(Leccion 7)

Básicamente, los parámetros de configuración de un proyecto nos permiten definir la cadena de conexión a la base de datos, la duración de la cookie de sesión o el idioma por defecto de la aplicación, entre otros. Normalmente, en lugar de escribirlos directamente en el código, se definen en unos ficheros independientes. Otra particularidad es que son accesibles en cualquier parte del código (como si fueran variables globales).

---
## Variables de entorno
1. Instalar el modulo: python-dotenv/ ->
pip install python-dotenv <br>
* Documentation: https://pypi.org/project/python-dotenv/
2. Crear el archivo .env y las variables necesarias.
3. Importar el modulo load_dotenv desde dotenv en el file config.py y llamar dicho modulo. <br>
"Esta  esta función lo que hace es que va a buscar el archivo .env y va a crear las variables que encuentre en el sistema, entonces... para poder leer estas variables se debe utilizar un módulo de py llamado os, por lo que lo importamos"
4. Crear una variable con el protocolo de MySQL 
5. import donde se requira utilizar las variable con el protocolo siempre importando desde config 


## Usando ficheros independiente, uno por entorno:
