# Login de usuarios:

1. Crear la clase para el formulario de login.
2. Crear la plantilla HTML para el formulario.
3. Actualizar la route para el login:
    1. Incorporar los methodos = ['GET','POST'].
    2. Implementar primero el GET.
    2. Redirrecionar si el usuario esta authenticado.
    3. Importar e utilizar la class LoginForm.
    4. Utilizar if form.validate_on_submit():
    5. Consiguir el correo. 
    6. Checkear las credenciales
    6. Utilizar user en login_user()
    7. Utilizar el arg "next"


<code>
@auth_bp.route('/login', methods=['GET', 'POST'])
def login(): 
    # Se comprueba si el usuario ya está autenticado:
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Correo {form.email.data} Contraseña {form.password.data}")
        user = User.get_by_email(form.email.data)
        print(user)
        # Si existe un con dicho email y la contraseña coincide se procede a autenticar al usuario llamando al método login_user
        if user is not None and user.check_password(form.password.data):
            #  ↑ Si las credenciales son correctas, se inicia sesión para el usuario. El parámetro remember=form.remember_me.data indica si el usuario quiere que se recuerde su sesión (por ejemplo, mediante una cookie persistente).
            print("entro")
            print(f"user1: {user.correo}, password2: {user.contrasena}")
            login_user(user, remember=form.remember_me.data)
            #Por último comprobaremos si recibimos el parametro next. Esto sucedera cuando el usuario ha intentado acceder a una pagina protegida pero no esta autenticado. Por temas de seguridad solo tendremos en cuenta dicho parámetro si la ruta es relativa. 
            next_page = request.args.get('next')
            # ↑ El parámetro next indica a qué página debe redirigir el sistema una vez que el usuario haya iniciado sesión. Si un usuario intentaba acceder a una página que requiere autenticación (como /dashboard), se le redirigiría primero a la página de inicio de sesión con un parámetro next que contiene la URL de destino: http://localhost:5000/login?next=/dashboard
            # ↓ Si no se recibe el parámetro next o este no contiene una relativa redirigimos al usuario a la pagina de inicio 
            if not next_page or urlparse(next_page).netloc !='':
                # ↑ Si next_page tiene un netloc no vacio lo considera insegura y lo redireccionar a la pagina principal
                next_page = url_for('public.index')
            return redirect(next_page)
    return render_template('auth/login_form.html', form=form)

Acerca de las rutas relativas:
Una ruta relativa es aquella que no incluye el dominio completo. En este caso, la ruta '/login' es una ruta relativa porque solo define la dirección después de la raíz del servidor. Por ejemplo, si la aplicación se ejecuta en http://localhost:5000, entonces la URL completa sería http://localhost:5000/login.

Ejemplo con parámetro next:

Imagina que el usuario intenta acceder a /dashboard, pero no está autenticado. Flask lo redirigiría a la página de inicio de sesión con el parámetro next que indica a dónde debe ser redirigido después de iniciar sesión.

Por ejemplo, la URL a la que se le redirige sería:

http://localhost:5000/login?next=/dashboard

Si el usuario inicia sesión correctamente, será redirigido a /dashboard en lugar de ser enviado a la página principal.


Explicación de "url_parse(next_page).netloc !='' "


    # if not next_page or url_parse(next_page).netloc != '':

tiene una función importante para asegurar que el parámetro next_page sea una URL interna (dentro del mismo sitio web) y no una URL externa (de otro dominio). Vamos a desglosarlo:

Explicación de url_parse(next_page).netloc != '':
url_parse(next_page):

La función url_parse proviene de werkzeug.urls y sirve para descomponer una URL en sus componentes: esquema (http o https), dominio (netloc), ruta, parámetros, etc. Es similar a lo que hace la función urlparse en la biblioteca estándar de Python.

Por ejemplo, si next_page es "http://example.com/dashboard", url_parse(next_page) devuelve un objeto que contiene:

scheme: "http"
netloc: "example.com" (dominio)
path: "/dashboard"
url_parse(next_page).netloc:

El atributo netloc representa el dominio (y opcionalmente el puerto) de una URL. Si next_page es una URL externa (como "http://example.com/dashboard"), netloc será "example.com".

Si next_page es una URL relativa dentro de tu aplicación (por ejemplo, "/dashboard"), el netloc será una cadena vacía ('') porque no tiene dominio.

url_parse(next_page).netloc != '':

Esta condición se asegura de que el valor de netloc no esté vacío, lo que significa que next_page contiene un dominio externo. Si netloc != '', la URL sería externa, lo cual podría representar un problema de seguridad (por ejemplo, un ataque de redireccionamiento malicioso).

### Contexto de seguridad:

El propósito de este código es evitar redirecciones no seguras a dominios externos. Si next_page fuera una URL externa, el usuario podría ser redirigido a otro sitio web fuera de tu control, lo que abre la posibilidad a ataques como phishing o redireccionamientos maliciosos.

Por eso, si next_page tiene un netloc no vacío, el código lo considera inseguro y establece un valor por defecto:

python

Copy code

next_page = url_for('index')

Esto garantiza que, si alguien intentara redirigir al usuario a un sitio externo, tu aplicación lo devolvería de manera segura a la página de inicio.

#### Ejemplo práctico:

Si next_page es "/dashboard", el valor de netloc será '' porque no hay dominio. En este caso, la redirección es segura y el usuario será enviado a "/dashboard".

Si next_page es "http://example.com/dashboard", el valor de netloc será "example.com", lo que indica una URL externa. En este caso, la redirección se considerará insegura y el usuario será redirigido a la página de inicio (/index).

Esta condición es un control de seguridad crucial en aplicaciones web que manejan redirecciones basadas en parámetros.

https://chatgpt.com/share/66e5d4ea-02d0-800d-a6d5-42a1e0949e22

</code>

Por que en Python si la variable next_page = none su negación not next_page = True

ChatGPT said:
ChatGPT
En Python, la evaluación de valores en contextos de verdad se basa en si un objeto es considerado "falsy" o "truthy". Aquí está la explicación paso a paso para el caso que planteas:

Evaluación de None en contextos de verdad
En Python, None es considerado un valor "falsy". Es decir, en un contexto donde se evalúa la verdad de un valor (por ejemplo, en una declaración if), None se interpreta como False.
Negación de None con not
Cuando usas el operador not, inviertes la evaluación de verdad del valor.
Si next_page = None, entonces:
python
Copy code
not next_page
Evalúa como True, porque None es "falsy".
Ejemplo práctico
python
Copy code
next_page = None

if not next_page:
    print("next_page es falsy y su negación es True")
Este código imprimirá el mensaje porque not None equivale a True.

Por qué sucede esto
None es uno de los valores que Python trata como "falsy".
La negación de un valor "falsy" siempre da True.
Esto no aplica solo a None. Otros valores considerados "falsy" incluyen:

False
0 (cero)
0.0 (cero flotante)
"" (cadena vacía)
[] (lista vacía)
{} (diccionario vacío)
() (tupla vacía)
set() (conjunto vacío)
En resumen, si next_page es None, su negación (not next_page) será True porque None es un valor "falsy".

https://chatgpt.com/share/676f236a-9a8c-800d-84eb-e29e2dcea60d