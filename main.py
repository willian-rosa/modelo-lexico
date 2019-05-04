from src.analisador_lexico import AnalisadorLexico
from src.analisador_sintatico import AnalisadorSintatico
import glob
import time
from src.interface import Application


al = AnalisadorLexico()
sintatico = AnalisadorSintatico()

app = Application(al, sintatico)

# Abrindo diretamente o arquivos
# for path_file in glob.glob("code/*.pas"):
#     file = open(path_file, 'r')
#     al.add_codigo(path_file, file.read())

# al.analise()


app.start()



app.root.mainloop()

time.sleep(3)


