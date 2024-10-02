class Regex(object):  
  def __init__(self):
    self.lines = []

  def load_filename(self,filename):
    with open(filename, "r", encoding='utf-8') as file:
      lines = file.read().splitlines()
    for line in lines:
      splitline = line.split()
      self.lines.append(splitline)

  def load_by_text(self, text):
    lines = text.splitlines()
    for line in lines:
      splitline = line.split()
      self.lines.append(splitline)


regx = Regex()
regx.load_filename('Laboratorio_7\\file.txt')
print(regx.lines)