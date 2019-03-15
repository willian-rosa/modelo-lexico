from analizador_lexico import AnalizadorLexico
import glob
import time
from interface import Application


al = AnalizadorLexico()

app = Application(al)

# Abrindo diretamente o arquivos
# for path_file in glob.glob("code/*.pas"):
#     file = open(path_file, 'r')
#     al.add_codigo(path_file, file.read())

# al.analize()


app.start()



app.root.mainloop()

time.sleep(3)


