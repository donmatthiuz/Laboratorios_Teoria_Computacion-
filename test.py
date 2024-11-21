from reader import Reader
import yaml
from TM import TM
with open("maquinas\maquina_alteradora.yaml", "r") as file:
    data = yaml.safe_load(file)
lector = Reader(content=data)
print(lector)
print(lector.transiciones)

tm = TM(lector=lector)
print(tm)
print(tm.transiciones)
tm.graficar()
valor, ids, cinta = tm.simular(lector.cadenas[3])


for i in ids:
    print(i)

print(valor) 
resultado = ''.join('B' if elemento is None else str(elemento) for elemento in cinta)
print(resultado)