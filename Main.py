#Hoja de Trabajo 10
#Juan Diego Solorzano 18151
#Andrea Paniagua

from py2neo import *
from py2neo.ogm import *


db = Graph(password="1234")

opcion = 0
print("Bienvenido a Hoja de Trabajo 10 \n")
while opcion != "7":
    opcion = input("Eliga una opcion: \n"
          "1. Ingresar un Doctor \n"
          "2. Ingresar un Paciente \n"
          "3. Ingresar una visita \n"
          "4. Consultar Doctores por especialidad \n"
          "5. Crear una relacion entre dos personas \n"
          "6. Sugerencia simple desde paciente \n"
          "7. Salir \n")
    
    if opcion == "1":
        #Crea un doctor con sus datos
        nombre = input("Ingrese el nombre del doctor")
        especialidad = input("Ingrese la especialidad del doctor")
        contacto = input("Ingrese numero de telefono del doctor")

        db.run("CREATE (d:Doctor {name:'"+nombre+"', specialty:'"+especialidad+"', contact:'"+contacto+"'})")

        
    elif opcion == "2":
        #Crea un paciente con sus datos
        nombre = input("Ingrese el nombre del paciente")
        contacto = input("Ingrese numero de telefono del paciente")

        db.run("CREATE (p:Patient {name:'"+nombre+"', contact:'"+contacto+"'})")

        
    elif opcion == "3":
        #Crea una visita con sus datos
        nomPac = input("Ingrese el paciente al tratar")
        nomDoc = input("Ingrese el nombre del doctor que visita")
        fecha = input("Ingrese la fecha de la visita (MM/DD/YY)")
        medicina = input("Ingrese el nombre de la medicina que le receto")

        db.run("MATCH (p:Patient),(d:Doctor),(m:Medicine) WHERE p.name = '"+nomPac+"' AND d.name = '"+nomDoc+"' AND m.name = '"+medicina+"' CREATE (p)-[r:VISITS{date: '"+ fecha +"'}]->(d) -> [r:PRESCRIBE] -> (m) -> [r: TAKES] -> (p) ")
        
        
        
    elif opcion == "4":
        #Busca doctores por especialidad
        esp = input("Ingrese la especialidad que busca")
        nomb = db.run("MACTH (d:Doctor) WHERE d.specialty = '"+esp+"' return d.name")
        contac = db.run("MACTH (d:Doctor) WHERE d.specialty = '"+esp+"' return d.contact")
        print("Resultados: \n"
              "Nombre: " + nomb + "\n"
              "Contacto: " + contac + "\n")
        
        
    elif opcion == "5":
        #Crea una relacion entre dos personas
        opc = input("Desea crear una relacion entre: \n"
                    "1. Doctores \n"
                    "2. Pacientes \n"
                    )
        if opc == "1":
            
            d1 = input("Ingrese el nombre del primer doctor")
            d2 = input("Ingrese el nombre del segundo doctor")
            db.run("MATCH (doc1:Doctor),(doc2:Doctor) WHERE doc1.name = '"+d1+"' AND doc2.name = '"+d2+"'CREATE (doc1)<-[r:KNOWS]->(doc2)")
            
        elif opc == "2":
            
            p1 = input("Ingrese el nombre del primer paciente")
            p2 = input("Ingrese el nombre del segundo paciente")
            db.run("MATCH (pac1:Patient),(pac2:Patient) WHERE pac1.name = '"+p1+"' AND pac2.name = '"+p2+"'CREATE (pac1)<-[r:KNOWS]->(pac2)")


    elif opcion == "6":
        #Busca doctores por especialidad
        nom = input("Ingrese el nombre paciente")
        esp = input("Ingrese la especialidad que busca")
        doctorVisitado = db.run("MACTH (p:Patient)-[r:VISITS]->(d:Doctor) WHERE p.name = '"+nom+"' AND d.specialty = '"+esp+"' return d.name")
        

        
        print("Has Visitado: \n"
              "Nombre: " + nomb + "\n"
              "Contacto: " + contac + "\n")
print("Gracias por utilizar el programa!")
        
        
