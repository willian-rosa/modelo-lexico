from src.analisador_lexico import AnalisadorLexico
from src.analisador_sintatico import AnalisadorSintatico
from src.gerador_codigo_intermediario import GeradorCodigoIntermediario


alexico = AnalisadorLexico()
asintatico = AnalisadorSintatico()

code = 'program classe; \
	        var x, y: integer; \
            begin \
                x := 123; \
                y := 456; \
                writeln(x, y) \
            end.'


code = 'program classe; \
	        var \
                a: integer; \
                b: integer; \
                c: integer; \
            begin \
                b := 1; \
                c := 2; \
                a := 3; \
            end.'

code = 'program classe; \
	        var \
                x: integer; \
            begin \
                x := 10 / 20; \
            end.'

code = 'program classe; \
	        var \
                x: integer; \
            begin \
                x := 10 + 20 * 30; \
            end.'

code = 'program classe; \
	        var \
                x: integer; \
            begin \
                x := 10 * 20 + 30; \
            end.'

code = 'program classe; \
	        var \
                x: integer; \
            begin \
                x := 123; \
                writeln(x); \
            end.'

code = 'program classe; \
	        var \
                x, y: integer; \
            begin \
                x := 123; \
                y := 465; \
                writeln(x, y); \
            end.'

code = 'program classe; \
	        var \
                x: integer; \
            begin \
                x := 123; \
                if x > 100 then \
                    writeln(1) \
                else \
                    writeln(0); \
            end.'

code = 'program classe; \
	        Const \
                a = 123; \
	        var \
                b: integer; \
            begin \
                writeln(a); \
                b := a + 1; \
            end.'

code = 'program classe; \
	        var \
                i: integer; \
            begin \
                while i > 10 do \
                begin; \
                    i := i - 1; \
                end; \
            end.'

code = 'program classe; \
	        var \
                i: integer; \
            begin \
                for i := 1 to 10 do \
                begin; \
                    writeln(20); \
                end; \
            end.'

code = 'program classe; \
	        Var \
				x : Integer; \
				Begin \
					Repeat  \
                        begin  \
                            readln(x);  \
                        end  \
					Until x > 10 \
            end.'
code = 'program classe; \
				Begin \
					Writeln("Hello"); \
					Writeln("Hello2"); \
            end.'
code = 'program classe; \
				var x : integer; \
				Begin \
					x := 123; \
					Writeln("Hello", x); \
            end.'

code = 'program classe; \
				var i : integer; \
				Begin \
					case i of \
                        10, 20: Writeln(11); \
                        30: Writeln(8) \
                     end \
            end.'

code = 'PROGRAM TESTEPROC1; \
        PROCEDURE PRINT(A,B:INTEGER); \
        BEGIN \
            WRITELN(77); \
        END; \
        \
        BEGIN \
            CALL PRINT(11,12); \
            END.'

code = 'PROGRAM TESTEPROC2; \
    PROCEDURE PRINT(A,B:INTEGER); \
    VAR I,J:INTEGER; \
    BEGIN \
        WRITELN(77); \
    END; \
    BEGIN \
        CALL PRINT(11,12); \
    END.'


code = 'PROGRAM TESTEPROC3; \
        PROCEDURE PRINT(A,B:INTEGER); \
        VAR I,J:INTEGER; \
        BEGIN \
            J := 55; \
        END; \
        BEGIN \
            CALL PRINT(11,12); \
        END.'





# code = 'PROGRAM TESTEPROC4; \
#         VAR X:INTEGER; \
#         PROCEDURE PRINT(A,B:INTEGER); \
#             VAR I,J:INTEGER; \
#         BEGIN \
#             X := 44; \
#         END; \
#         BEGIN \
#             CALL PRINT(11,12); \
#         END.'








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




