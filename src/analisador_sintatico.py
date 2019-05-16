from src.analisador import Analisador
from src.analisador_semantico import AnalisadorSemantico

class AnalisadorSintatico(Analisador):

    pilha = []

    analisador_semantico = None

    # pega item na tabela de parse
    def _get_in_parse(self, topo_pilha, codigo_token_entrada):

        producao = topo_pilha - self.c_inicio_nao_terminal

        return self.c_tabela_parse[producao][codigo_token_entrada-1]

    def _get_in_producao(self, topo_pilha, codigo_token_entrada):

        return self.c_producao[self._get_in_parse(topo_pilha, codigo_token_entrada)].copy()


    def _gerar_msg_erro_sintaxe(self, topo_pilha, token):

        # pegando mensagem com base no token não reconhecido e o que deveria ser escrito
        # exemplo escrever 'prog' em vez de 'program'
        if topo_pilha >= self.c_inicio_nao_terminal:
            parse = self.c_tabela_parse[topo_pilha - self.c_inicio_nao_terminal]
            producao = list(x for x in parse if x > -1).copy().pop(0)

            topo_pilha = self.c_producao[producao].copy().pop(0)

        msg = ''
        # ignorando mensagem sem sentido
        if token['token'] != '$':
            msg = 'Não era esperado "'+token['token']+'". '

        # complentando mensagem com base no que se espera de token
        # between entre 0 e max de mensagens
        if 0 < topo_pilha < len(self.c_msg_erro_complementar):
            msg = msg + self.c_msg_erro_complementar[topo_pilha] + '.'

        # colocando informação de linha e coluna do token com erro
        msg = msg + ' Na linha ' + str(token['linha']) + ":" + str(token['coluna'])

        return msg

    def _tratar_acao_semantica(self, topo_pilha, token_nao_terminal_atual):

        numero_acao_semantica = topo_pilha - self.c_inicio_acoes_semantica

        print("tratando acao de código: " + str(numero_acao_semantica))

        self.analisador_semantico.executeAcao(numero_acao_semantica, token_nao_terminal_atual)

    def analise(self, tokens: list, gerador_codigo):

        self.analisador_semantico = AnalisadorSemantico(gerador_codigo)

        tokens.append(self.ct_fim_sentenca)

        # preparando tabela pilha de derivação
        self.pilha.append(self.ct_fim_sentenca)  # iniciando com o '$'
        self.pilha.append(self.c_inicio_nao_terminal)  # adicionando o <INICIO>

        # pegando ultimo elemento do array
        topo_pilha = self.pilha[-1]

        # É necessario para passar para o semantico, o token não terminal atual
        # lá vai conseguir salvar na TS esse token.
        token_nao_terminal_atual = None

        # vai repetir até o momento que o topo da pilha for $
        while topo_pilha != self.ct_fim_sentenca:

            # pegando ultimo elemento do array
            topo_pilha = self.pilha[-1]

            if topo_pilha == self.ct_vazio:
                del self.pilha[-1]
                continue

            # token de entrada atual
            token = tokens[0]

            # se topo é terminal ou $
            # caso o token é menor que 46
            if topo_pilha < self.c_inicio_nao_terminal:

                # vefificando se é o token esperado
                if topo_pilha == token['codigo']:

                    # removendo o ultimo item da pilha
                    del self.pilha[-1]

                    # removendo primeiro item dos tokens
                    tokens.pop(0)

                    # o token não terminal para passar para o analisador semantico
                    token_nao_terminal_atual = token


                else:
                    raise Exception('[ERRO SINTATICO]: '+self._gerar_msg_erro_sintaxe(topo_pilha, token))

            # vai executar se p token atual é uma regra de produção, ou seja o token esta entre [46 e 77[
            # 77 esta fora pq já é uma ação semantica
            elif self.c_inicio_nao_terminal <= topo_pilha < self.c_inicio_acoes_semantica:

                # topo não é terminal
                if self._get_in_parse(topo_pilha, token['codigo']) > -1:
                    producao = self._get_in_producao(topo_pilha, token['codigo'])

                    # removendo o topo da pilha de tokens
                    del self.pilha[-1]

                    # invertendo ordem da produção
                    producao.reverse()

                    # colocando produção na pilha
                    self.pilha = self.pilha + producao

                else:
                    raise Exception('[ERRO SINTATICO]: ' + self._gerar_msg_erro_sintaxe(topo_pilha, token))

            else:

                self._tratar_acao_semantica(topo_pilha, token_nao_terminal_atual)

                # removendo o topo da pilha de tokens
                del self.pilha[-1]

                # raise Exception('[ERRO SEMANTICO]: ')


        print("compilado com  sucesso")
