class ItemTabelaSimbolo:

    _hash = None
    _next = None

    nome = None
    categoria = None
    nivel = None
    dado1 = None
    dado2 = None

    def __init__(self, nome, categoria, nivel, dado1, dado2):
        self.nome = nome
        self.categoria = categoria
        self.nivel = nivel
        self.dado1 = dado1
        self.dado2 = dado2


    def _to_string(self):
        return 'Nome: '+str(self.nome) + \
        ' - Categoria: '+str(self.categoria) + \
        ' - Nivel: '+str(self.nivel) + \
        ' - Dado1: '+str(self.dado1) + \
        ' - Dado2: '+str(self.dado2)
