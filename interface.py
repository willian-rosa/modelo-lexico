from tkinter import *
from analisador_lexico import AnalisadorLexico
  
class Application:

    analisador_lexico = None
    root = None
    container_esquerdo = None

    btn_analise = None
    txt = None

    items_result = []

    def __init__(self, analisador_lexico: AnalisadorLexico):
        self.analisador_lexico = analisador_lexico

    def start(self):

        self.root = Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))

        self.root.update_idletasks()
        self.root.update()

        container_principal = Frame(self.root)
        container_principal["padx"] = 50
        container_principal.pack()

        titulo = Label(container_principal, text="Analisador Léxico")
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

        self.btn_analise = Button(container_meio, text="Analisar >>>", fg="black", command=self.click_analisar)
        self.btn_analise.pack()

        self.create_grid(container_esquerdo, [])

        self.refresh()

    def refresh(self):
        self.root.update_idletasks()
        self.root.update()

    def create_textarea(self, container):
        scroll = Scrollbar(container)
        textarea = Text(container, height=50, width=80)

        scroll.pack(side=RIGHT, fill=Y)
        textarea.pack(side=LEFT, fill=Y)
        scroll.config(command=textarea.yview)
        textarea.config(yscrollcommand=scroll.set)

        return textarea

    def create_grid(self, container, tokens:list):
        # {'codigo': 19, 'token': 'dsadas', 'descricao': 'Identificador'}
        # {'codigo': 2, 'token': '=', 'descricao': 'Sinal de Igualdade'}
        # {'codigo': 19, 'token': 'dasdas', 'descricao': 'Identificador'}
        self.rows = []

        for widget in self.items_result:
            widget.destroy()

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

        for i, token in enumerate(tokens):

            r = i + 1

            for j, valor in enumerate(token):  # Columns
                b = Entry(container)
                b.insert(0, token[valor])
                items.append(b)
                b.grid(row=r, column=j)

        self.items_result = items

    def create_grid_erro(self, container, erro):

        self.rows = []

        for widget in self.items_result:
            widget.destroy()

        items = []
        label = Label(container, text=erro, fg="red")
        label["font"] = ("Arial", "11")
        label.grid(row=0, column=0)

        items.append(label)

        self.items_result = items


    def click_analisar(self):

        self.analisador_lexico.clear()

        code = self.txt.get("1.0", "end-1c")
        self.analisador_lexico.add_codigo('', code)

        try:
            tokens = self.analisador_lexico.analise()
            print(tokens)
            print('---------------------')
            self.create_grid(self.container_esquerdo, tokens)
        except Exception as e:
            self.create_grid_erro(self.container_esquerdo, e)





