from tabela_simbolos import TabelaSimbolos
from item_tabela_simbolo import ItemTabelaSimbolo


ts = TabelaSimbolos()
its1 = ItemTabelaSimbolo()
its1.nome = 'casa'


ts.add(its1)

its2 = ItemTabelaSimbolo()
its2.nome = 'casa2'
ts.add(its2)



aa = ts.remove(its2)
print(aa)