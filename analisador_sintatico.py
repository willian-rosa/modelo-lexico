from analisador import Analisador
from analisador_lexico import AnalisadorLexico

class AnalisadorSintatico(Analisador):

    pilha = []

    def _get_in_parse(self, topo_pilha, codigo_token_entrada):

        producao = topo_pilha - self.c_inicio_nao_terminal

        return self.c_tabela_parse[producao][codigo_token_entrada-1]

    def _get_in_producao(self, topo_pilha, codigo_token_entrada):

        return self.c_producao[self._get_in_parse(topo_pilha,codigo_token_entrada)].copy()


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

    def analise(self, tokens: list):

        tokens.append(self.ct_fim_sentenca)

        # preparando tabela pilha de derivação
        self.pilha.append(self.ct_fim_sentenca)  # iniciando com o '$'
        self.pilha.append(self.c_inicio_nao_terminal)  # adicionando o <INICIO>

        # pegando ultimo elemento do array
        topo_pilha = self.pilha[-1]

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
            if topo_pilha < self.c_inicio_nao_terminal:

                # vefificando se é o token esperado
                if topo_pilha == token['codigo']:

                    # removendo o ultimo item da pilha
                    del self.pilha[-1]

                    # removendo primeiro item dos tokens
                    tokens.pop(0)
                else:
                    raise Exception('[ERRO SINTATICO]: '+self._gerar_msg_erro_sintaxe(topo_pilha, token))
            else:
                # topo não é terminal
                if self._get_in_parse(topo_pilha, token['codigo']) > -1:
                    producao = self._get_in_producao(topo_pilha, token['codigo'])

                    del self.pilha[-1]

                    # invertendo ordem da produção
                    producao.reverse()

                    # colocando produção na pilha
                    self.pilha = self.pilha + producao

                else:
                    raise Exception('[ERRO SINTATICO]: '+self._gerar_msg_erro_sintaxe(topo_pilha, token))


        print("compilado com  sucesso")
