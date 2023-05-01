class Agenda:
    def __init__(self):
        self.contactos=[]

    def insertar_contacto(self,nombre,apellido,email,telefono):
        self.contactos.append(nombre,apellido,email,telefono)
        return result
    def buscar(self,telefono):
        for contacto in self.contactos:
            if contacto['telefono'] == telefono:
                return contacto
        return None

    def eliminar_contacto(self,nombre,apellido): 
        for contacto in self.contactos:
            if contacto['nombre'] == nombre and contacto['apellido'] == apellido:
                self.contactos.remove(contacto)
                return True
        return False
    def actualizar_contacto(self,email,telefono):
        for contacto in self.contactos:
            if contacto['email'] == email and contacto['telefono'] == telefono:
                self.contactos[self.contactos.index(contacto)] = {'nombre':nombre,'apellido':apellido,'email':email,'telefono':telefono}
                return True
        return False
        
    def visionado_contacto(self):
        for contacto in self.contactos:
            if contacto['estado'] == 'visionado':
                print("Nombre: ",contacto['nombre'])
                print("Apellido: ",contacto['apellido'])
                print("Email: ",contacto['email'])
                print("Telefono: ",contacto['telefono'])
                print("-----------------------")
                return True
        return False
    

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
        telefono = input("Ingrese telefono: ")
        result = agenda.buscar(telefono)
        if result:
           agenda.visionado_contacto(result)
           print("Contacto encontrado")
        else:
            print("Contacto no encontrado")
    elif opcion == 2:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        email = input("Ingrese email: ")
        telefono = input("Ingrese telefono: ")
        result = agenda.insertar_contacto(nombre,apellido,email,telefono)
        if result:
            agenda.visionado_contacto(result)
            
            print("Contacto  añadido correctamente")
        else:
            print("Contacto no añadido correctamente")
    elif opcion == 3:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        agenda.eliminar_contacto(nombre,apellido)
        print("Contacto eliminado correctamente")
    elif opcion == 4:
        telefono = input("Ingrese telefono: ")
        result=agenda.buscar(telefono)
        agenda.visionado_contacto(result)
        respuesta = input("��Desea actualizar el contacto? (S/N): ")
        if respuesta == "S" or "s":
            email = input("Ingrese email: ")
            telefono = input("Ingrese telefono: ")
            agenda.actualizar_contacto(email,telefono)
            print("Contacto actualizado")
        else:
            print("Contacto no actualizado")
    elif opcion == 5:
        print(contactos)
        break
    
