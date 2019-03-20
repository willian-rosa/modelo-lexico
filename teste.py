from analisador_lexico import AnalisadorLexico
from analisador_sintatico import AnalisadorSintatico


alexico = AnalisadorLexico()
asintatico = AnalisadorSintatico()

code = 'PROGRAM testeOperacoesMatematica; \
            VAR x, y, z :integer; \
        BEGIN \
            z:=1; \
            y:= 10; \
            READLN(x); \
            z:= (10+z+x) * y; \
            WRITELN(z); \
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

    asintatico.analise(tokens)
# try:
#     pass
#
# except Exception as e:
#     print(e)




