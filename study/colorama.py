# Primero, necesitas instalar colorama si aún no lo has hecho. Puedes hacerlo ejecutando:
# pip install colorama

# from colorama import Fore, Back, Style, init
from colorama import Fore as fore, init
# Inicializa colorama
init()

print(fore.RED + 'Este texto es rojo')
print(fore.GREEN + 'Este texto es verde')
# print(Back.YELLOW + 'Este texto tiene fondo amarillo')
# print(Style.BRIGHT + 'Este texto es brillante')

# Resetea el estilo
# print(Style.RESET_ALL + 'Este es el estilo predeterminado')

# print(fore.BLUE + 'Puedes combinar' + Style.BRIGHT + ' estilos y colores')
# print(Back.CYAN + 'de diferentes maneras.' + 
#       fore.RESET)

# En este ejemplo:

# Fore se usa para cambiar el color del texto.

# Back se usa para cambiar el color de fondo.

# Style se usa para cambiar el estilo del texto (como brillante o atenuado).

# init() inicializa colorama para que funcione correctamente en diferentes plataformas. Style.RESET_ALL se usa para restablecer todos los estilos a los valores predeterminados.

# ¡Diviértete coloreando tu texto en la consola! ¿Hay algo más en lo que pueda ayudarte?

