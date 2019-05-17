from src.tabela_simbolos import TabelaSimbolos
from src.item_tabela_simbolo import ItemTabelaSimbolo
from src.gerador_codigo_intermediario import GeradorCodigoIntermediario

class AnalisadorSemantico:

    def __init__(self, gerador_codigo: GeradorCodigoIntermediario):
        print("iniciando analisador semantico")
        self._cod_intermediario = gerador_codigo

    def executeAcao(self, codigo_acao, token_nao_terminal_atual):

        if codigo_acao == 100:
            self._acao_semantica_100()
        elif codigo_acao == 101:
            self._acao_semantica_101()
        elif codigo_acao == 102:
            self._acao_semantica_102()
        elif codigo_acao == 104:
            self._acao_semantica_104(token_nao_terminal_atual)
        elif codigo_acao == 105:
            self._acao_semantica_105(token_nao_terminal_atual)
        elif codigo_acao == 106:
            self._acao_semantica_106(token_nao_terminal_atual)
        elif codigo_acao == 107:
            self._acao_semantica_107()
        elif codigo_acao == 108:
            self._acao_semantica_108()
        elif codigo_acao == 109:
            self._acao_semantica_109()
        elif codigo_acao == 110:
            self._acao_semantica_110()
        elif codigo_acao == 111:
            self._acao_semantica_111()
        elif codigo_acao == 114:
            self._acao_semantica_114(token_nao_terminal_atual)
        elif codigo_acao == 115:
            self._acao_semantica_115()
        elif codigo_acao == 116:
            self._acao_semantica_116()
        elif codigo_acao == 117:
            self._acao_semantica_117()
        elif codigo_acao == 118:
            self._acao_semantica_118()
        elif codigo_acao == 120:
            self._acao_semantica_120()
        elif codigo_acao == 121:
            self._acao_semantica_121()
        elif codigo_acao == 122:
            self._acao_semantica_122()
        elif codigo_acao == 123:
            self._acao_semantica_123()
        elif codigo_acao == 124:
            self._acao_semantica_124()
        elif codigo_acao == 125:
            self._acao_semantica_125()
        elif codigo_acao == 126:
            self._acao_semantica_126()
        elif codigo_acao == 127:
            self._acao_semantica_127()
        elif codigo_acao == 128:
            self._acao_semantica_128()
        elif codigo_acao == 129:
            self._acao_semantica_129(token_nao_terminal_atual)
        elif codigo_acao == 130:
            self._acao_semantica_130(token_nao_terminal_atual)
        elif codigo_acao == 131:
            self._acao_semantica_131()
        elif codigo_acao == 132:
            self._acao_semantica_132()
        elif codigo_acao == 133:
            self._acao_semantica_133()
        elif codigo_acao == 134:
            self._acao_semantica_134(token_nao_terminal_atual)
        elif codigo_acao == 135:
            self._acao_semantica_135()
        elif codigo_acao == 136:
            self._acao_semantica_136(token_nao_terminal_atual)
        elif codigo_acao == 137:
            self._acao_semantica_137(token_nao_terminal_atual)
        elif codigo_acao == 138:
            self._acao_semantica_138()
        elif codigo_acao == 139:
            self._acao_semantica_139()
        elif codigo_acao == 140:
            self._acao_semantica_140(token_nao_terminal_atual)
        elif codigo_acao == 141:
            self._acao_semantica_141()
        elif codigo_acao == 142:
            self._acao_semantica_142()
        elif codigo_acao == 143:
            self._acao_semantica_143()
        elif codigo_acao == 144:
            self._acao_semantica_144()
        elif codigo_acao == 145:
            self._acao_semantica_145()
        elif codigo_acao == 146:
            self._acao_semantica_146()
        elif codigo_acao == 147:
            self._acao_semantica_147()
        elif codigo_acao == 148:
            self._acao_semantica_148()
        elif codigo_acao == 149:
            self._acao_semantica_149()
        elif codigo_acao == 150:
            self._acao_semantica_150()
        elif codigo_acao == 151:
            self._acao_semantica_151()
        elif codigo_acao == 152:
            self._acao_semantica_152()
        elif codigo_acao == 153:
            self._acao_semantica_153()
        elif codigo_acao == 154:
            self._acao_semantica_154(token_nao_terminal_atual)
        elif codigo_acao == 155:
            self._acao_semantica_155()
        elif codigo_acao == 156:
            self._acao_semantica_156()

    def is_variable(self, token):

        id = self._ts.find(token['token'])

        if id and id.categoria == 'variavel':
            return True
        else:
            raise Exception('Identificador "'+str(token['token'])+'" não foi declarado')  # TODO colocar linha

    def _acao_semantica_100(self):
        self._pilhas = []
        self._ts = TabelaSimbolos()
        self._pilha_literais = []
        self._numero_variaveis = 0
        self._deslocamento = 3
        self._lc = None
        self._lit = None

        self._nivel_atual = 0

        # pilhas
        self._pilha_ifs = []
        self._pilha_whiles = []
        self._pilha_fors = []
        self._pilha_repeats = []
        self._pilha_strings = []
        self._pilha_case = []

        # controle de pilha
        self._ponteiro_string = -1
        self._tipo_identificador = ''
        self._contexto = ''
        self._topo = self._deslocamento
        self._variavel_a_esquerda = None
        self._constante_a_esquerda = None



    def _acao_semantica_101(self):
        #Gera instrução PARA
        # Verifica utilização de rótulos através da tabela de símbolos

        self._cod_intermediario.add(self._cod_intermediario.PARA, '-', '-')

        # TODO Verifica utilização de rótulos através da tabela de símbolos


    def _acao_semantica_102(self):

        self._cod_intermediario.add(self._cod_intermediario.AMEM, '-', self._deslocamento + self._numero_variaveis)


    def _acao_semantica_104(self, token):

        if self._tipo_identificador == 'rotulo':
            raise Exception('Falta desenvolver')  # TODO Falta desenvolver
        elif self._tipo_identificador == 'variavel':

            if self._ts.find(token['token']):
                raise Exception('Variavel já declarada') #TODO colocar linha
            else:

                self._ts.add(ItemTabelaSimbolo(
                    token['token'],
                    'variavel',
                    self._nivel_atual,
                    self._topo,
                    '-'
                ))

                self._topo = self._topo + 1

                self._numero_variaveis = self._numero_variaveis + 1

        elif self._tipo_identificador == 'paramentro':
            raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_105(self, token):
        if self._ts.find(token['token']):
            raise Exception('Constante já declarada')  # TODO colocar linha
        else:
            constant = ItemTabelaSimbolo(
                token['token'],
                'constante',
                self._nivel_atual,
                '-',
                '-'
            )

            self._ts.add(constant)

            self._constante_a_esquerda = constant

    def _acao_semantica_106(self, token):
        self._constante_a_esquerda.dado1 = token['token']

    def _acao_semantica_107(self):
        self._tipo_identificador = 'variavel'

    def _acao_semantica_108(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_109(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_110(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_111(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_114(self, token):

        identificador = self._ts.find(token['token'])

        if identificador:
            if identificador.categoria == 'variavel':
                self._variavel_a_esquerda = identificador
            else:
                raise Exception('Não é permitido atribuir valor em '+identificador.categoria)  # TODO colocar linha
        else:
            raise Exception('Identificador não declarado')  # TODO colocar linha

    def _acao_semantica_115(self):

        self._cod_intermediario.add(self._cod_intermediario.ARMZ, self._nivel_atual, self._variavel_a_esquerda.dado1)

    def _acao_semantica_116(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_117(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_118(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_120(self):

        instrucao = self._cod_intermediario.add(self._cod_intermediario.DSVF, '-', 999)
        self._pilha_ifs.append(instrucao)

    def _acao_semantica_121(self):
        self._pilha_ifs[-1]['operador2'] = self._cod_intermediario.getLc()

        del self._pilha_ifs[-1]

    def _acao_semantica_122(self):

        self._pilha_ifs[-1]['operador2'] = self._cod_intermediario.getLc() + 1

        del self._pilha_ifs[-1]

        instrucao = self._cod_intermediario.add(self._cod_intermediario.DSVS, '-', 999)

        self._pilha_ifs.append(instrucao)


    def _acao_semantica_123(self):
        self._pilha_whiles.append(self._cod_intermediario.getLc())

    def _acao_semantica_124(self):
        instrucao = self._cod_intermediario.add(self._cod_intermediario.DSVF, '-', 999)

        self._pilha_whiles.append(instrucao)


    def _acao_semantica_125(self):

        self._pilha_whiles[-1]['operador2'] = self._cod_intermediario.getLc() + 1

        del self._pilha_whiles[-1]

        self._cod_intermediario.add(self._cod_intermediario.DSVS, '-', self._pilha_whiles[-1])

        del self._pilha_whiles[-1]


    def _acao_semantica_126(self):
        self._pilha_repeats.append(self._cod_intermediario.getLc())

    def _acao_semantica_127(self):

        self._cod_intermediario.add(self._cod_intermediario.DSVF, '-', self._pilha_repeats[-1])

        del self._pilha_repeats[-1]

    def _acao_semantica_128(self):
        self._contexto = 'readln'

    def _acao_semantica_129(self, token):

        id = self._ts.find(token['token'])

        if self._contexto == 'readln':

            if self.is_variable(token):

                self._cod_intermediario.add(self._cod_intermediario.LEIT, '-', '-')

                self._cod_intermediario.add(self._cod_intermediario.ARMZ, self._nivel_atual, id.dado1)

                self._topo = self._topo + 1

        elif self._contexto == 'expressao':

            if id:
                if id.categoria == 'procedure' or id.categoria == 'rotulo':
                    raise Exception('Não é permitido usar nome de procedure')  # TODO colocar linha
                elif id.categoria == 'constante':
                    self._cod_intermediario.add(self._cod_intermediario.CRCT, '-', id.dado1)
                else:
                    self._cod_intermediario.add(self._cod_intermediario.CRVL, self._nivel_atual, id.dado1)
            else:
                raise Exception('Identificador "' + str(token['token']) + '" não foi declarado')  # TODO colocar linha


    def _acao_semantica_130(self, token):
        self._pilha_strings.append(token['token'])
        self._ponteiro_string = self._ponteiro_string + 1
        self._cod_intermediario.add(self._cod_intermediario.IMPRL, '-',  self._ponteiro_string)

        # TODO incrementa no. de ordem do literal

    def _acao_semantica_131(self):
        self._cod_intermediario.add(self._cod_intermediario.IMPR, '-', '-')

    def _acao_semantica_132(self):
        pass
        #raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_133(self):

        while len(self._pilha_case) > 0:
            self._pilha_case[-1]['operador2'] = self._cod_intermediario.getLc()
            del self._pilha_case[-1]

        self._cod_intermediario.add(self._cod_intermediario.AMEM, '-', -1)




    def _acao_semantica_134(self, token):

        self._cod_intermediario.add(self._cod_intermediario.COPI, '-', '-')
        self._cod_intermediario.add(self._cod_intermediario.CRCT, '-', token['token'])
        self._cod_intermediario.add(self._cod_intermediario.CMIG, '-', '-')

        if self._pilha_case[-1] and self._pilha_case[-1]['codigo'] == self._cod_intermediario.DSVT:
            self._pilha_case[-1]['operador2'] = self._cod_intermediario.getLc() + 1

            del self._pilha_case[-1]

        dsvt = self._cod_intermediario.add(self._cod_intermediario.DSVF, '-', 9999)
        self._pilha_case.append(dsvt)

    def _acao_semantica_135(self):

        self._pilha_case[-1]['operador2'] = self._cod_intermediario.getLc() + 1

        del self._pilha_case[-1]

        dsvt = self._cod_intermediario.add(self._cod_intermediario.DSVS, '-', 9999)
        self._pilha_case.append(dsvt)



    def _acao_semantica_136(self, token):

        self._cod_intermediario.add(self._cod_intermediario.COPI, '-', '-')
        self._cod_intermediario.add(self._cod_intermediario.CRCT, '-', token['token'])
        self._cod_intermediario.add(self._cod_intermediario.CMIG, '-', '-')

        dsvt = self._cod_intermediario.add(self._cod_intermediario.DSVT, '-', 9999)

        self._pilha_case.append(dsvt)

    def _acao_semantica_137(self, token):

        if self.is_variable(token):

            self._variavel_a_esquerda = self._ts.find(token['token'])

    def _acao_semantica_138(self):
        self._cod_intermediario.add(self._cod_intermediario.ARMZ, self._nivel_atual, self._variavel_a_esquerda.dado1)

    def _acao_semantica_139(self):

        self._pilha_fors.append(self._cod_intermediario.getLc())

        self._cod_intermediario.add(self._cod_intermediario.COPI, '-', '-')

        self._cod_intermediario.add(self._cod_intermediario.CRVL, self._nivel_atual, self._variavel_a_esquerda.dado1)

        self._cod_intermediario.add(self._cod_intermediario.CMAI, '-', '-')

        instrucao = self._cod_intermediario.add(self._cod_intermediario.DSVF, '-', 999)
        self._pilha_fors.append(instrucao)

        self._pilha_fors.append(self._variavel_a_esquerda)

    def _acao_semantica_140(self, token):

        self._cod_intermediario.add(self._cod_intermediario.CRVL, self._nivel_atual, self._pilha_fors[-1].dado1)

        # colocado constante valor 1 mesmo no CRCT, pq é o incremento do loop do FOR
        self._cod_intermediario.add(self._cod_intermediario.CRCT, '-', 1)

        self._cod_intermediario.add(self._cod_intermediario.SOMA, '-', '-')
        self._topo = self._topo + 2

        self._cod_intermediario.add(self._cod_intermediario.ARMZ, self._nivel_atual, self._pilha_fors[-1].dado1)

        self._pilha_fors[-2]['operador2'] = self._cod_intermediario.getLc() + 1

        self._cod_intermediario.add(self._cod_intermediario.DSVS, '-', self._pilha_fors[-3])

        self._cod_intermediario.add(self._cod_intermediario.AMEM, '-', -1)



    def _acao_semantica_141(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_142(self):
        self._cod_intermediario.add(self._cod_intermediario.CMMA, '-', '-')
        self._topo = self._topo + 2

    def _acao_semantica_143(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_144(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_145(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_146(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_147(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_148(self):
        self._cod_intermediario.add(self._cod_intermediario.SOMA, '-', '-')
        self._topo = self._topo + 2

    def _acao_semantica_149(self):
        self._cod_intermediario.add(self._cod_intermediario.SUBT, '-', '-')
        self._topo = self._topo + 2

    def _acao_semantica_150(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_151(self):
        self._cod_intermediario.add(self._cod_intermediario.MULT, '-', '-')
        self._topo = self._topo + 2

    def _acao_semantica_152(self):
        self._cod_intermediario.add(self._cod_intermediario.DIVI, '-', '-')
        self._topo = self._topo + 2

    def _acao_semantica_153(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_154(self, token):
        self._cod_intermediario.add(self._cod_intermediario.CRCT, '-', token['token'])
        self._topo = self._topo + 1

    def _acao_semantica_155(self):
        raise Exception('Falta desenvolver')  # TODO Falta desenvolver

    def _acao_semantica_156(self):
        self._contexto = 'expressao'
