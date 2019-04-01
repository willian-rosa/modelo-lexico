from analisador import Analisador


class AnalisadorLexico(Analisador):

    ESTADO_INICIAL = 'inicial'
    ESTADO_LITERAL = 'literal'
    ESTADO_IDENTIFICADOR = 'identificador'
    ESTADO_INTEIRO = 'inteiro'
    ESTADO_SINAL_MULTIPLICACAO = 'sinal_multiplicacao'
    ESTADO_SINAL_MAIOR = 'sinal_maior'
    ESTADO_SINAL_MENOR = 'sinal_menor'
    ESTADO_SINAL_DOIS_PONTOS = 'sinal_dois_pontos'
    ESTADO_SINAL_ABREPAR = 'sinal_abrepar'
    ESTADO_COMENTARIO = 'comentario'
    ESTADO_COMENTARIO_FECHANDO = 'comentario_fechando'

    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    linha = 1
    coluna = 1
    estado = None
    coletor = ''
    tabela_tokens = []
    codes = []
    palavras_resevadas = []

    def add_codigo(self, path_file, code):
        # TODO fazer indeficação se é ultimo caracter no arquivo
        code = code+' '

        self.codes.append({
            "arquivo": path_file,
            "code": code
        })

    def analise(self):

        for code in self.codes:
            self._analise_code(code['arquivo'], code['code'])
        return self.tabela_tokens

    def clear(self):
        self.tabela_tokens = []
        self.codes = []

    def _analise_code(self, arquivo, code):

        self.linha = 1
        self.coluna = 1

        self.estado = self.ESTADO_INICIAL

        for caracter in code:

            # Controlador de linhas e coluna

            if caracter == "\n":
                self.linha = self.linha + 1
                self.coluna = 1
            else:
                self.coluna = self.coluna + 1

            self._analise_caracter(arquivo, caracter)

        if self.estado == self.ESTADO_LITERAL:
            self.add_error('Final do arquivo inesperado, esperando simbolo \'"\' .', arquivo)
        elif self.estado != self.ESTADO_INICIAL:
            self.add_error('Erro no interpretador, estado atual: "'+self.estado+'".', arquivo)

        self.add_token(self.ct_fim_sentenca, '$', 'Fim de sentença')

    def define_estado_inicial(self, caracter, arquivo):
        self.coletor = ''

        # Iniciando estado
        if caracter == '"':
            self.estado = self.ESTADO_LITERAL
        elif self.letras.count(caracter):
            self.estado = self.ESTADO_IDENTIFICADOR
            self.coletor = caracter
        elif self.numeros.count(caracter):
            self.estado = self.ESTADO_INTEIRO
            self.coletor = caracter
        elif caracter == '+':
            self.add_token(self.ct_adicao, caracter, 'Sinal de Adição')
        elif caracter == '-':
            self.add_token(self.ct_subtracao, caracter, 'Sinal de Subtração')
        elif caracter == '*':
            self.add_token(self.ct_multiplicacao, caracter, 'Sinal de Multiplicação')
        elif caracter == '/':
            self.add_token(self.ct_divisao, caracter, 'Sinal de Divisão')
        elif caracter == '=':
            self.add_token(self.ct_igualdade, caracter, 'Sinal de Igualdade')
        elif caracter == '>':
            self.estado = self.ESTADO_SINAL_MAIOR
        elif caracter == '<':
            self.estado = self.ESTADO_SINAL_MENOR
        elif caracter == ':':
            self.estado = self.ESTADO_SINAL_DOIS_PONTOS
        elif caracter == ';':
            self.add_token(self.ct_ponto_virgula, caracter, 'Sinal de Ponto e Virgula')
        elif caracter == ',':
            self.add_token(self.ct_virgula, caracter, 'Sinal de Virgula')
        elif caracter == '.':
            self.add_token(self.ct_ponto, caracter, 'Sinal de Ponto')
        elif caracter == '(':
            self.estado = self.ESTADO_SINAL_ABREPAR
        elif caracter == ')':
            self.add_token(self.ct_fecha_par, caracter, 'Sinal de Fecha Parêntese')
        elif caracter == ' ' or caracter == '\t' or caracter == '\r' or caracter == '\n':
            self.estado = self.ESTADO_INICIAL
        else:
            self.add_error('Simbolo inesperado \'' + caracter + '\'.', arquivo)

    def _analise_caracter(self, arquivo, caracter):

        if self.estado == self.ESTADO_INICIAL:
            self.define_estado_inicial(caracter, arquivo)

        # Literal
        elif self.estado == self.ESTADO_LITERAL:

            if caracter == '"':
                self.estado = self.ESTADO_INICIAL
                if len(self.coletor) > 255:
                    self.add_error('Literal excedeu 255 caracteres.', arquivo)
                else:
                    self.add_token(self.ct_literal, self.coletor, 'Literal')
            else:
                self.coletor = self.coletor + caracter

        # Identificador
        elif self.estado == self.ESTADO_IDENTIFICADOR:

            if self.letras.count(caracter) or self.numeros.count(caracter):
                self.coletor = self.coletor + caracter
            else:
                is_palavra_reservada = self.verifica_coletor_palavras_reservadas()

                # Palavra Reservada
                if is_palavra_reservada is not None: # palavras reservadas
                    self.estado = self.ESTADO_INICIAL
                    self.add_token(is_palavra_reservada, self.coletor, 'Palavra Reservada')

                    # voltando a analisar o caracter terminal
                    self._analise_caracter(arquivo, caracter)
                elif len(self.coletor) > 30:
                    self.add_error('Idenficador atingiu tamanho maximo de 30 caracteres', arquivo)
                else:
                    self.estado = self.ESTADO_INICIAL
                    self.add_token(self.ct_identificador, self.coletor, 'Identificador')

                    # voltando a analisar o caracter terminal
                    self._analise_caracter(arquivo, caracter)
        elif self.estado == self.ESTADO_INTEIRO:
            if self.numeros.count(caracter):
                self.coletor = self.coletor + caracter
            elif self.letras.count(caracter):
                self.add_error('Declaração de inteiro invalida', arquivo)
            elif caracter == '.':
                self.add_error('Valores reais não são permitidos', arquivo)
            elif int(self.coletor) >= 32767 or int(self.coletor) <= -32767:
                self.add_error('Valor inteiro ('+self.coletor+') fora da escala', arquivo)
            else:
                self.estado = self.ESTADO_INICIAL
                self.add_token(self.ct_inteiro, self.coletor, 'Inteiro')

                # voltando a analisar o caracter terminal
                self._analise_caracter(arquivo, caracter)
        elif self.estado == self.ESTADO_SINAL_MAIOR:
            if caracter == '=':
                self.add_token(self.ct_sinal_maior_igual, '>=', 'Sinal de Maior/Igual')
                self.estado = self.ESTADO_INICIAL
            else:
                self.add_token(self.ct_sinal_maior, '>', 'Sinal de Maior')
                self.estado = self.ESTADO_INICIAL
                self._analise_caracter(arquivo, caracter)

        elif self.estado == self.ESTADO_SINAL_MENOR:
            if caracter == '=':
                self.add_token(self.ct_sinal_menor_igual, '<=', 'Sinal de Menor/Igual')
                self.estado = self.ESTADO_INICIAL
            elif caracter == '>':
                self.add_token(self.ct_sinal_diferente, '<>', 'Sinal de Diferente')
                self.estado = self.ESTADO_INICIAL
            else:
                self.add_token(self.ct_sinal_menor, '<', 'Sinal de Menor')
                self.estado = self.ESTADO_INICIAL
                self._analise_caracter(arquivo, caracter)

        elif self.estado == self.ESTADO_SINAL_DOIS_PONTOS:
            if caracter == '=':
                self.add_token(self.ct_atribuicao, ':=', 'Sinal de Atribuição')
                self.estado = self.ESTADO_INICIAL
            else:
                self.add_token(self.ct_dois_pontos, ':', 'Sinal dois pontos')
                self.estado = self.ESTADO_INICIAL
                self._analise_caracter(arquivo, caracter)

        elif self.estado == self.ESTADO_SINAL_ABREPAR:
            if caracter == '*':
                self.estado = self.ESTADO_COMENTARIO
            else:
                self.add_token(self.ct_abre_par, '(', 'Sinal Abre Parêntese')
                self.estado = self.ESTADO_INICIAL
                self._analise_caracter(arquivo, caracter)

        elif self.estado == self.ESTADO_COMENTARIO and caracter == '*':
            self.estado = self.ESTADO_COMENTARIO_FECHANDO

        elif self.estado == self.ESTADO_COMENTARIO_FECHANDO:
            if caracter == ')':
                self.estado = self.ESTADO_INICIAL
            elif caracter != '*':
                self.estado = self.ESTADO_COMENTARIO

    def add_token(self, codigo_token, valor, descricao):
        self.tabela_tokens.append({
            'codigo': codigo_token,
            'token': valor,
            'descricao': descricao,
            'linha': self.linha,
            'coluna': self.coluna,
        })

    def add_error(self, msg, arquivo):
        raise Exception('ERRO FATAL: '+msg + ' Arquivo: ' + arquivo + ' - Linha: ' + str(self.linha) + ':' + str(self.coluna))

    def verifica_coletor_palavras_reservadas(self):
        coletor = self.coletor.lower()
        if coletor == 'program':
            return self.ct_program
        elif coletor == 'const':
            return self.ct_const
        elif coletor == 'var':
            return self.ct_var
        elif coletor == 'procedure':
            return self.ct_procedure
        elif coletor == 'begin':
            return self.ct_begin
        elif coletor == 'end':
            return self.ct_end
        elif coletor == 'integer':
            return self.ct_integer
        elif coletor == 'of':
            return self.ct_of
        elif coletor == 'call':
            return self.ct_call
        elif coletor == 'if':
            return self.ct_if
        elif coletor == 'then':
            return self.ct_then
        elif coletor == 'else':
            return self.ct_else
        elif coletor == 'while':
            return self.ct_while
        elif coletor == 'do':
            return self.ct_do
        elif coletor == 'repeat':
            return self.ct_repeat
        elif coletor == 'until':
            return self.ct_until
        elif coletor == 'readln':
            return self.ct_readln
        elif coletor == 'writeln':
            return self.ct_writeln
        elif coletor == 'or':
            return self.ct_or
        elif coletor == 'and':
            return self.ct_and
        elif coletor == 'not':
            return self.ct_not
        elif coletor == 'for':
            return self.ct_for
        elif coletor == 'to':
            return self.ct_to
        elif coletor == 'case':
            return self.ct_case
        else:
            return None
