# Creando formularios:

1. Crear una ruta para mostrar el formulario con los methods = ['GET', 'POST]
2. En el html al agregar el atributo action e indicar la URL en donde se enviarán los datos del formulario, si se deja vacío será la misma URL desde la que se descargo el recurso. Y en el atributo method = "POST"
2. En el form del html incluir un nombre a cada campo del formulario.
3. A la ruta agregar los nombre del formulario con el objeto request del módulo flask
4. Instalar las extensiones Flask-WTF: pip install Flask-WTF y
pip install email-validator
5. Crear un file para crear una clase y utilizando componentes de la extensión Flask-WTF.
6. A la ruta correspondiente se debe importar e instarciar la clase, luego actualizar la vista correspondiente Flask sabrá como hacerlo por medio de  {{ form.xxx.label }} 
7. Agregar la "Secret_key"
8. Para la captura de los datos se hace uso del método validate_on_submit() y ya no se usara request sin form.name.data

[Volver al Indice](index.md)