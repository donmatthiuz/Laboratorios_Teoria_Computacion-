from reader import Reader
import yaml
from TM import TM
with open("files\caso_Base.yaml", "r") as file:
    data = yaml.safe_load(file)
lector = Reader(content=data)
print(lector)
print(lector.transiciones)

tm = TM(lector=lector)
print(tm)
print(tm.transiciones)
tm.graph()
print(tm.simulate(lector.cadenas[0]))
