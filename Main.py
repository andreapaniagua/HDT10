#Hoja de Trabajo 10
#Juan Diego Solorzano 18151
#Andrea Paniagua

from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")

pacientes = Hospital.labels.create("Pacientes")

doctores = Hospital.labels.create("Doctores")

medicina = Hospital.labels.create("Medicina")


opcion = 0

print("Bienvenido a Hoja de Trabajo 10 \n")
while opcion != "6":
    opcion = input("Eliga una opcion: \n
          "1. Ingresar un Doctor \n
          "2. Ingresar un Paciente \n
          "3. Ingresar una visita \n
          "4. Consultar Doctores por especialidad \n
          "5. Crear una relacion entre dos personas \n
          "6. Salir \n")
    
    if opcion == "1":
        #Crea un doctor con sus datos
        nombre = input("Ingrese el nombre del doctor")
        especialidad = input("Ingrese la especialidad del doctor")
        contacto = input("Ingrese numero de telefono del doctor")
        
        doc = Hospital.nodes.create(name=nombre, specialty=especialidad, contact=contacto)
        doctores.add(doc)
        
    else if opcion == "2":
        #Crea un paciente con sus datos
        nombre = input("Ingrese el nombre del paciente")
        contacto = input("Ingrese numero de telefono del paciente")

        pac = Hospital.nodes.create(name=nombre, contact=contacto)
        pacientes.add(pac)
        
    else if opcion == "3":
        #Crea una visita con sus datos
        fecha = input("Ingrese la fecha de la visita (MM/DD/YY)")
        doctor = input("Ingrese el nombre del doctor que visita")
        if specialty == especialidad1:
            receta = medicina1
        else if specialty == especialidad2:
            receta = medicina2
        
    else if opcion == "4":
        #Busca doctores por especialidad
        esp = input("Ingrese la especialidad que busca")
        
    else if opcion == "5":
        #Crea una relacion entre dos personas
        opc = input("Desea crear una relacion entre: \n
                    "1. Doctores \n
                    "2. Pacientes \n
                    )
        if opc == "1":
            
            d1 = input("Ingrese el nombre del primer doctor")
            d2 = input("Ingrese el nombre del segundo doctor")
            d1.relationships.create("Conoce", d2)
            d2.relationships.create("Conoce", d1)
        else if opc == "2":
            
            p1 = input("Ingrese el nombre del primer paciente")
            p2 = input("Ingrese el nombre del segundo paciente")
            p1.relationships.create("Conoce", p2)
            p2.relationships.create("Conoce", p1)

        
print("Gracias por utilizar el programa!")
        
        
