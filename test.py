from reader import Reader
import yaml
with open("files\caso_Base.yaml", "r") as file:
    data = yaml.safe_load(file)
lector = Reader(content=data)
print(lector)
print(lector.transiciones)

