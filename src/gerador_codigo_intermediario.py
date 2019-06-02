

class GeradorCodigoIntermediario:

    RETU = 1  # RETU - a (* a = no de parâmetros +1*)
    CRVL = 2  # CRVL L a (* L= diferença de nível ; a = deslocamento *)
    CRCT = 3  # CRCT - k
    ARMZ = 4  # ARMZ L a (* a= deslocamento; L= diferença de nível*)
    SOMA = 5  # SOMA - -
    SUBT = 6  # SUBT - -
    MULT = 7  # MULT - -
    DIVI = 8  # DIVI - -
    INVR = 9  # INVR - -
    NEGA = 10  # NEGA - -
    CONJ = 11  # CONJ - -
    DISJ = 12  # DISJ - -
    CMME = 13  # CMME - - compara menor.
    CMMA = 14  # CMMA - - compara maior.
    CMIG = 15  # CMIG - - compara igual.
    CMDF = 16  # CMDF - - compara diferente.
    CMEI = 17  # CMEI - - compara menor igual.
    CMAI = 18  # CMAI - - compara maior igual.
    DSVS = 19  # DSVS - a
    DSVF = 20  # DSVF - a
    LEIT = 21  # LEIT - -
    IMPR = 22  # IMPR - -
    IMPRL = 23  # IMPRL - a
    AMEM = 24  # AMEM - a
    CALL = 25  # CALL L a (* L= diferença de nível; a= endereço do início da proc. na área de instruções *)
    PARA = 26  # PARA - -
    NADA = 27  # NADA - -
    COPI = 28  # COPI - -
    DSVT = 29  # DSVT - a ######################## Suponho #####################

    def __init__(self):
        self._tabela = []

    def add(self, codigo, operador1, operador2):

        instrucao = {
            'codigo': codigo,
            'operador1': operador1,
            'operador2': operador2,
        }

        self._tabela.append(instrucao)

        # retorna a instrução para fazer alteração (if)
        return instrucao

    def getLc(self):
        return len(self._tabela)

    def _to_string(self):

        comandos = ['', 'RETU', 'CRVL', 'CRCT', 'ARMZ', 'SOMA', 'SUBT', 'MULT', 'DIVI', 'INVR', 'NEGA', 'CONJ', 'DISJ',
                    'CMME', 'CMMA', 'CMIG', 'CMDF', 'CMEI', 'CMAI', 'DSVS', 'DSVF', 'LEIT', 'IMPR', 'IMPRL', 'AMEM',
                    'CALL', 'PARA', 'NADA', 'COPI', 'DSVT']

        cods = '';

        for i, item in enumerate(self._tabela):
            cods = cods + str(i) + comandos[item['codigo']] + str(item['operador1']) + str(item['operador2']) + "\n"

        return cods

    def print(self):

        comandos = ['', 'RETU', 'CRVL', 'CRCT', 'ARMZ', 'SOMA', 'SUBT', 'MULT', 'DIVI', 'INVR', 'NEGA', 'CONJ', 'DISJ',
                    'CMME', 'CMMA', 'CMIG', 'CMDF', 'CMEI', 'CMAI', 'DSVS', 'DSVF', 'LEIT', 'IMPR', 'IMPRL', 'AMEM',
                    'CALL', 'PARA', 'NADA', 'COPI', 'DSVT']

        for i, item in enumerate(self._tabela):
            print(i, comandos[item['codigo']], item['operador1'], item['operador2'])