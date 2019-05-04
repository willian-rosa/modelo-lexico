from src.analisador_lexico import AnalisadorLexico
from src.analisador_sintatico import AnalisadorSintatico


alexico = AnalisadorLexico()
asintatico = AnalisadorSintatico()

code = 'program classe; \
	var a:integer; \
begin \
a := 2; \
end.'

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




