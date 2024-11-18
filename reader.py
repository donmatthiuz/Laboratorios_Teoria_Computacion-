class Reader(object):
    def __init__(self, content):
      self.tm_machine = content
      self.estados = []
      self.alfabeto = []
      self.tape_alphabet = []
      self.q0 = None
      self.aceptacion = None
      self.rechazo = None
      self.transiciones = {}
      self.cinta = []
      self.get_states_and_alphabets()
      self.get_create_Transitions()
    
    def get_states_and_alphabets(self):
      self.estados = self.tm_machine['q_states']['q_list']
      self.alfabeto = self.tm_machine['alphabet']
      self.tape_alphabet = self.tm_machine['tape_alphabet'] + self.alfabeto
      self.q0 = self.tm_machine['q_states']['initial']
      self.aceptacion = self.tm_machine['q_states']['final']
      self.cadenas = self.tm_machine['simulation_strings']
    
    def get_create_Transitions(self):
      transiciones = {}
      lista_params = self.tm_machine['delta']
      valor = ''
      for l in lista_params:
        if valor != l['params']['initial_state']:
          valor = l['params']['initial_state']
          transiciones[valor] = {}
        input_value = (l['params']['mem_cache_value'],l['params']['tape_input'],)
        transiciones[valor][input_value] = [l['output']['final_state'], 
                                            l['output']['mem_cache_value'], 
                                            l['output']['tape_output'],
                                            l['output']['tape_displacement']]
      self.transiciones = transiciones