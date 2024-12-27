# Sign up de usuarios en flask

* How to authenticate users in flask with flask-login. 
https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/

## Flask - Login 0.7.0 documentation:
1. Install the extension with flask-login:<br>
pip install flask-login<br>
2. Create LoginManager():<br>
~~~
from flask_login import LoginManager
login_manager = LoginManager()
~~~


3. Once the actual application object has been created, you can configure it for login with:<br>
~~~
login_manager.init_app(app)
~~~


4. Use the next callback:

~~~
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
~~~


5. Crear un nuevo fichero llamado models.py en el directorio raiz del proyecto para crear el modelo user y añade la clase siguiente: 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash.<br>
Para guardar las contraseñas se utilizara un hash del password: se hace uso de la librería werkzeug.security.<br>
El método check_password comprueba si el hash del parámetro password coincide con el del usuario.

6. Cambios en la ruta signin:

7. Logout
~~~
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
~~~

8. Protegiendo las vistas:
~~~
@login_required
~~~
9. Mostrando la info del usuario logueado en las plantillas

[Volver al Indice](index.md)