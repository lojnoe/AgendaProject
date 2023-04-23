import pymongo

class Agenda:
    def __init__(self,cliente,nombre_bd,nombre_collection):
        self.cliente = cliente
        self.db = cliente[nombre_bd]
        self.collection = self.db[nombre_collection]

    def insertar_contacto(self,nombre,apellido,email,telefono):
        collection = self.collection
        collection.insert_one({
            'nombre':nombre,
            'apellido':apellido,
            'email':email,
            'telefono':telefono
        })
        result = collection.find_one({'nombre':nombre,'apellido':apellido,'email':email,'telefono':telefono})
        return result
    def buscar(self,telefono):
        collection = self.collection
        result = collection.find_one({'telefono':telefono})
        return result
    def eliminar_contacto(self,nombre,apellido): 
        collection = self.collection
        collection.delete_one({'nombre':nombre,'apellido':apellido})
    def actualizar_contacto(self,email,telefono):
        collection = self.collection
        collection.update_one({'telefono':telefono},{'$set':{'email':email,'telefono':telefono}})
    def visionado_contacto(self,result):
        collection = self.collection
        print("-------RESULTADO------")
        print("Nombre: ",result['nombre'])
        print("Apellido: ",result['apellido'])
        print("Email: ",result['email'])
        print("Telefono: ",result['telefono'])
        print("-----------------------")



cliente = pymongo.MongoClient("mongodb://localhost:27017/")
agenda = Agenda(cliente, 'Agenda', 'Contactos')
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
        break
    
