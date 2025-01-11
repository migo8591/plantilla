from colorama import Fore as fore, init
from colorama import Style
init()
# Escribe un programa que pida al usuario una contraseña y la valide. El programa debe seguir pidiendo la contraseña hasta que sea correcta.
pswd_real = "123456"
pswd_user = ""

while pswd_user != pswd_real:
    pswd_user = input("Introduce una contraseña: ")
    
    if pswd_user != pswd_real:
        print("Contraseña incorrecta")
print("Logre salir del bucle..")
      
print("Contraseña correcta")       

customers= []       
class Customer():
    def __init__(self,id,name,phone, email, address, a_credito=False):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.a_credito = a_credito
        
    def get_customer(correo):
        for customer in customers:
            if customer.email == correo:
                return customer
    def save(self):
        customers.append(self)       
    def __str__(self):
        return f"{self.id} {self.name} {self.phone} {self.email} {self.address} {self.is_credito}"


def print_nombre(nombre):
    print("El nombre ingresado es: "+fore.LIGHTYELLOW_EX+nombre+Style.RESET_ALL)
def print_hola(f):
    print(fore.GREEN+"Segundo print "+fore.RED+"Hola"+fore.RESET)
    f
name = input("Introduce tu nombre: ")
print_hola(print_nombre(name))
print("El resultado debe ser: "+ fore.RED + " Hola "+ Style.RESET_ALL+"Nombre ingresado: "+ fore.GREEN + str(name )+ Style.RESET_ALL)
from functools import wraps
def imprima_hola(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("Hola")
        return f(*args, **kwargs)
    return decorated_function
@imprima_hola
def imprima_nombre(nombre):
    print(nombre)
    
imprima_nombre(name)
print("Al decorador la función "+fore.CYAN+"print_nombre() "+fore.RESET+"con "+fore.CYAN+" @print_hola"+fore.RESET+", se ejecuta el código del decorador antes que el de la propia función")