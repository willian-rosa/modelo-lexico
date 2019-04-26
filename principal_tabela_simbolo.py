from tabela_simbolos import TabelaSimbolos
from item_tabela_simbolo import ItemTabelaSimbolo

class PrincipalTabelaSimbolo:

    def run(self):
        ts = TabelaSimbolos()


        # add item 1
        item = ItemTabelaSimbolo()
        item.nome = 'casa'
        item.nivel = 'a1'
        item.categoria = 'a1'
        item.dado2 = 'a1'
        item.dado1 = 'a1'

        ts.add(item)

        # add item 2
        item = ItemTabelaSimbolo()
        item.nome = 'a2'
        item.nivel = 'a2'
        item.categoria = 'a2'
        item.dado2 = 'a2'
        item.dado1 = 'a2'

        ts.add(item)



