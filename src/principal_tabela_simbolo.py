from src.tabela_simbolos import TabelaSimbolos
from src.item_tabela_simbolo import ItemTabelaSimbolo

class PrincipalTabelaSimbolo:

    def run(self):
        ts = TabelaSimbolos()

        # Inserir 10 elementos;
        print('\n####################### Cadastrando 10 itens')

        # casa = 4
        # casa1 = 3
        # casa4 = 1
        # casa44 = 0

        # add item 1
        item1 = ItemTabelaSimbolo()
        item1.nome = 'casa1'
        item1.nivel = 1
        item1.categoria = 'variavel'
        item1.dado1 = 'arg1'
        item1.dado2 = 'arg2'

        ts.add(item1)

        # add o resto
        for i in range(2, 11):
            item_loop = ItemTabelaSimbolo()
            item_loop.nome = 'v'+str(i)
            item_loop.nivel = 1
            item_loop.categoria = 'variavel'
            item_loop.dado1 = 'arg1'
            item_loop.dado2 = 'arg2'

            ts.add(item_loop)

        # mostranto a tabela
        ts.print()

        print('\n####################### Alterando 5 itens')

        item1.nome = 'casa44'
        ts.update(item1)  # o item um vai para o index 0

        item_alter = ts.find('v3')
        item_alter.nome = 'v103'
        ts.update(item_alter)  # o item v3 vai para o index 1

        item_alter = ts.find('v5')
        item_alter.nome = 'v105'
        ts.update(item_alter)  # o item v5 vai para o index 2

        item_alter = ts.find('v8')
        item_alter.nome = 'v108'
        ts.update(item_alter)  # o item v8 vai para o index 1

        item_alter = ts.find('v9')
        item_alter.nome = 'v109'
        ts.update(item_alter)  # o item v9 vai para o index 4

        ts.print()

        print('\n####################### Excluindo 3 itens')
        item_delete = ts.find('v103')
        ts.remove(item_delete)

        item_delete = ts.find('v6')
        ts.remove(item_delete)


        item_delete = ts.find('v10')
        ts.remove(item_delete)

        ts.print()

        print('\n####################### busca inexistente')

        # buscando um item excluido anteriormente
        item_find_erro = ts.find('v6')  # vai retornar None, equivalente a null no java

        if not item_find_erro:
            print('Erro - Item não encontrado')

        print('\n####################### busca 3 itens')

        item_find = ts.find('v109')
        print(item_find._to_string())

        item_find = ts.find('v7')
        print(item_find._to_string())
        
        item_find = ts.find('v105')
        print(item_find._to_string())

n=PrincipalTabelaSimbolo()
n.run()
