from tabela_simbolos import TabelaSimbolos
from item_tabela_simbolo import ItemTabelaSimbolo

class PrincipalTabelaSimbolo:

    def run(self):
        ts = TabelaSimbolos()

        nomes = []

        # Inserir 10 elementos;

        # add item 1
        item = ItemTabelaSimbolo()
        item.nome = 'casa'
        item.nivel = 'a1'
        item.categoria = 'a1'
        item.dado2 = 'a1'
        item.dado1 = 'a1'

        # add item 2
        item = ItemTabelaSimbolo()
        item.nome = 'a2'
        item.nivel = 'a2'
        item.categoria = 'a2'
        item.dado2 = 'a2'
        item.dado1 = 'a2'
        nomes.append(item.nome)
        ts.add(item)

        # add item 3
        item = ItemTabelaSimbolo()
        item.nome = 'b3'
        item.nivel = 'b3'
        item.categoria = 'b3'
        item.dado2 = 'b3'
        item.dado1 = 'b3'
        nomes.append(item.nome)
        ts.add(item)

        # add item 4
        item = ItemTabelaSimbolo()
        item.nome = 'f3'
        item.nivel = 'f3'
        item.categoria = 'f3'
        item.dado2 = 'f3'
        item.dado1 = 'f3'
        nomes.append(item.nome)
        ts.add(item)

        # add item 5
        item = ItemTabelaSimbolo()
        item.nome = 'j4'
        item.nivel = 'j4'
        item.categoria = 'j4'
        item.dado2 = 'j4'
        item.dado1 = 'j4'
        nomes.append(item.nome)
        ts.add(item)

        # add item 6
        item = ItemTabelaSimbolo()
        item.nome = 'r4'
        item.nivel = 'r4'
        item.categoria = 'r4'
        item.dado2 = 'r4'
        item.dado1 = 'r4'
        nomes.append(item.nome)
        ts.add(item)

        # add item 7
        item = ItemTabelaSimbolo()
        item.nome = 'm7'
        item.nivel = 'm7'
        item.categoria = 'm7'
        item.dado2 = 'm7'
        item.dado1 = 'm7'
        nomes.append(item.nome)
        ts.add(item)


        # add item 8
        item = ItemTabelaSimbolo()
        item.nome = 'b3'
        item.nivel = 'b3'
        item.categoria = 'b3'
        item.dado2 = 'b3'
        item.dado1 = 'b3'
        nomes.append(item.nome)
        ts.add(item)

        # add item 9
        item = ItemTabelaSimbolo()
        item.nome = 'p7'
        item.nivel = 'p7'
        item.categoria = 'p7'
        item.dado2 = 'p7'
        item.dado1 = 'p7'
        nomes.append(item.nome)
        ts.add(item)

        # add item 10
        item = ItemTabelaSimbolo()
        item.nome = 'D7'
        item.nivel = 'D7'
        item.categoria = 'D7'
        item.dado2 = 'D7'
        item.dado1 = 'D7'
        nomes.append(item.nome)
        ts.add(item)

        # Alterar dados de 5 elementos;
        item = ItemTabelaSimbolo()
        nomes.append(item.nome,item.nivel,item.categoria,item.dado2,item.dado1)
        item.nome = 'carro'
        item.nivel = 'a12'
        item.categoria = 'a13'
        item.dado2 = 'a14'
        item.dado1 = 'a15'
        ts.update(item)

        item = ItemTabelaSimbolo()
        nomes.append(item.nome,item.nivel,item.categoria,item.dado2,item.dado1)
        item.nome = 'f2'
        item.nivel = 'ak3'
        item.categoria = 'ak3'
        item.dado2 = 'ak4'
        item.dado1 = 'ak5'
        ts.update(item)

        item = ItemTabelaSimbolo()
        nomes.append(item.nome,item.nivel,item.categoria,item.dado2,item.dado1)
        item.nome = 'h3'
        item.nivel = 'au3'
        item.categoria = 'r3'
        item.dado2 = 'aq3'
        item.dado1 = 'aty'
        ts.update(item)

        # - Excluir 3 elementos;


        # del item 8
        item = ItemTabelaSimbolo()
        nomes.remove(item.nome, item.nivel, item.categoria, item.dado2, item.dado1)
        item.nome = 'b3'
        item.nivel = 'b3'
        item.categoria = 'b3'
        item.dado2 = 'b3'
        item.dado1 = 'b3'
        nomes.append(item.nome)
        ts.remove(item)

        # del item 9
        item = ItemTabelaSimbolo()
        nomes.remove(item.nome, item.nivel, item.categoria, item.dado2, item.dado1)
        item.nome = 'p7'
        item.nivel = 'p7'
        item.categoria = 'p7'
        item.dado2 = 'p7'
        item.dado1 = 'p7'
        nomes.append(item.nome)
        ts.remove(item)

        # del item 10
        item = ItemTabelaSimbolo()
        nomes.remove(item.nome, item.nivel, item.categoria, item.dado2, item.dado1)
        item.nome = 'D7'
        item.nivel = 'D7'
        item.categoria = 'D7'
        item.dado2 = 'D7'
        item.dado1 = 'D7'
        nomes.append(item.nome)
        ts.remove(item)


#O retonro do metodo vai retornar o tipo none
#variavel que vai receber/vai fazr a busca e vai atribuir a uma variavel se for tipo none vai dar um print com a mensagem: nao encontrou o elemento


 #- Fazer uma busca por 1 elemento inexistente na tabela. Mostrar mensagem informando que o elemento não foi encontrado;
 # chamar o metodo encontrar
 #- Fazer uma busca por nome de 3 elementos que estão na tabela. Mostrar os dados completos dos elementos encontrados.
#buscar tres itens que tenham cadastrado