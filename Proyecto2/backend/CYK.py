from backend.Node import Node
class CYK(object):
    def __init__(self, cfg, w):
        self.cfg = cfg
        self.w = w.split(' ')
        self.table = []
        self.build_table()
        self.node_id = 0

    def build_table(self):
        longitud_cadena = len(self.w)
        self.table = [[set() for _ in range(longitud_cadena - row)] for row in range(longitud_cadena)]

    def algoritm(self):
        for i, x in enumerate(self.w):
            terminal_productions = self.cfg.get_productions_terminal(x)
            terminal_node = Node(x, self.node_id)
            self.node_id += 1
            for A in terminal_productions:
                non_terminal_node = Node(A, self.node_id)
                non_terminal_node.left = terminal_node
                self.node_id += 1
                self.table[0][i].add(non_terminal_node)

        n = len(self.w)

        for j in range(2, n + 1):
            for i in range(n - j + 1):
                for k in range(1, j):
                    B_productions = self.table[k-1][i]
                    C_productions = self.table[j-k-1][i+k]

                    for B_node in B_productions:
                        for C_node in C_productions:
                            conjuncion = B_node.data + " " + C_node.data
                            A_productions = self.cfg.get_productions_terminal(conjuncion)
                            
                            for A in A_productions:
                                A_node = Node(A, self.node_id)
                                A_node.left = B_node
                                A_node.right = C_node
                                self.table[j-1][i].add(A_node)
                                self.node_id += 1

        root_nodes = [node for node in self.table[n-1][0] if node.data == self.cfg.S]

        if root_nodes:
            return root_nodes[0]
        else:
            return None