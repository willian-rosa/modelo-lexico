from src.item_tabela_simbolo import ItemTabelaSimbolo

class TabelaSimbolos:

    _tamanho_array = 5

    def __init__(self):
        # iniciando a variavel com tamanho determiando de itens
        self._items = [None for x in range(self._tamanho_array)]

    def print(self):

        for i, no in enumerate(self._items):
            if no:
                print(i)
                self._print_nome_recursive(no)

    def _print_nome_recursive(self, item):
        print('  - ' + item.nome)

        if item._next:
            self._print_nome_recursive(item._next)

    """
    :return ItemTabelaSimbolo
    """
    def add(self, item):

        # gerando chave
        hash = self._convert_word_in_hash(item.nome)
        i = self._convert_word_in_index(hash)

        # salvando a chave no hash para ultilizar no metodo update
        item._hash = hash

        if self._items[i]:
            item._next = self._items[i]
            self._items[i] = item
        else:
            self._items[i] = item

        return item

    """
    Buscando o item pelo nome do item
    :return ItemTabelaSimbolo
    """
    def find(self, nome, nivel_base):

        hash = self._convert_word_in_hash(nome)

        return self._find_by_hash(hash, nivel_base)

    def _find_by_hash(self, hash, nivel_base):

        i = self._convert_word_in_index(hash)

        item = self._items[i]

        items_found = []

        # percorrendo a arvore para encontrar os itens correspondente ao token
        while item != None:
            if item._hash == hash and item.nivel <= nivel_base:
                items_found.append(item)

            item = item._next

        # buscando o maior nivel
        if len(items_found):

            item_max = items_found[0]

            for item_found in items_found:
                if item_found.nivel > item_max.nivel:
                    item_max = item_found

            return item_max

        return None

    def remove(self, item):

        if item._hash:

            # TODO analisar melhor
            # Esse código provavelmete não faz o menor sentido hahaha
            # uma que estamos trabalhando uma pilha, logo deveria remover o item do topo
            # e caso quiser remover um nivel deveria remover até chegar ao nivel anterior

            index = self._convert_word_in_index(item._hash)

            root = self._items[index]
            no_prev = None

            while root != None:
                if root._hash == item._hash:
                    break
                no_prev = root
                root = root._next

            if no_prev:
                no_prev._next = item._next
            else:
                # se não encontrou o prev é pq o item é o topo da pilha
                self._items[index] = item._next

            return True

        # como esta recendo o item inteiro por paramentro é plausível que ele esteja na lista,
        # caso não estaja é gerado Exception, pq ai tem algo muito errado
        raise Exception('Item não encontrado para remover')


    def update(self, item):

        self.remove(item)
        self.add(item)

        pass

    def _convert_word_in_index(self, hash: int):

        return hash % self._tamanho_array

    def _convert_word_in_hash(self, word: str):

        charsAscii = []

        for c in word:
            charsAscii.append(ord(c))

        return self._horner(charsAscii)

    def _horner(self, chars):

        polinomio = 37

        if len(chars) == 1:
            return chars[0]
        else:
            # fazendo multiplicação
            # e passando o array de ASCII para a função recursiva
            # passando um slice maior que o primeiro item do array
            return chars[0] + polinomio * self._horner(chars[1:])
