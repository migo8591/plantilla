from index import customers, Customer
def enterCustomerData():
    starting = True
    while starting:
        while True:
            nameCustomer = input("Introduce el nombre del cliente: ")
            if nameCustomer =="":
                print("El nombre no puede estar vacio")
            elif nameCustomer != "":
                break
        starting_email = True
        while starting_email:
            emailCustomer = input("Introduce el email del cliente: ")
            if emailCustomer =="":
                print("El email no puede estar vacio")
                confirm_email = input("¿Desea continuar? (S/N): ")
                if confirm_email.lower() == "n":
                    break
            elif emailCustomer != "":
                break
        new_customer = Customer.get_customer(emailCustomer)
        if new_customer is not None:
            print("El cliente ya existe.")
        else:
            starting = False
            while True:
                phoneCustomer = input("Introduce el telefono del cliente: ")
                if phoneCustomer =="":
                    print("El phone no puede estar vacio")
                elif phoneCustomer != "":
                    break
            while True:
                addressCustomer = input("Introduce la dirección del cliente: ")
                if addressCustomer =="":
                    print("La dirección no puede estar vacio")
                elif addressCustomer != "":
                    break
            is_credito = input("¿Es cliente de credito? (S/N): ")
            is_credito = is_credito.lower()
            # print(is_credito)   
            def customerCredit(credito):
                enter = True
                while enter:
                    if credito == "s" or credito == "n":
                        if credito == "s":
                            a_credito = True
                        else:
                            a_credito = False
                        enter = False
                    else:
                        credito = input("¿Es cliente de credito2? (S/N): ")   
                        # print(credito)
                    is_credito = credito
                # print(enter)
                print("Cliente nuevo: ",nameCustomer, phoneCustomer, emailCustomer, addressCustomer, is_credito, a_credito)
                return a_credito
            customerCredit(is_credito)
            a_credito = customerCredit(is_credito)
            new_customer = Customer(len(customers)+1, nameCustomer, phoneCustomer, emailCustomer, addressCustomer, a_credito)
            new_customer.save()
            print("Cliente agregado correctamente.")
enter = True
while enter:
    enterData = input("Do you want to add a new customer? (1/0): ")
    if enterData not in ['1','0']:
        print('Please enter 1 for "Yes" or 0 to "No".')
        continue
    enterData = int(enterData)
    try:
        if enterData == 1:
            enterCustomerData()
        else:
            print("Good bye!")
            break
    except ValueError:
        print("Invalid input. Please enter 1 or 0.")    

for customer in customers:
    print(customer.id, customer.name, customer.phone, customer.email, customer.address, customer.a_credito)



        
# while is_credito in ['S','N']:
#     if is_credito == 'S':
#         credito = True
#     else:
#         credito = False
# else:
#     is_credito = input("¿Es cliente de credito? (S/N): ")