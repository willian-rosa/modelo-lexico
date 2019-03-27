class Analisador:
    ct_vazio = 0
    ct_fim_sentenca = 1

    ct_ponto_virgula = 2  # ";"
    ct_ponto = 3  # "."

    ct_virgula = 4  # ","
    ct_igualdade = 5  # "="
    ct_dois_pontos = 6  # ":"
    ct_abre_par = 7  # "("
    ct_fecha_par = 8  # ")"
    ct_atribuicao = 9  # ":="
    ct_sinal_maior = 10  # "<"
    ct_sinal_menor = 11  # ">"
    ct_sinal_maior_igual = 12  # ">="
    ct_sinal_menor_igual = 13  # "<="
    ct_sinal_diferente = 14  # "<>"
    ct_adicao = 15  # "+"
    ct_subtracao = 16  # "-"
    ct_multiplicacao = 17  # "*"
    ct_divisao = 18  # "/"

    ct_identificador = 19
    ct_inteiro = 20
    ct_literal = 21
    ct_program = 22
    ct_const = 23
    ct_var = 24
    ct_integer = 25
    ct_procedure = 26
    ct_begin = 27
    ct_call = 28
    ct_if = 29
    ct_then = 30
    ct_else = 31
    ct_while = 32
    ct_repeat = 33
    ct_until = 34
    ct_readln = 35
    ct_writeln = 36
    ct_case = 37
    ct_of = 38
    ct_end = 39
    ct_for = 40
    ct_to = 41
    ct_do = 42
    ct_or = 43
    ct_and = 44
    ct_not = 45
    
    c_inicio_nao_terminal = 46

    c_tabela_parse = [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 4, -1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, 6, -1, 6, 6, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, 8, -1, 8, 8, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, 10, 10, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, 12, 12, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, 15, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 16, -1, -1, -1, -1, 17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 18, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19, -1, -1, -1, -1, -1, -1],
        [-1, 25, -1, -1, -1, -1, 26, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, 25, -1, -1, 25, -1, -1, -1, -1, 25, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 28, -1, -1, -1, 27, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 30, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, 31, -1, -1, 30, -1, -1, -1, -1, 30, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 35, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 37, -1, -1, -1, 36, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 40, -1, -1, -1, -1, -1, -1, -1, 40, 40, -1, -1, 40, 40, 39, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 40],
        [-1, -1, -1, 42, -1, -1, -1, 41, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 44, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 45, -1, 46, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 48, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 47, -1, -1, -1, -1, -1, -1],
        [-1, 23, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 21, -1, -1, -1, -1, -1, -1, -1, 22, 24,
         29, -1, 23, 32, 33, 23, 34, 38, 43, -1, 23, 49, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 50, -1, -1, -1, -1, -1, -1, -1, 50, 50, -1, -1, 50, 50, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 50],
        [-1, 51, -1, 51, 52, -1, -1, 51, -1, 53, 54, 55, 56, 57, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, 51, 51, -1, -1, 51, -1, -1, -1, 51, 51, -1, 51, 51, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 60, -1, -1, -1, -1, -1, -1, -1, 58, 59, -1, -1, 60, 60, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 60],
        [-1, 64, -1, 64, 64, -1, -1, 64, -1, 64, 64, 64, 64, 64, 61, 62, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, 64, 64, -1, -1, 64, -1, -1, -1, 64, 64, -1, 64, 64, 63, -1, -1],
        [-1, -1, -1, -1, -1, -1, 65, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 65, 65, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 65],
        [-1, 66, -1, 66, 66, -1, -1, 66, -1, 66, 66, 66, 66, 66, 66, 66, 67, 68, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, 66, 66, -1, -1, 66, -1, -1, -1, 66, 66, -1, 66, 66, 66, 69, -1],
        [-1, -1, -1, -1, -1, -1, 71, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 73, 70, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 72]
    ]

    c_producao = [
        [22, 19, 2, 47, 3],
        [51, 53, 55, 57],
        [19, 49],
        [0],
        [4, 19, 49],
        [23, 19, 5, 20, 2, 50],
        [0],
        [19, 5, 20, 2, 50],
        [0],
        [24, 48, 6, 54, 2, 52],
        [0],
        [48, 6, 54, 2, 52],
        [0],
        [25],
        [26, 19, 56, 2, 47, 2, 55],
        [0],
        [0],
        [7, 48, 6, 25, 8],
        [27, 69, 58, 39],
        [0],
        [2, 69, 58],
        [19, 9, 70],
        [57],
        [0],
        [28, 19, 59],
        [0],
        [7, 70, 60, 8],
        [0],
        [4, 70, 60],
        [29, 70, 30, 69, 61],
        [0],
        [31, 69],
        [32, 70, 42, 69],
        [33, 69, 34, 70],
        [35, 7, 62, 63, 8],
        [19],
        [0],
        [4, 62, 63],
        [36, 7, 64, 65, 8],
        [21],
        [70],
        [0],
        [4, 64, 65],
        [37, 70, 38, 66, 39],
        [20, 67, 6, 69, 68],
        [4, 20, 67],
        [0],
        [0],
        [2, 66],
        [40, 19, 9, 70, 41, 70, 42, 69],
        [72, 71],
        [0],
        [5, 72],
        [10, 72],
        [11, 72],
        [12, 72],
        [13, 72],
        [14, 72],
        [15, 74, 73],
        [16, 74, 73],
        [74, 73],
        [15, 74, 73],
        [16, 74, 73],
        [43, 74, 73],
        [0],
        [76, 75],
        [0],
        [17, 76, 75],
        [18, 76, 75],
        [44, 76, 75],
        [20],
        [7, 70, 8],
        [45, 76],
        [62]
    ]

    # não coloquei todos erros, pq fica estranho a linguagem informar todas suas funcões
    c_msg_erro_complementar = [
        "Erro vazio???",
        "Era esperado fim de programa",
        "Era esperado \";\"",
        "Era esperado \".\"",
        "Era esperado \",\"",
        "Era esperado \"=\"",
        "Era esperado \":\"",
        "Era esperado \"(\"",
        "Era esperado \")\"",
        "Era esperado \":=\"",
        "Era esperado \"<\"",
        "Era esperado \">\"",
        "Era esperado \">=\"",
        "Era esperado \"<=\"",
        "Era esperado \"<>\"",
        "Era esperado \"+\"",
        "Era esperado \"-\"",
        "Era esperado \"*\"",
        "Era esperado \"/\"",
        "Era esperado identificador",
        "Era esperado INTEIRO",
        "Era esperado LITERAL",
        "Era esperado PROGRAM",
        "Era esperado CONST",
        "Era esperado VAR",
        "Era esperado INTEGER",
        "Era esperado PROCEDURE",
        "Era esperado BEGIN",
        "Era esperado CALL",
        "Era esperado IF",
        "Era esperado THEN",
        "Era esperado ELSE",
        "Era esperado WHILE",
        "Era esperado REPEAT",
        "Era esperado UNTIL",
        "Era esperado READLN",
        "Era esperado WRITELN",
        "Era esperado CASE",
        "Era esperado OF",
        "Era esperado END",
        "Era esperado FOR",
        "Era esperado TO",
        "Era esperado DO",
        "Era esperado OR",
        "Era esperado AND",
        "Era esperado NOT",
    ]


