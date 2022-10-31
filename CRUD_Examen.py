#Planetas de star wars
planetas = {
    "Bespin" : {
        "Localización"  : "Borde exterior",
        "Población"     : 6000000,
        "Residente"    : ["Humanos","Ugnaughts"],
        "Lengua"        :["Básico Galáctico Estándar"]
    },
    "Coruscant" : {
        "Localización"  : "Mundos del Núcleo",
        "Población"     : 1000000000,
        "Residente"    : ["Humanos", "Taung - extinta", "Varios"],
        "Lengua"        :["Básico Galáctico Estándar"]
    },
    "Endor" : {
        "Localización"  : "Borde exterior",
        "Población"     : 30000000,
        "Residente"     : ["Ewoks","Sanyassan","Gorax","Yuzzums","Teeks"],
        "Lengua"        : ["Ewokés","Goraxés","Yuzzumés"]
    },
    "Mandalore" : {
        "Localización"  : "Borde Exterior",
        "Población"     : 4000000,
        "Residente"     : ["Mandaloriana","Taungs","Humanos"],
        "Lengua"        : ["Mando'a ","Básico Galáctico Estándar"]
    }
}

def menu():
    return int(input("""
    ======= Registro de los planetas conocidos de la galaxia =======
    ======= 1.Registrar planeta
    ======= 2.Modificar planeta
    ======= 3.Información sobre planeta
    ======= 4.Eliminar planeta
    ======= 5.Salir del registro de planeta
    Opcion:"""))

def menuModificar():
    return int(input("""
    ======= Opciones de modificación =======
    ======= 1.Localización 
    ======= 2.Población
    ======= 3.Residente
    ======= 4.Lenguaje
    ======= 5.Salir
    Opcion:"""))

def menuVer():
    return int(input("""
    ======= Opciones de modificación =======
    ======= 1.Ver todos los planetas
    ======= 2.Ver planeta en especifico
    ======= 3.Salir
    Opcion:"""))

def planetasExistente(planeta):

    return planeta in planetas.keys()

def ingresarPlaneta(planeta):
    
    if not planetasExistente(planeta):   
        
        localizacion = str(input("Ingresar la localización:"))
        #planetas[planeta]["Localización"] = localizacion 

        poblacion = int(input("Ingrese la cantidad de población:"))
        #planetas[planeta]["Población"]      = poblacion

        listadeResidente = []

        while True:
            raza = str(input("Ingresar residente:"))
            listadeResidente.append(raza)

            salir = input("Ingresar otra raza (S/N):")

            if salir.lower() == "n":
                break 
            #planetas[planeta]["Residente"] = listadeResidente

        listadeIdioma = []

        while True:
            idioma = str(input("Ingresar idioma:"))
            listadeIdioma.append(idioma)

            salir = input("Ingresar otro idioma (S/N):")
            if salir.lower() == "n":
                break
            #planetas[planeta]["Lengua"] = listadeIdioma

        planetas[planeta] = {
            "Localización"  : localizacion,
            "Población"    : poblacion,
            "Residente"    : listadeResidente,
            "Lengua"        : listadeIdioma
        }

        print("=========== Planeta registrado con exito ===========")

    else:

        print("=========== Planeta ya fue registrado ===========")

def modificarPlaneta(planeta):

    if planetasExistente(planeta):   
        op = menuModificar()

        while op != 5 :
            
            if op == 1:
                localizacion = str(input("Ingresar la  nueva localización:"))
                planetas[planeta]["Localización"] = localizacion 
                print("Dato actualizado")

            if op == 2:
                poblacion = int(input("Ingrese la nueva cantidad de población:"))
                planetas[planeta]["Población"]      = poblacion
                print("Dato actualizado")

            if op == 3:
                
                listadeResidente = []

                while True:
                    raza = str(input("Ingresar nuevos residente:"))
                    listadeResidente.append(raza)

                    salir = input("Ingresar otra raza (S/N):")

                    if salir.lower() == "n":
                        break 
                    
                    planetas[planeta]["Residente"] = listadeResidente
                    print("Dato actualizado")
            if op == 4:
                
                listadeIdioma = []
                while True:
                    idioma = str(input("Ingresar idioma:"))
                    listadeIdioma.append(idioma)

                    salir = input("Ingresar otro idioma (S/N):")
                    if salir.lower() == "n":
                        break
                planetas[planeta]["Lengua"] = listadeIdioma 
                print("Dato actualizado")
            
            op = menuModificar()

        print("=========== Planeta modificado con exito ===========")


    else:

        print("=========== Planeta no exite en los registros galácticos ===========")

def eliminarPlaneta(planeta):

    if planetasExistente(planeta):   
        planetas.pop(planeta)
        print("=========== Planeta eliminado por la estreña de la muerte ===========")
    else:
        print("=========== Planeta no exite en los registros galácticos ===========")

def verPlaneta():

    op = menuVer()

    while op !=3:
        
        if op == 1:
            #print("{}".format(planetas["Bespin"]["Lengua"]))
            print("=========== Catalogo de los planetas conocidos de la galaxia")
            for planeta in planetas.keys():
                #print("{}".format(planetas[planeta]["Lengua"]))
                print("\tPlaneta: {}\n \tLocalización: {} \n \tPoblacioó: {} \n \tResidente: {} \n \tLengua: {} \n". format(planeta,planetas[planeta]["Localización"],planetas[planeta]["Población"], planetas[planeta]["Residente"] ,planetas[planeta]["Lengua"]))                

        if op == 2:
            planeta = str(input("Ingresar el nombre del planeta:").capitalize())
            print("\tPlaneta: {} \n \tLocalización: {} \n \tPoblacioó: {} \n \tResidente: {} \n \tLengua: {} \n".format(planeta,planetas[planeta]["Localización"],planetas[planeta]["Población"],planetas[planeta]["Residente"],planetas[planeta]["Lengua"]))
        op = menuVer()

opcion = menu()

while opcion != 5:

    if opcion == 1:
       planeta = str(input("Ingresar el nuevo planeta:"))
       ingresarPlaneta(planeta.capitalize())

    if opcion == 2:

        planeta = str(input("Ingresar el nombre del planeta a modificar:"))
        modificarPlaneta(planeta.capitalize())

    if opcion == 3:
        verPlaneta()

    if opcion == 4:
        
        planeta = str(input("Ingresar el nombre del planeta a eliminar:"))
        eliminarPlaneta(planeta.capitalize())

    opcion = menu()

print("\t=========== Programa finalizado ===========")