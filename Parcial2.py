class Paciente:
    def __init__(self,identificacion, nombre, edad, diagnostico,sintomas):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        self.sintomas=sintomas
        self.diagnostico = diagnostico
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.identificacion} - {self.nombre} - {self.edad} - {self.diagnostico} - {self.sintomas}"

class CentroSalud:
    def __init__(self):
        self.primero = None                  
        self.ultimo = None                   
        self.cantidad = 0                    
        self.bebes = 0                       
        self.primeraInfancia = 0            
        self.ninos = 0                       
        self.adolescentes = 0                
        self.adultos = 0                    
        self.adultosMayores = 0             
        self.ultimos_nodiagnosticados = []   

    
    def actGruposEdad(self, edad, incremento):
        if edad >= 0 and edad <= 2:
            self.bebes += incremento
        elif edad >= 3 and edad <= 5:
            self.primeraInfancia += incremento
        elif edad >= 6 and edad <= 11:
            self.ninos += incremento
        elif edad >= 12 and edad <= 17:
            self.adolescentes += incremento
        elif edad >= 18 and edad <= 50:
            self.adultos += incremento
        else:
            self.adultosMayores += incremento
    
    
    def registrar_paciente(self, identificacion, nombre, edad, diagnostico , sintomas):
        
        
        if self.buscar_paciente(identificacion) is not None:
            print("número de identificación existente. No se puede registrar al paciente. Rectifique y Reintente Nuevamente.")
            return
        
        nuevo = Paciente(identificacion, nombre, edad, diagnostico , sintomas)
        
        
        if diagnostico == "":
            self.ultimos_nodiagnosticados.append(nuevo)
        if len(self.ultimos_nodiagnosticados) > 7:
            self.ultimos_nodiagnosticados.pop(0)
        
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.primero.siguiente = self.ultimo
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
            self.ultimo.anterior = self.primero
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.ultimo = nuevo
        self.cantidad += 1
        self.actGruposEdad(edad, 1)

    
    def eliminar_paciente(self, identificacion):
        actual = self.primero
        encontrado = False
        for _ in range(self.cantidad):
            if actual.identificacion == identificacion:
                encontrado = True
                break
            actual = actual.siguiente

        if encontrado:
            if self.cantidad == 1:
                self.primero = None
                self.ultimo = None
            elif actual == self.primero:
                self.primero = self.primero.siguiente
                self.primero.anterior = self.ultimo
                self.ultimo.siguiente = self.primero
            elif actual == self.ultimo:
                self.ultimo = self.ultimo.anterior
                self.ultimo.siguiente = self.primero
                self.primero.anterior = self.ultimo
            else:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior

            self.cantidad -= 1
            self.actGruposEdad(actual.edad, -1)
            return True
        else:
            return False
    
    
    def mostrar_pacientes(self):
        actual = self.primero
        for _ in range(self.cantidad):
            print(actual)
            actual = actual.siguiente

    
    def mostrar_pacientes_edades(self):
        print(f"Bebes: {self.bebes}")
        print(f"Primera Infancia: {self.primeraInfancia}")
        print(f"Niños: {self.ninos}")
        print(f"Adolescentes: {self.adolescentes}")
        print(f"Adultos: {self.adultos}")
        print(f"Adultos Mayores: {self.adultosMayores}")
        

   
    def buscar_paciente(self, identificacion):
        actual = self.primero
        for _ in range(self.cantidad):
            if actual.identificacion == identificacion:
                return actual
            actual = actual.siguiente
        return None

    def mostrar_pacientes_diagnosticados(self, diagnostico):
        actual = self.primero
        for _ in range(self.cantidad):
            if actual.diagnostico == diagnostico:
                print(actual)
            actual = actual.siguiente
    
    def mostrar_pacientes_nodiagnosticados(self):
        if len(self.ultimos_nodiagnosticados) == 0:
            print("No se han encontrado pacientes sin diagnosticar")
        else:
            count = min(len(self.ultimos_nodiagnosticados), 7)
            ultimosNodiagnosticados = self.ultimos_nodiagnosticados[-count:]
        for paciente in ultimosNodiagnosticados:
            print(paciente)

centro = CentroSalud()

while True:
    print("1. Registrar paciente")
    print("2. Eliminar paciente")
    print("3. Buscar paciente")
    print("4. Mostrar  los pacientes")
    print("5. Mostrar pacientes por clasificacion de edad")
    print("6. Mostrar pacientes por diagnostico")
    print("7. Mostrar ultimos pacientes no diagnosticados")
    print("0. Salir")
    
    opcion = int(input("Ingrese la opción que desea utilizar: "))
    
    if opcion == 1:
        identificacion = input("Ingrese el numero de identificacion del paciente: ")
        nombre = input("Ingrese el nombre completo del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        sintomas = input("Ingrese los sintomas que presenta el paciente: ")
        diagnostico = input("Ingrese el diagnostico del paciente, si no esta diagnosticado, presione enter: ")
        centro.registrar_paciente(identificacion, nombre, edad, diagnostico,sintomas)
        
    elif opcion == 2:
        identificacion = input("Ingrese el numero de identificacion del paciente que quiere eliminar: ")
        if centro.eliminar_paciente(identificacion):
            print("Paciente eliminado.")
        else:
            print("El paciente no fue encontrado, rectifique  que el numero de identificacion sea correcto.")
            
    elif opcion == 3:
        identificacion = input("Ingrese el numero de identificacion del paciente que quiere buscar: ")
        paciente_encontrado = centro.buscar_paciente(identificacion)
        if paciente_encontrado:
            print("Paciente encontrado:")
            print(f"Identificación: {paciente_encontrado.identificacion}")
            print(f"Nombre: {paciente_encontrado.nombre}")
            print(f"Edad: {paciente_encontrado.edad}")
            print(f"Sintomas: {paciente_encontrado.sintomas}")
            print(f"Diagnóstico: {paciente_encontrado.diagnostico}")
            
        else:
            print("Paciente no encontrado. Rectifique la informacion y vuelva a intentarlo")
            
    elif opcion == 4:
        centro.mostrar_pacientes()
        
    elif opcion == 5:
        centro.mostrar_pacientes_edades()
        
    elif opcion == 6:
        diagnostico = input("Ingrese el diagnóstico medico que desea buscar: ")
        centro.mostrar_pacientes_diagnosticados(diagnostico)
        
    elif opcion == 7:
        centro.mostrar_pacientes_nodiagnosticados()
        
    elif opcion == 0:
        break
        
    else:
        print("La opcion no es valida. Rectifique la informacion y vuelva a intentarlo.")
        
        centro = CentroSalud()



    
        

   
            


    







    
    

        


