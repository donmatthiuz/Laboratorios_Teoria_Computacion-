class CYK(object):
  def __init__(self, cfg, w):
    self.cfg  = cfg
    self.table = []
    self.w = w
    self.build_table()
  
  def build_table(self):
    longitud_cadena = len(self.w)
    self.table = [['' for _ in range(longitud_cadena - row)] for row in range(longitud_cadena)]
