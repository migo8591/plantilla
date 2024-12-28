# Leccion 8: Gestion y manejo de errores y excepciones:
<img src="img/zerrorError.jpg" width="300" height="300" margin="50 50"/>
Si desactivamos el modo <code>DEBUG</code> y volvemos a acceder a la página anterior, veremos que en esta ocasión se nos muestra una página de error genérica:
<img src="img/serverError.jpg" width="300" height="300" margin="50 50"/>

La función <code>abort()</code> detiene la ejecución de la petición de forma prematura y devuelve un código de estado HTTP permitido (el que le pasemos como parámetro).

Hay dos formas de definier un manejador de error:
* Decorando una función con <code>errorhandler</code>
* Registrando una función como errorhandler: <code>app.register_error_handler(codigo_estado, funcion)</code>

Se pueden manejas dos tipos de errores:
* Códigos de estado HTTP conocidos.
* Excepciones.
### Páginas de error personalizadas:
1. Abrir el fichero app/__init__.py y añadir el siguiente código:
~~~
    def register_error_handlers(app):

        @app.errorhandler(500)
        def base_error_handler(e):
            return render_template('500.html'), 500

        @app.errorhandler(404)
        def error_404_handler(e):
            return render_template('404.html'), 404
~~~
2. Añade también lo siguiente al final del método <code>create_app()</code>, justo antes del return app:
~~~
    # Custom error handlers
    register_error_handlers(app)
~~~
3. Crear los ficheros 404.html y 500.html en el directorio app/templates
