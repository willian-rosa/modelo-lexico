from analizador_lexico import AnalizadorLexico
import glob


al = AnalizadorLexico()


for path_file in glob.glob("code/*.pas"):
    file = open(path_file, 'r')
    al.add_codigo(path_file, file.read())

al.analize()



