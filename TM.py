import os
from graphviz import Digraph
class TM:

    def __init__(self,  lector):
        self.estados = lector.estados
        self.alfabeto = lector.alfabeto
        self.alfabetoCinta = lector.tape_alphabet
        self.q0 = lector.q0
        self.aceptacion = lector.aceptacion
        self.transiciones = lector.transiciones
        self.tamano_cinta = 11
        self.tape = []
        self.cabezal = 0
        self.ids = []

    def validar_Cadena(self, cadena):
        return all(symbol in self.alfabetoCinta for symbol in cadena)

    def Comprobar_Transiciones(self):
        for estado, trans in self.transiciones.items():
            if estado not in self.estados:
                return False
            for simbolo, (next_state,cache_escrita, simbolo_escrito, _) in trans.items():
                if simbolo[0] not in self.alfabetoCinta or simbolo[1] not in self.alfabetoCinta or simbolo_escrito not in self.alfabetoCinta or next_state not in self.estados:
                    return False
        return True
    

    def simular(self, cadena, cintaConfiguration=[], positionCabezal=0):
        if not self.validar_Cadena(cadena):
            return "Error: Cadena contiene símbolos que no son del alfabeto.", []
        if not self.Comprobar_Transiciones():
            return "Error: Las transiciones no pertenecen al lenguaje", []
        
        result = ""
        estado_actual = self.q0
        cache_actual = None
        self.ids = []
        isReject = False 


        self.tape = cintaConfiguration if cintaConfiguration else list(cadena) + [None] * (self.tamano_cinta - len(cadena))


        self.cabezal = positionCabezal if cintaConfiguration else 0

        while not isReject and (estado_actual != self.aceptacion):
            simbolo_actual = self.tape[self.cabezal]


            id = (
                ''.join([str(item) if item is not None else 'B' for item in self.tape[:self.cabezal]]) +
                f"[{estado_actual}, {cache_actual if cache_actual is not None else "B"}]"+
                f"{simbolo_actual if simbolo_actual is not None else 'B'}"+
                ''.join([str(item) if item is not None else 'B' for item in self.tape[self.cabezal + 1:]])
            )
            self.ids.append(f"- {id}")
        

            if (cache_actual,simbolo_actual) not in self.transiciones.get(estado_actual, {}):
                result = "rechazo"
                self.ids.append(f"- [{estado_actual}] - No tiene transición para [{simbolo_actual}], la cadena se rechaza")
                isReject = True
                continue


            next_state, cache_siguiente, simbolo_escrito, direccion = self.transiciones[estado_actual][(cache_actual,simbolo_actual)]
            self.tape[self.cabezal] = simbolo_escrito
            cache_actual = cache_siguiente
            estado_actual = next_state
            if direccion == 'R':
                self.cabezal += 1
            elif direccion == 'L':
                self.cabezal -= 1
            elif direccion == 'S':
                self.cabezal = self.cabezal


            if self.cabezal < 0:
                self.cabezal = 0
            elif self.cabezal >= len(self.tape):
                self.tape.append(None)


        if estado_actual == self.aceptacion:
            result = "aceptado"

       
        if result != "rechazo":
            simbolo_actual = self.tape[self.cabezal]
            id = (
                ''.join([str(item) if item is not None else 'B' for item in self.tape[:self.cabezal]]) +
                f"[{estado_actual}, {cache_actual if cache_actual is not None else "B"}]"+
                f"{simbolo_actual if simbolo_actual is not None else 'B'}"+
                ''.join([str(item) if item is not None else 'B' for item in self.tape[self.cabezal + 1:]])
            )
            self.ids.append(f"- {id}")

        return result, self.ids, ''.join('B' if elemento is None else str(elemento) for elemento in self.tape)

    def graficar(self):
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
                next_state, simbolo_escrito_en_cache, simbolo_escrito, direccion = self.transiciones[estado][simbolo]
                label = f'{simbolo[0] if simbolo[0] is not None else "B"}/{simbolo_escrito_en_cache if simbolo_escrito_en_cache is not None else "B"};{simbolo[1] if simbolo[1] is not None else "B"}/{simbolo_escrito if simbolo_escrito is not None else "B"},{direccion} '
                dot.edge(estado, next_state, label=label)

       
        if not os.path.exists('graficas'):
            os.makedirs('graficas')

       
        file_path = 'graficas/maquina_turing'
        dot.render(file_path, view=False)

        
