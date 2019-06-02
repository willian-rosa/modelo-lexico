from src.analisador_lexico import AnalisadorLexico
from src.analisador_sintatico import AnalisadorSintatico
from src.gerador_codigo_intermediario import GeradorCodigoIntermediario


alexico = AnalisadorLexico()
asintatico = AnalisadorSintatico()




code = ''

code = 'PROGRAM TESTEPROC8; \
            VAR \
                CONT: INTEGER; \
            PROCEDURE P1; \
                    PROCEDURE P2; \
                    BEGIN \
                        WRITELN(CONT); \
                        CONT := CONT + 1; \
                        IF CONT < 5 THEN \
                            CALL P1; \
                    END; \
            BEGIN \
                CALL P2; \
            END; \
             \
            BEGIN \
                CONT := 0; \
                CALL P1; \
            END.'

alexico.clear()

tokens = None

try:
    alexico.add_codigo('', code)
    tokens = alexico.analise()
except Exception as e:
    print(e)


if tokens != None:
    # for i in tokens:
    #     print(i)
    # print('======================================')

    gerador = GeradorCodigoIntermediario()

    asintatico.analise(tokens, gerador)

    gerador.print()

# try:
#     pass
#
# except Exception as e:
#     print(e)




