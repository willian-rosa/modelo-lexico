class ItemTabelaSimbolo:

    _hash = None
    _next = None

    nome = None
    categoria = None
    nivel = None
    dado1 = None
    dado2 = None

    def _to_string(self):
        return 'Nome: '+str(self.nome) + \
        ' - Categoria: '+str(self.categoria) + \
        ' - Nivel: '+str(self.nivel) + \
        ' - Dado1: '+str(self.dado1) + \
        ' - Dado2: '+str(self.dado2)
