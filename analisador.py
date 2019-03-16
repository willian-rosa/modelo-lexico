class Analisador:
    ct_vazio = 0
    ct_fim_sentenca = 1

    ct_abre_par = 2  # "("
    ct_fecha_par = 3  # ")"
    ct_ponto_virgula = 4  # ";"
    ct_ponto = 5  # "."
    ct_identificador = 6
    ct_inteiro = 7
    ct_program = 8
    ct_begin = 9
    ct_end = 10
    ct_readln = 11
    ct_writeln = 12
    
    c_inicio_nao_terminal = 13

    c_tabela_parse = [
        [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, 3],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 5, 4, 4]
    ]

    c_producao = [
        [8, 14, 5],
        [9, 15, 16, 10],
        [11, 2, 6, 3, 4],
        [12, 2, 6, 3, 4],
        [15],
        [0]
    ]





