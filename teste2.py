from tabela_simbolos import TabelaSimbolos
from item_tabela_simbolo import ItemTabelaSimbolo


ts = TabelaSimbolos()

nome = 'v103'
hash = ts._convert_word_in_hash(nome)
i = ts._convert_word_in_index(hash)
print(nome, i, hash)

nome = 'v108'
hash = ts._convert_word_in_hash(nome)
i = ts._convert_word_in_index(hash)
print(nome, i, hash)

nome = 'v109'
hash = ts._convert_word_in_hash(nome)
i = ts._convert_word_in_index(hash)
print(nome, i, hash)


nome = 'v110'
hash = ts._convert_word_in_hash(nome)
i = ts._convert_word_in_index(hash)
print(nome, i, hash)