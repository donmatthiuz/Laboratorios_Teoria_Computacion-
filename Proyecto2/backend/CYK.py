class CYK(object):
    def __init__(self, cfg, w):
        self.cfg = cfg
        self.w = w.split(' ')
        self.table = []
        self.build_table()

    def build_table(self):
        longitud_cadena = len(self.w)
        self.table = [[set() for _ in range(longitud_cadena - row)] for row in range(longitud_cadena)]

    def algoritm(self):
        
        for i, x in enumerate(self.w):
            self.table[0][i] = set(self.cfg.get_productions_terminal(x))        
        n = len(self.w)

        for j in range(2, n + 1):
            for i in range(n - j + 1):
                for k in range(1, j):
                    B_productions = self.table[k-1][i]
                    C_productions = self.table[j-k-1][i+k]
                    for B in B_productions:
                        for C in C_productions:
                            conjuncion = B + " " + C
                            A_productions = self.cfg.get_productions_terminal(conjuncion)
                            self.table[j-1][i].update(A_productions)

        
        for row in range(len(self.table)):
            for col in range(len(self.table[row])):
                self.table[row][col] = list(self.table[row][col])

      
        if self.cfg.S in self.table[n-1][0]:
            return True
        else:
            return False
