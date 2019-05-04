from src.item_tabela_simbolo import ItemTabelaSimbolo

class TabelaSimbolos:

    _tamanho_array = 5

    # iniciando a variavel com tamanho determiando de itens
    _items = [None for x in range(_tamanho_array)]

    def __init__(self):
        pass

    def print(self):

        for i, no in enumerate(self._items):
            if no:
                print(i)
                self._print_nome_recursive(no)

    def _print_nome_recursive(self, item):
        print('  - ' + item.nome)

        if item._next:
            self._print_nome_recursive(item._next)


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

    """
    Buscando o item pelo nome do item
    """
    def find(self, nome):

        hash = self._convert_word_in_hash(nome)

        return self._find_by_hash(hash)

    def _find_by_hash(self, hash):

        i = self._convert_word_in_index(hash)

        item = self._items[i]

        # pega o primeiro item que tenha aquele nome
        # TODO verificar com o professor se esta certo, acho que tem que informar o escopo
        while item != None:
            if item._hash == hash:
                return item

            item = item._next

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
