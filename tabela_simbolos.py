from item_tabela_simbolo import ItemTabelaSimbolo

class TabelaSimbolos:

    _tamanho_array = 5

    # iniciando a variavel com tamanho determiando de itens
    _items = [[] for x in range(_tamanho_array)]

    def __init__(self):
        pass

    def add(self, item):

        # gerando chave
        i = self._convert_word_in_hash(item.nome)

        # salvando a chave no hash para ultilizar no metodo update
        item._hash = i

        self._items[i].append(item)

    """
    Buscando o item pelo nome do item
    """
    def find(self, nome):

        i = self._convert_word_in_hash(nome)

        # pega o primeiro item que tenha aquele nome
        # TODO verificar com o professor se esta certo, acho que tem que informar o escopo
        for item in self._items[i]:
            if item.nome == nome:
                return item

        return None

    def remove(self, item):

        item = self.find(item.nome)

        if item:

            index = [i for i, x in enumerate(self._items[item._hash]) if item == x]

            for i in index:
                del self._items[item._hash][i]

            return True

        # como esta recendo o item inteiro por paramentro é plausível que ele esteja na lista,
        # caso não estaja é gerado Exception, pq ai tem algo muito errado
        raise Exception('Item não encontrado para remover')


    def update(self, item):

        self.remove(item)
        self.add(item)


    def _convert_word_in_hash(self, word: str):

        charsAscii = []

        for c in word:
            charsAscii.append(ord(c))

        index = self._horner(charsAscii)

        return index % self._tamanho_array

    def _horner(self, chars):

        polinomio = 37

        if len(chars) == 1:
            return chars[0]
        else:
            # fazendo multiplicação
            # e passando o array de ASCII para a função recursiva
            # passando um slice maior que o primeiro item do array
            return chars[0] + polinomio * self._horner(chars[1:])
