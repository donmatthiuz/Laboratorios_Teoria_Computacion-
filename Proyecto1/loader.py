
def reader(filename):
  with open(filename, "r", encoding='utf-8') as file:
    lines = file.read().splitlines()
  return lines