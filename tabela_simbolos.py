
class TabelaSimbolos:
    
    items = []

    def init(self):
        pass

    def add(self, item):
        i = self._convert_word_in_hash(item.nome)
        # TODO tem que trabalhar com as pilhas e colisões
        item[i] = item

    def find(self, item):
        i = self._convert_word_in_hash(item.nome)
        # TODO tem que trabalhar com as pilhas e colisões
        return item[i]

    def remove(self, item):
        i = self._convert_word_in_hash(item.nome)
        # TODO tem que trabalhar com as pilhas e colisões
        del item[i]

    def update(self, item):
        self.add(item)

    def _convert_word_in_hash(self, word: str):

        charsAscii = []

        for c in word:
            charsAscii.append(ord(c))

        index = self._horner(charsAscii)

        return index % 50



    def _horner(self, chars):

        polinomio = 37

        if len(chars) == 1:
            return chars[0]
        else:
            # fazendo multiplicação
            # e passando o array de ASCII para a função recursiva
            # passando um slice maior que o primeiro item do array
            return chars[0] + polinomio * self._horner(chars[1:])
