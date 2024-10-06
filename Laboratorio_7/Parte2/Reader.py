class Reader (object):
  def __init__(self, cfg):
    self.cfg = cfg
    self.string_P = ""
  
  def show_CFG_productions(self):
    for non_terminal in self.cfg.V:
      self.string_P += f"{non_terminal} → "
      i = 0
      for idx, production in enumerate(self.cfg.P):
        if production.v_ == non_terminal:
          if i == 0:
            self.string_P += f"{production.t_} "
          else:
            self.string_P += f"| {production.t_} "
          i += 1
      self.string_P += "\n"
