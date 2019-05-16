from tkinter import *
from tkinter import scrolledtext
from src.analisador_lexico import AnalisadorLexico
from src.analisador_sintatico import AnalisadorSintatico
from src.gerador_codigo_intermediario import GeradorCodigoIntermediario


class Application:

    analisador_lexico = None
    root = None
    container_esquerdo = None

    btn_analise = None
    txt = None

    items_result = []

    def selectall(self, event):
        event.widget.tag_add("sel", "1.0", "end")

    def shortcut_run(self, event):
        self.click_analisar()

    def __init__(self, analisador_lexico: AnalisadorLexico, analisador_sintatico: AnalisadorSintatico):
        self.analisador_lexico = analisador_lexico
        self.analisador_sintatico = analisador_sintatico

    def start(self):

        self.root = Tk()
        self.root.bind_class("Text", "<Control-a>", self.selectall)
        self.root.bind_class("Text", "<Control-r>", self.shortcut_run)

        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))

        self.root.update_idletasks()
        self.root.update()

        container_principal = Frame(self.root)
        container_principal["padx"] = 50
        container_principal.pack()

        titulo = Label(container_principal, text="Compilador - Linguagem LMS")
        titulo["font"] = ("Arial", "15", "bold")
        titulo.pack()

        container_direito = Frame(container_principal)
        container_direito["pady"] = 10
        container_direito.pack(side=LEFT)

        container_meio = Frame(container_principal)
        container_meio["padx"] = 20
        container_meio.pack(side=LEFT)

        container_esquerdo = Frame(container_principal)
        container_esquerdo["padx"] = 20
        container_esquerdo.pack(side=LEFT)

        self.container_esquerdo = container_esquerdo

        self.txt = self.create_textarea(container_direito)

        self.btn_analise = Button(container_meio, text="Run >>>", fg="black", command=self.click_analisar)
        self.btn_analise.pack()

        #self.create_grid(container_esquerdo, [])

        self.refresh()

    def refresh(self):
        self.root.update_idletasks()
        self.root.update()

    def create_textarea(self, container):

        dica = Label(container, text="Atalho: Ctrl + r -> run")
        dica["font"] = ("Arial", "11")
        dica.grid()

        textarea = scrolledtext.ScrolledText(container, width=80, height=50, undo=True)
        textarea.grid(column=0, row=2)

        return textarea

    def create_grid(self, container, tokens: list):

        items = []
        label = Label(container, text="Código")
        label["font"] = ("Arial", "11")
        label.grid(row=0, column=0)

        items.append(label)

        label = Label(container, text="Token")
        label["font"] = ("Arial", "11")
        label.grid(row=0, column=1)

        items.append(label)

        label = Label(container, text="Descrição")
        label["font"] = ("Arial", "11")
        label.grid(row=0, column=2)

        items.append(label)

        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = Frame(container)
        frame_canvas.grid(row=2, column=0, columnspan=3)
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = Canvas(frame_canvas, bg="yellow")
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        # Create a frame to contain the buttons
        frame_buttons = Frame(canvas, bg="blue")
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

        tabela_tokens = [[Entry() for j in range(3)] for i in enumerate(tokens)]

        for i, token in enumerate(tokens):

            r = i + 1

            for j, valor in enumerate(token):  # Columns
                b = Entry(frame_buttons)
                b.insert(0, token[valor])
                items.append(b)
                b.grid(row=r, column=j, sticky='news')
                tabela_tokens[i][j] = b

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_buttons.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([tabela_tokens[0][j].winfo_width() for j in range(0, 3)])
        first5rows_height = sum([tabela_tokens[i][0].winfo_height() for i in range(0, 30)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(), height=first5rows_height)

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))

        self.items_result.append(frame_canvas)

    def create_grid_erro(self, container, erro):

        label = Label(container, text=erro, fg="red")
        label["font"] = ("Arial", "11")
        label.grid(columnspan=20)

        self.items_result.append(label)

    def create_grid_sucesso(self, container, msg):

        label = Label(container, text=msg, fg="green")
        label["font"] = ("Arial", "11")
        label.grid(columnspan=20)

        self.items_result.append(label)

    def click_analisar(self):

        self.analisador_lexico.clear()


        for widget in self.items_result:
            widget.destroy()

        code = self.txt.get("1.0", "end-1c")
        self.analisador_lexico.add_codigo('', code)

        try:
            tokens = self.analisador_lexico.analise()

            if tokens != None:
                for i in tokens:
                    print(i)
                print('======================================')

            gerador = GeradorCodigoIntermediario()

            self.analisador_sintatico.analise(tokens, gerador)
            self.create_grid_sucesso(self.container_esquerdo, 'Compilado com sucesso.')
        except Exception as e:
            self.create_grid_erro(self.container_esquerdo, e)







