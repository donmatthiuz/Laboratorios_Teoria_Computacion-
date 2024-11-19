import os
from graphviz import Digraph
class TM:

    def __init__(self,  lector):
        self.estados = lector.estados
        self.alfabetoEntrada = lector.alfabeto
        self.alfabetoCinta = lector.tape_alphabet
        self.q0 = lector.q0
        self.aceptacion = lector.aceptacion
        self.transiciones = lector.transiciones
        self.size_cinta = 8
        self.cinta = []
        self.posCabezal = 0
        self.historial = []

    def validar_Cadena(self, cadena):
        """Valida si la cadena pertenece al alfabeto de entrada de la máquina."""
        return all(symbol in self.alfabetoCinta for symbol in cadena)

    def Comprobar_Transiciones(self):
        """Valida si las transiciones cumplen con el alfabeto de la cinta y estados definidos."""
        for estado, trans in self.transiciones.items():
            if estado not in self.estados:
                return False
            for simbolo, (siguiente_estado,cache_escrita, simbolo_escrito, _) in trans.items():
                if simbolo[0] not in self.alfabetoCinta or simbolo[1] not in self.alfabetoCinta or simbolo_escrito not in self.alfabetoCinta or siguiente_estado not in self.estados:
                    return False
        return True
    

    def simulate(self, cadena, cintaConfiguration=[], positionCabezal=0):
        if not self.validar_Cadena(cadena):
            return "Error: Cadena contiene símbolos fuera del alfabeto de entrada.", []
        if not self.Comprobar_Transiciones():
            return "Error: Las transiciones son inválidas.", []
        
        result = ""
        estado_actual = self.q0
        cache_actual = None
        self.historial = []  # Reiniciar historial en cada simulación
        isReject = False  # Flag para controlar el rechazo

        # Usar la configuración de la cinta si se proporciona, de lo contrario, usa la cadena
        self.cinta = cintaConfiguration if cintaConfiguration else list(cadena) + [None] * (self.size_cinta - len(cadena))

        # Asignar la posición del cabezal dependiendo de si se pasó una configuración de la cinta
        self.posCabezal = positionCabezal if cintaConfiguration else 0

        while not isReject and (estado_actual != self.aceptacion):
            simbolo_actual = self.cinta[self.posCabezal]

            # Formatear la cinta con el estado y el símbolo en la posición del cabezal
            cinta_formateada = (
                ''.join([str(item) if item is not None else 'B' for item in self.cinta[:self.posCabezal]]) +
                f"[{estado_actual}, {cache_actual if cache_actual is not None else "B"}]"+
                f"{simbolo_actual if simbolo_actual is not None else 'B'}"+
                ''.join([str(item) if item is not None else 'B' for item in self.cinta[self.posCabezal + 1:]])
            )
            self.historial.append(f"|- {cinta_formateada}")
        
            # Detectar rechazo verificando si la transición no existe
            if (cache_actual,simbolo_actual) not in self.transiciones.get(estado_actual, {}):
                result = "rechazo"
                self.historial.append(f"|- [{estado_actual}] - No tiene transición para [{simbolo_actual}], la cadena se rechaza")
                isReject = True
                continue

            # Obtener la transición y actualizar la cinta, estado y cabezal
            siguiente_estado, cache_siguiente, simbolo_escrito, direccion = self.transiciones[estado_actual][(cache_actual,simbolo_actual)]
            self.cinta[self.posCabezal] = simbolo_escrito
            cache_actual = cache_siguiente
            estado_actual = siguiente_estado
            if direccion == 'R':
                self.posCabezal += 1
            elif direccion == 'L':
                self.posCabezal -= 1
            elif direccion == 'S':
                self.posCabezal = self.posCabezal

            # Asegurar que el cabezal no se salga de la cinta
            if self.posCabezal < 0:
                self.posCabezal = 0
            elif self.posCabezal >= len(self.cinta):
                self.cinta.append(None)

        # Determinar el resultado final si no es un rechazo
        if estado_actual == self.aceptacion:
            result = "aceptado"

       
        if result != "rechazo":
            simbolo_actual = self.cinta[self.posCabezal]
            cinta_formateada = (
                ''.join([str(item) if item is not None else 'B' for item in self.cinta[:self.posCabezal]]) +
                f"[{estado_actual}, {cache_actual if cache_actual is not None else "B"}]"+
                f"{simbolo_actual if simbolo_actual is not None else 'B'}"+
                ''.join([str(item) if item is not None else 'B' for item in self.cinta[self.posCabezal + 1:]])
            )
            self.historial.append(f"|- {cinta_formateada}")

        return result, self.historial

    def writeInTXT(self):
        """Escribe el historial de la simulación en un archivo de texto."""
        with open('historial.txt', 'w') as f:
            for paso in self.historial:
                f.write(paso + '\n')

    def graph(self):
        """Genera un diagrama visual de la máquina de Turing usando Graphviz."""
        dot = Digraph(format='png', engine='dot')

       
        for estado in self.estados:
            if estado == self.aceptacion:
                dot.node(estado, shape='doublecircle', style='filled', color='lightgreen')
            elif estado == self.q0:
                dot.node(estado, shape='doublecircle', style='filled')
            else:
                dot.node(estado)


        dot.node('start', shape='point', width='0')
        dot.edge('start', self.q0)


        for estado in self.transiciones:
            for simbolo in self.transiciones[estado]:
                siguiente_estado, simbolo_escrito_en_cache, simbolo_escrito, direccion = self.transiciones[estado][simbolo]
                label = f'{simbolo[0] if simbolo[0] is not None else "B"}/{simbolo_escrito_en_cache if simbolo_escrito_en_cache is not None else "B"};{simbolo[1] if simbolo[1] is not None else "B"}/{simbolo_escrito if simbolo_escrito is not None else "B"},{direccion} '
                dot.edge(estado, siguiente_estado, label=label)

       
        if not os.path.exists('graphs'):
            os.makedirs('graphs')

       
        file_path = 'graphs/maquina_turing'
        dot.render(file_path, view=False)

        print(f"Grafo de la máquina de Turing generado y guardado en {file_path}.png.")


# EJEMPLO DE USO

# Crear instancia de la clase TM con los parámetros
estados = ['q0', 'q1', 'q2', 'q3', 'q4']
alfabetoEntrada = ['0', '1']
alfabetoCinta = ['0', '1', 'B']
q0 = 'q0'
aceptacion = 'q4'
rechazo = 'q3'
transiciones = {
    'q0': {
        '0': ['q1', '0', 'R'], 
        '1': ['q3', '1', 'R']
    },
    'q1': {
        '0': ['q1', '0', 'R'], 
        '1': ['q2', '1', 'R']
    },
    'q2': {
        '0': ['q2', '0', 'R'], 
        '1': ['q2', '1', 'R'], 
        'B': ['q4', 'B', 'R']
    }
}


# read = Reader('Proyecto4\\files\\turing_machine.yaml')
# maquina = TM(lector=read)

# # Ejecutar la simulación
# result, historial = maquina.simulate(read.cadena) #11 rechazo, 01 aceptado, 00 rechazo (con 00, si se borra transiciones de q1 -> rechazo, si se borra trasicion de q1 leyendo 0 -> rechazo)
# print(f"El resultado es \"{result}\".\nLos pasos de la MT son:")

# # Imprimir el historial de pasos
# for paso in historial:
#     print(paso)


# # # Llamar al método para imprimir la tabla de transiciones
# # maquina.imprimir_tabla_transiciones()

# # Llamar al método para generar el grafo
# maquina.graph()

# # # Guardar el historial de pasos
# maquina.writeInTXT()