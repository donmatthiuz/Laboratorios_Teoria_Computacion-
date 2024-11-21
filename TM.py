import os
from graphviz import Digraph

class TuringMachine:
    def __init__(self, lector):
        self.estados = lector.estados
        self.alfabeto = lector.alfabeto
        self.alfabetoCinta = lector.tape_alphabet
        self.estado_inicial = lector.q0
        self.estado_aceptacion = lector.aceptacion
        self.transiciones = lector.transiciones
        self.longitud_cinta = 11
        self.cinta = []
        self.posicion_cabezal = 0
        self.historial = []

    def es_cadena_valida(self, cadena):
        return all(caracter in self.alfabetoCinta for caracter in cadena)

    def validar_transiciones(self):
        for estado, reglas in self.transiciones.items():
            if estado not in self.estados:
                return False
            for entrada, (siguiente_estado, cache, escribir, _) in reglas.items():
                if (entrada[0] not in self.alfabetoCinta or entrada[1] not in self.alfabetoCinta or 
                    escribir not in self.alfabetoCinta or siguiente_estado not in self.estados):
                    return False
        return True

    def procesar(self, entrada, configuracion_inicial=[], posicion_inicial=0):
        if not self.es_cadena_valida(entrada):
            return "Error: La cadena contiene caracteres no válidos.", []
        if not self.validar_transiciones():
            return "Error: Las transiciones no son válidas.", []

        estado_actual = self.estado_inicial
        cache = None
        self.historial = []
        es_rechazada = False

        self.cinta = configuracion_inicial if configuracion_inicial else list(entrada) + [None] * (self.longitud_cinta - len(entrada))
        self.posicion_cabezal = posicion_inicial if configuracion_inicial else 0

        while not es_rechazada and estado_actual != self.estado_aceptacion:
            simbolo_actual = self.cinta[self.posicion_cabezal]

            paso = (
                ''.join(str(x) if x is not None else 'B' for x in self.cinta[:self.posicion_cabezal]) +
                f"[{estado_actual}, {cache if cache is not None else 'B'}]" +
                f"{simbolo_actual if simbolo_actual is not None else 'B'}" +
                ''.join(str(x) if x is not None else 'B' for x in self.cinta[self.posicion_cabezal + 1:])
            )
            self.historial.append(f"- {paso}")

            if (cache, simbolo_actual) not in self.transiciones.get(estado_actual, {}):
                self.historial.append(f"- [{estado_actual}] - No se encontró transición para [{simbolo_actual}], la cadena es rechazada")
                es_rechazada = True
                continue

            siguiente_estado, nuevo_cache, escribir, direccion = self.transiciones[estado_actual][(cache, simbolo_actual)]
            self.cinta[self.posicion_cabezal] = escribir
            cache = nuevo_cache
            estado_actual = siguiente_estado

            if direccion == 'R':
                self.posicion_cabezal += 1
            elif direccion == 'L':
                self.posicion_cabezal -= 1

            if self.posicion_cabezal < 0:
                self.posicion_cabezal = 0
            elif self.posicion_cabezal >= len(self.cinta):
                self.cinta.append(None)

        resultado = "rechazada" if es_rechazada else "aceptada"

        if resultado == "aceptada":
            simbolo_actual = self.cinta[self.posicion_cabezal]
            paso = (
                ''.join(str(x) if x is not None else 'B' for x in self.cinta[:self.posicion_cabezal]) +
                f"[{estado_actual}, {cache if cache is not None else 'B'}]" +
                f"{simbolo_actual if simbolo_actual is not None else 'B'}" +
                ''.join(str(x) if x is not None else 'B' for x in self.cinta[self.posicion_cabezal + 1:])
            )
            self.historial.append(f"- {paso}")

        return resultado, self.historial, ''.join('B' if x is None else str(x) for x in self.cinta)

    def generar_grafico(self):
        grafo = Digraph(format='png', engine='dot')

        for estado in self.estados:
            if estado == self.estado_aceptacion:
                grafo.node(estado, shape='doublecircle', style='filled', color='lightgreen')
            elif estado == self.estado_inicial:
                grafo.node(estado, shape='doublecircle', style='filled')
            else:
                grafo.node(estado)

        grafo.node('inicio', shape='point', width='0')
        grafo.edge('inicio', self.estado_inicial)

        for estado, reglas in self.transiciones.items():
            for simbolo, (siguiente_estado, _, escribir, direccion) in reglas.items():
                etiqueta = f"{simbolo[0] or 'B'}/{simbolo[1] or 'B'} -> {escribir or 'B'}, {direccion}"
                grafo.edge(estado, siguiente_estado, label=etiqueta)

        if not os.path.exists('graficas'):
            os.makedirs('graficas')

        ruta = 'graficas/maquina_turing'
        grafo.render(ruta, view=False)
