from tabela_simbolos import TabelaSimbolos
from item_tabela_simbolo import ItemTabelaSimbolo

class PrincipalTabelaSimbolo:

    def run(self):
        ts = TabelaSimbolos()

        nomes = []

        # Inserir 10 elementos;

        # add item 1
        item1 = ItemTabelaSimbolo()
        item1.nome = 'casa'
        item1.nivel = 'a1'
        item1.categoria = 'a1'
        item1.dado2 = 'a1'
        item1.dado1 = 'a1'





        # add item 2
        item2 = ItemTabelaSimbolo()
        item2.nome = 'a2'
        item2.nivel = 'a2'
        item2.categoria = 'a2'
        item2.dado2 = 'a2'
        item2.dado1 = 'a2'
        ts.add(item2)

        # add item 3
        item3 = ItemTabelaSimbolo()
        item3.nome = 'b3'
        item3.nivel = 'b3'
        item3.categoria = 'b3'
        item3.dado2 = 'b3'
        item3.dado1 = 'b3'
        ts.add(item3)

        # add item 4
        item4 = ItemTabelaSimbolo()
        item4.nome = 'f3'
        item4.nivel = 'f3'
        item4.categoria = 'f3'
        item4.dado2 = 'f3'
        item4.dado1 = 'f3'
        ts.add(item4)

        # add item 5
        item5 = ItemTabelaSimbolo()
        item5.nome = 'j4'
        item5.nivel = 'j4'
        item5.categoria = 'j4'
        item5.dado2 = 'j4'
        item5.dado1 = 'j4'
        ts.add(item5)

        # add item 6
        item = ItemTabelaSimbolo()
        item.nome = 'r4'
        item.nivel = 'r4'
        item.categoria = 'r4'
        item.dado2 = 'r4'
        item.dado1 = 'r4'
        ts.add(item)

        # add item 7
        item = ItemTabelaSimbolo()
        item.nome = 'm7'
        item.nivel = 'm7'
        item.categoria = 'm7'
        item.dado2 = 'm7'
        item.dado1 = 'm7'
        ts.add(item)


        # add item 8
        item = ItemTabelaSimbolo()
        item.nome = 'b3'
        item.nivel = 'b3'
        item.categoria = 'b3'
        item.dado2 = 'b3'
        item.dado1 = 'b3'
        ts.add(item)

        # add item 9
        item = ItemTabelaSimbolo()
        item.nome = 'p7'
        item.nivel = 'p7'
        item.categoria = 'p7'
        item.dado2 = 'p7'
        item.dado1 = 'p7'
        ts.add(item)

        # add item 10
        item = ItemTabelaSimbolo()
        item.nome = 'D7'
        item.nivel = 'D7'
        item.categoria = 'D7'
        item.dado2 = 'D7'
        item.dado1 = 'D7'
        ts.add(item)

        #####################################################################################3

        # Alterar dados de 5 elementos;
        item2.nome = 'novo_nome_para_item_1'
        ts.update(item2)

        item = ItemTabelaSimbolo()

        item.nome = 'f2'
        item.nivel = 'ak3'
        item.categoria = 'ak3'
        item.dado2 = 'ak4'
        item.dado1 = 'ak5'
        ts.update(item)

        item = ItemTabelaSimbolo()

        item.nome = 'h3'
        item.nivel = 'au3'
        item.categoria = 'r3'
        item.dado2 = 'aq3'
        item.dado1 = 'aty'
        ts.update(item)


        ##########################################################################
        # - Excluir 3 elementos;


        # del item 1
        ts.remove(item1)

        # del item 9
        item = ItemTabelaSimbolo()
        nomes.remove(item.nome, item.nivel, item.categoria, item.dado2, item.dado1)
        item.nome = 'p7'
        item.nivel = 'p7'
        item.categoria = 'p7'
        item.dado2 = 'p7'
        item.dado1 = 'p7'
        ts.remove(item)



        # del item 10
        item = ItemTabelaSimbolo()
        nomes.remove(item.nome, item.nivel, item.categoria, item.dado2, item.dado1)
        item.nome = 'D7'
        item.nivel = 'D7'
        item.categoria = 'D7'
        item.dado2 = 'D7'
        item.dado1 = 'D7'
        ts.remove(item)


        find_item_erro = ts.find('...')

        if not find_item_erro:
            print('Token de pesquisa invalido')


        find_item_2 = ts.find('novo_nome_para_item_1')

        if find_item_2:
            print('encontrou')
        else:
            print('Token de pesquisa invalido para item 2x')




#O retonro do metodo vai retornar o tipo none
#variavel que vai receber/vai fazr a busca e vai atribuir a uma variavel se for tipo none vai dar um print com a mensagem: nao encontrou o elemento


 #- Fazer uma busca por 1 elemento inexistente na tabela. Mostrar mensagem informando que o elemento não foi encontrado;
 # chamar o metodo encontrar
 #- Fazer uma busca por nome de 3 elementos que estão na tabela. Mostrar os dados completos dos elementos encontrados.
#buscar tres itens que tenham cadastrado

n=PrincipalTabelaSimbolo()
n.run()
