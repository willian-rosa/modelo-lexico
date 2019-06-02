from src.interface import Application

from src.analisador_sintatico import AnalisadorSintatico
from src.gerador_codigo_intermediario import GeradorCodigoIntermediario


def analise(data_view):

    from src.analisador_lexico import AnalisadorLexico

    lexico = AnalisadorLexico()
    sintatico = AnalisadorSintatico()

    lexico.add_codigo('', data_view['code'])
    tokens = lexico.analise()

    data_view['tokens'] = tokens

    gerador = GeradorCodigoIntermediario()
    sintatico.analise(tokens, gerador)

    data_view['cod_inter'] = gerador._to_string()




app = Application(analise)
app.start()
app.root.mainloop()