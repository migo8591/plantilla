# Instalando una base de datos:

0. Instalación de SQLAlchemy con sqlite: https://flask-sqlalchemy.readthedocs.io/en/3.1.x/quickstart/
SQLAlchemy documentation: https://docs.sqlalchemy.org/en/14/index.html
flask 2x: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

1. repositorio: https://github.com/PyMySQL/mysqlclient?tab=readme-ov-file
2. instalar: $ pip install mysqlclient
3. app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:pl4n3TaJupiter@localhost/blogCuatro"

---

1. pip install - U Flask-SQLAlchemy
2. Crear un archivo: extensions.py e importar SQLALchemy e instanciarlo.
    ~~~
        from flask_sqlalchemy import SQLAlchemy
        db = SQLAlchemy()
    ~~~
3. Configure the SQLite database, relative to the app instance folder:
    ~~~
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    ~~~
4.  Importar e initialize the app with the extension al file __init__.py
    ~~~
    db.init_app(app)
    ~~~
5. Crear un archivo models.py de la misma jerarquia de entrypoint.py para definer los models
6. Create the tables:
    ~~~
    with app.app_context():
    db.create_all()
    ~~~
7. Save the information:
***
### Para consultar desde CLI con SQLite3

1. Localiza la base de datos:

Asegúrate de que tu base de datos SQLite se encuentra en el directorio <code>instance</code>. Por ejemplo, si el archivo de la base de datos se llama app.db, su ruta será algo como:
<code>
    flask_project/instance/app.db
</code>

2. Accede al directorio del proyecto:

Navega hasta el directorio base de tu proyecto Flask en la terminal. Este es el directorio donde ejecutas tu aplicación Flask (por ejemplo, donde se encuentra run.py).
<code>
    cd path/a/flask_project
</code>
<br>
3. Abre SQLite desde la consola:

Una vez abierto, verás el prompt de SQLite (sqlite>), donde puedes ejecutar consultas SQL directamente:
<code>
    sqlite> .tables
    sqlite> SELECT * FROM users;
    sqlite> .exit
</code>

### Utilizando .mode
1. .mode table (tambien se puede:.mode table .width10 )
2. headers on
3. SELECT * FROM blog_user;
<img src="img/table.png" width="800" height="150" margin="50 50"/>

## Instalando MySQL:
1. repositorio: https://github.com/PyMySQL/mysqlclient?tab=readme-ov-file
2. instalar: $ pip install mysqlclient
3. app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:pl4n3TaJupiter@localhost/blogCuatro"

### Utilizando MySQL desde CMD: 
1. Abrir CMD
2. Ir al explorador de archivo para buscar la ruta donde se esta ejecutando MySQL:
C/archivosDePrograma/MySQL/MySQLServer8.0/bin/ (copiar toda esta ruta)
3. Volver a la CMD: cd path
4. mysql -uroot -p (-u: usuario, -p: password)
5. Para ver todas las bases de datos: <br>
SHOW DATABASES;
6. Para crear una base: <br>
CREATE DATABASE xxx;
7. Para utilizar la base creada: <br>
USE xxx;
8. Para ver las tablas que tiene disponible xxx:<br>
SHOW TABLES;
9. Para crear una tabla:<br>
CREATE TABLE user(id, nombre varchar(120), description text);
10. Para ver los datos que tiene la tabla:
SELECT * from user;<br>
Otra opción: SELECT * FROM nombre_tabla\G
11. 
12. 
13. 
14. exit;




### Variable de entorno para MySQL:




* Tomado desde LinkedIn_MySQL_esencial: <br>
https://unedcr-my.sharepoint.com/personal/miguel_munoz_uned_cr/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmiguel%5Fmunoz%5Funed%5Fcr%2FDocuments%2F1%2Fvideos%5FLinkedIn%5FDev%2Fothers%5FCourse%2FCourse%5FLinkedIn%2FLinkedIn%5FMySQL%5Fesencial%2F1%2D2%2D3MySQL%20%5Fesencial%5F1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Efbf55147%2D9c44%2D4173%2Db5d0%2D41605fc2c395



[Volver al Indice](index.md)