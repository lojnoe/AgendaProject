class Agenda:
    def __init__(self):
        self.contactos=[]

    def insertar_contacto(self,nombre,apellido,email,telefono):
        self.contactos.append([nombre,apellido,email,telefono])
        
    def buscar(self,nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                print(contacto)
            else:
                print("Contacto no encontrado.")
                
       

    def eliminar_contacto(self,nombre,apellido): 
        for contacto in self.contactos:
            if contacto[0] == nombre and contacto[1] == apellido:
                self.contactos.remove(contacto)
                print("Contacto eliminado correctamente.")
            else:
                print("Contacto no encontrado.")

    def actualizar_contacto(self,nombre,apellido,email,telefono):
        for contacto in self.contactos:
            if contacto[0] == nombre and contacto[1] == apellido:
                contacto[2] = email
                contacto[3] = telefono
                print ("Contacto actualizado correctamente")

agenda = Agenda()
while True:
    print("------------------------")
    print("1. Buscar")
    print("2. Añadir")
    print("3. Borrar ")
    print("4. Actualizar")
    print("5. Salir")
    print("------------------------")
    opcion = int(input("Ingrese una opcion del 1 al 5: "))
    if opcion == 1:
        nombre = input("Ingrese nombre: ")
        agenda.buscar(nombre)
        
    elif opcion == 2:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        email = input("Ingrese email: ")
        telefono = input("Ingrese telefono: ")
        agenda.insertar_contacto(nombre,apellido,email,telefono)
        agenda.buscar(nombre)
    elif opcion == 3:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        agenda.eliminar_contacto(nombre,apellido)
        print("Contacto eliminado correctamente")
    elif opcion == 4:
        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ")
        telefono = input("Ingrese telefono: ")
        agenda.actualizar_contacto(nombre,apellido,email,telefono)
        agenda.buscar(nombre)
    elif opcion == 5:
        break
    
