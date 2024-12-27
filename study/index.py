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
    
