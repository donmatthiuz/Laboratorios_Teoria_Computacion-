import os
from graphviz import Digraph
from reader import Reader
class TM:
    """
    Clase para simular una Máquina de Turing determinista.
    
    Parámetros:
        estados (list): Lista de estados de la máquina.
        alfabetoEntrada (list): Lista de símbolos del alfabeto de entrada.
        alfabetoCinta (list): Lista de símbolos del alfabeto de la cinta.
        q0 (str): Estado inicial.
        aceptacion (str): Estado de aceptación.
        rechazo (str): Estado de rechazo.
        transiciones (dict): Diccionario de transiciones con formato {estado: {simbolo: [siguiente_estado, simbolo_escrito, direccion]}}.

    Ejemplo de configuración:
        estados = ['q0', 'q1', 'q2', 'q3', 'q4']
        alfabetoEntrada = ['0', '1']
        alfabetoCinta = ['0', '1', 'B']
        q0 = 'q0'
        aceptacion = 'q4'
        rechazo = 'q3'
        transiciones = {
            'q0': {'0': ['q1', '0', 'R'], '1': ['q3', '1', 'R']},
            'q1': {'0': ['q1', '0', 'R'], '1': ['q2', '1', 'R']},
            'q2': {'0': ['q2', '0', 'R'], '1': ['q2', '1', 'R'], 'B': ['q4', 'B', 'R']}
        }
    """

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

    def isValidString(self, cadena):
        """Valida si la cadena pertenece al alfabeto de entrada de la máquina."""
        return all(symbol in self.alfabetoCinta for symbol in cadena)

    def isValidTransitions(self):
        """Valida si las transiciones cumplen con el alfabeto de la cinta y estados definidos."""
        for estado, trans in self.transiciones.items():
            if estado not in self.estados:
                return False
            for simbolo, (siguiente_estado,cache_escrita, simbolo_escrito, _) in trans.items():
                if simbolo[0] not in self.alfabetoCinta or simbolo[1] not in self.alfabetoCinta or simbolo_escrito not in self.alfabetoCinta or siguiente_estado not in self.estados:
                    return False
        return True
    
    def imprimir_tabla_transiciones(self):
        print(f"{'Estado':<10}{'Símbolo':<10}{'Siguiente Estado':<20}{'Símbolo Escrito':<20}{'Dirección'}")
        print("-" * 70)
        
        for estado in self.transiciones:
            for simbolo in self.transiciones[estado]:
                siguiente_estado, simbolo_escrito, direccion = self.transiciones[estado][simbolo]
                print(f"{estado:<10}{simbolo:<10}{siguiente_estado:<20}{simbolo_escrito:<20}{direccion}")

    def simulate(self, cadena, cintaConfiguration=[], positionCabezal=0):
        """
        Ejecuta la simulación de la máquina de Turing con la cadena de entrada.
        
        Args:
            cadena (str): La cadena de entrada a procesar.
            cintaConfiguration (list): Configuración inicial de la cinta.
            positionCabezal (int): Posición inicial del cabezal.
        
        Returns:
            result (str): Resultado de la simulación ('aceptado', 'rechazo' o 'bucle').
            historial (list): Registro paso a paso de la simulación.
        """
        if not self.isValidString(cadena):
            return "Error: Cadena contiene símbolos fuera del alfabeto de entrada.", []
        if not self.isValidTransitions():
            return "Error: Las transiciones son inválidas.", []
        
        result = ""
        estado_actual = self.q0
        self.historial = []  # Reiniciar historial en cada simulación
        isBucle = False  # Flag para controlar el bucle

        # Usar la configuración de la cinta si se proporciona, de lo contrario, usa la cadena
        self.cinta = cintaConfiguration if cintaConfiguration else list(cadena) + ['B'] * (self.size_cinta - len(cadena))

        # Asignar la posición del cabezal dependiendo de si se pasó una configuración de la cinta
        self.posCabezal = positionCabezal if cintaConfiguration else 0

        while not isBucle and (estado_actual != self.aceptacion and estado_actual != self.rechazo):
            simbolo_actual = self.cinta[self.posCabezal]

            # Formatear la cinta con el estado y el símbolo en la posición del cabezal
            cinta_formateada = (
                ''.join(self.cinta[:self.posCabezal]) +
                f"[{estado_actual}, {simbolo_actual}]" +
                ''.join(self.cinta[self.posCabezal + 1:])
            )
            self.historial.append(f"|- {cinta_formateada}")

            # Detectar bucle verificando si la transición no existe
            if simbolo_actual not in self.transiciones.get(estado_actual, {}):
                result = "bucle"
                self.historial.append(f"|- [{estado_actual}] - No tiene transición para [{simbolo_actual}], se detectó un bucle")
                isBucle = True
                continue

            # Obtener la transición y actualizar la cinta, estado y cabezal
            siguiente_estado, simbolo_escrito, direccion = self.transiciones[estado_actual][simbolo_actual]
            self.cinta[self.posCabezal] = simbolo_escrito
            estado_actual = siguiente_estado
            self.posCabezal += 1 if direccion == 'R' else -1

            # Asegurar que el cabezal no se salga de la cinta
            if self.posCabezal < 0:
                self.posCabezal = 0
            elif self.posCabezal >= len(self.cinta):
                self.cinta.append('B')

        # Determinar el resultado final si no es un bucle
        if estado_actual == self.aceptacion:
            result = "aceptado"
        elif estado_actual == self.rechazo:
            result = "rechazo"

       
        if result != "bucle":
            simbolo_actual = self.cinta[self.posCabezal]
            cinta_formateada = (
                ''.join(self.cinta[:self.posCabezal]) +
                f"[{estado_actual}, {simbolo_actual}]" +
                ''.join(self.cinta[self.posCabezal + 1:])
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
# result, historial = maquina.simulate(read.cadena) #11 rechazo, 01 aceptado, 00 bucle (con 00, si se borra transiciones de q1 -> bucle, si se borra trasicion de q1 leyendo 0 -> bucle)
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