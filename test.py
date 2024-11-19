from reader import Reader
import yaml
from TM import TM
with open("files\machine_turing_aceptacion.yaml", "r") as file:
    data = yaml.safe_load(file)
lector = Reader(content=data)
print(lector)
print(lector.transiciones)

tm = TM(lector=lector)
print(tm)
print(tm.transiciones)
tm.graph()
valor, historial = tm.simulate(lector.cadenas[2])


for p in historial:
    print(p)

print(valor)