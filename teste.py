from src.analisador_lexico import AnalisadorLexico
from src.analisador_sintatico import AnalisadorSintatico
from src.gerador_codigo_intermediario import GeradorCodigoIntermediario


alexico = AnalisadorLexico()
asintatico = AnalisadorSintatico()




code = ''

code = 'PROGRAM TESTEPROC4; \
        VAR X:INTEGER; \
        PROCEDURE PRINT(A,B:INTEGER); \
            VAR I,J:INTEGER; \
        BEGIN \
            X := 44; \
        END; \
        BEGIN \
            CALL PRINT(11,12); \
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




