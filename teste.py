from analisador_lexico import AnalisadorLexico
from analisador_sintatico import AnalisadorSintatico


alexico = AnalisadorLexico()
asintatico = AnalisadorSintatico()

code = 'program \
            begin \
                readln( x ); \
                writeln( y ); \
            end.'

alexico.clear()

alexico.add_codigo('', code)

tokens = alexico.analise()

for i in tokens:
    print(i)
print('======================================')

asintatico.analise(tokens)

print('---------------------')