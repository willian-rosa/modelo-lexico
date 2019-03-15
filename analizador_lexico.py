import sys


class AnalizadorLexico:

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

    def analize(self):

        for code in self.codes:
            self._analize_code(code['arquivo'], code['code'])
        return self.tabela_tokens

    def clear(self):
        self.tabela_tokens = []
        self.codes = []


    def _analize_code(self, arquivo, code):
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

            self._analize_caracter(arquivo, caracter)

        if self.estado == self.ESTADO_LITERAL:
            self.add_error('Final do arquivo inesperado, esperando simbolo \'"\' .', arquivo)
        elif self.estado != self.ESTADO_INICIAL:
            self.add_error('Erro no interpretador, estado atual: "'+self.estado+'".', arquivo)

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
            self.add_token(2, caracter, 'Sinal de Adição')
        elif caracter == '-':
            self.add_token(2, caracter, 'Sinal de Subtração')
        elif caracter == '*':
            self.add_token(2, caracter, 'Sinal de Multiplicação')
        elif caracter == '/':
            self.add_token(2, caracter, 'Sinal de Divisão')
        elif caracter == '=':
            self.add_token(2, caracter, 'Sinal de Igualdade')
        elif caracter == '>':
            self.estado = self.ESTADO_SINAL_MAIOR
        elif caracter == '<':
            self.estado = self.ESTADO_SINAL_MENOR
        elif caracter == ':':
            self.estado = self.ESTADO_SINAL_DOIS_PONTOS
        elif caracter == ';':
            self.add_token(14, caracter, 'Sinal de Ponto e Virgula')
        elif caracter == ',':
            self.add_token(15, caracter, 'Sinal de Virgula')
        elif caracter == '.':
            self.add_token(16, caracter, 'Sinal de Ponto')
        elif caracter == '(':
            self.estado = self.ESTADO_SINAL_ABREPAR
        elif caracter == ')':
            self.add_token(16, caracter, 'Sinal de Fecha Parêntese')
        elif caracter == ' ' or caracter == '\t' or caracter == '\r' or caracter == '\n':
            self.estado = self.ESTADO_INICIAL
        else:
            self.add_error('Simbolo inesperado \'' + caracter + '\'.', arquivo)

    def _analize_caracter(self, arquivo, caracter):

        if self.estado == self.ESTADO_INICIAL:
            self.define_estado_inicial(caracter, arquivo)

        # Literal
        elif self.estado == self.ESTADO_LITERAL:

            if caracter == '"':
                self.estado = self.ESTADO_INICIAL
                if len(self.coletor) > 255:
                    self.add_error('Literal excedeu 255 caracteres.', arquivo)
                else:
                    self.add_token(21, self.coletor, 'Literal')
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

                    # voltando a analizar o caracter terminal
                    self._analize_caracter(arquivo, caracter)
                elif len(self.coletor) > 30:
                    self.add_error('Idenficador atingiu tamanho maximo de 30 caracteres', arquivo)
                else:
                    self.estado = self.ESTADO_INICIAL
                    self.add_token(19, self.coletor, 'Identificador')

                    # voltando a analizar o caracter terminal
                    self._analize_caracter(arquivo, caracter)
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
                self.add_token(20, self.coletor, 'Inteiro')

                # voltando a analizar o caracter terminal
                self._analize_caracter(arquivo, caracter)
        elif self.estado == self.ESTADO_SINAL_MAIOR:
            if caracter == '=':
                self.add_token(8, '>=', 'Sinal de Maior/Igual')
                self.estado = self.ESTADO_INICIAL
            else:
                self.add_token(7, '>', 'Sinal de Maior')
                self.estado = self.ESTADO_INICIAL
                self._analize_caracter(arquivo, caracter)

        elif self.estado == self.ESTADO_SINAL_MENOR:
            if caracter == '=':
                self.add_token(10, '<=', 'Sinal de Menor/Igual')
                self.estado = self.ESTADO_INICIAL
            elif caracter == '>':
                self.add_token(11, '<>', 'Sinal de Diferente')
                self.estado = self.ESTADO_INICIAL
            else:
                self.add_token(9, '<', 'Sinal de Menor')
                self.estado = self.ESTADO_INICIAL
                self._analize_caracter(arquivo, caracter)

        elif self.estado == self.ESTADO_SINAL_DOIS_PONTOS:
            if caracter == '=':
                self.add_token(12, ':=', 'Sinal de Atribuição')
                self.estado = self.ESTADO_INICIAL
            else:
                self.add_token(13, ':', 'Sinal dois pontos')
                self.estado = self.ESTADO_INICIAL
                self._analize_caracter(arquivo, caracter)

        elif self.estado == self.ESTADO_SINAL_ABREPAR:
            if caracter == '*':
                self.estado = self.ESTADO_COMENTARIO
            else:
                self.add_token(17, '(', 'Sinal Abre Parêntese')
                self.estado = self.ESTADO_INICIAL

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
            'descricao': descricao
        })

    def add_error(self, msg, arquivo):
        raise Exception('ERRO FATAL: '+msg + ' Arquivo: ' + arquivo + ' - Linha: ' + str(self.linha) + ':' + str(self.coluna))

    def verifica_coletor_palavras_reservadas(self):
        coletor = self.coletor.lower()
        if coletor == 'program':
            return 22
        elif coletor == 'const':
            return 23
        elif coletor == 'var':
            return 24
        elif coletor == 'procedure':
            return 25
        elif coletor == 'begin':
            return 26
        elif coletor == 'end':
            return 27
        elif coletor == 'integer':
            return 28
        elif coletor == 'of':
            return 29
        elif coletor == 'call':
            return 30
        elif coletor == 'if':
            return 31
        elif coletor == 'then':
            return 32
        elif coletor == 'else':
            return 33
        elif coletor == 'while':
            return 34
        elif coletor == 'do':
            return 35
        elif coletor == 'repeat':
            return 36
        elif coletor == 'until':
            return 37
        elif coletor == 'readln':
            return 38
        elif coletor == 'writeln':
            return 39
        elif coletor == 'or':
            return 40
        elif coletor == 'and':
            return 41
        elif coletor == 'not':
            return 42
        elif coletor == 'for':
            return 43
        elif coletor == 'to':
            return 44
        elif coletor == 'case':
            return 45
        else:
            return None
