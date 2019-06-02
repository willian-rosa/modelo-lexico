from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext


class Application:

    root = None
    container_esquerdo = None
    txt = None
    txt_intermediario = None
    txt_exe = None
    fun_analise = None
    label_mensagem = None

    def __init__(self, fun_analise):
        self.fun_analise = fun_analise

    def selectall(self, event):
        event.widget.tag_add("sel", "1.0", "end")

    def shortcut_run(self, event):
        self.click_analisar()

    def start(self):

        self.root = Tk()
        self.root.bind_class("Text", "<Control-a>", self.selectall)
        self.root.bind_class("Text", "<Control-r>", self.shortcut_run)
        self.root.bind_class("Text", "<Control-Return>", self.shortcut_run)

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

        self.txt = self.create_textarea_code_lms(container_direito)

        Button(container_meio, text="Analisar Código", fg="black", command=self.click_analisar).pack()

        self.create_grid(container_esquerdo)

        self.refresh()

    def _load_file(self):

        path_file = filedialog.askopenfilename(
            initialdir="./fontes",
            title="Selecione o arquivo fonte",
            filetypes=(("Fonte LMS", "*.lms"), ("all files", "*.*"))
        )

        code = open(path_file, 'r').read()

        self.txt.delete('1.0', END)

        self.txt.insert(INSERT, code)

    def refresh(self):
        self.root.update_idletasks()
        self.root.update()

    def create_textarea_code_lms(self, container):

        Label(
            container,
            text="Atalhos:",
            font=("Arial", "11"),
            width=80,
            anchor=W,
            justify=LEFT
        ).grid()

        Label(
            container,
            text="Ctrl + r  ou Ctrl + Enter: analise",
            font=("Arial", "11"),
            width=80,
            anchor=W,
            justify=LEFT
        ).grid()

        Button(container, text="Abrir arquivo", fg="black", command=self._load_file).grid()

        textarea = scrolledtext.ScrolledText(container, width=80, height=45, undo=True)
        textarea.grid(column=0, row=3)

        return textarea

    def create_textarea_pequeno(self, container):
        textarea = scrolledtext.ScrolledText(container, width=80, height=10, undo=True)
        textarea.grid(columnspan=20)

        return textarea

    def create_grid(self, container):

        self.label_mensagem = Label(container, fg="green", font=("Arial", "11"))
        self.label_mensagem.grid(columnspan=3)

        Label(container, text="Código", font=("Arial", "11"), width=7, anchor=W, justify=LEFT).grid(row=1, column=0)
        Label(container, text="Token", font=("Arial", "11"), width=24, anchor=W, justify=LEFT).grid(row=1, column=1)
        Label(container, text="Descrição", font=("Arial", "11"), width=20, anchor=W, justify=LEFT).grid(row=1, column=2)

        self.txt_intermediario = self.create_textarea_pequeno(container)
        self.txt_exe = self.create_textarea_pequeno(container)

    def populate_grid(self, data_view):

        self.txt_intermediario.delete('1.0', END)
        self.txt_exe.delete('1.0', END)

        if 'tokens' in data_view:
            tokens = data_view['tokens']

            code = ''

            for token in tokens:

                token_codigo = str(token['codigo'])
                token_token = str(token['token'])
                token_descricao = str(token['descricao'])

                code = code + str(token_codigo) + self.generate_spaces(10, len(token_codigo))
                code = code + str(token_token)  + self.generate_spaces(25, len(token_token))
                code = code + token_descricao   + self.generate_spaces(45, len(token_descricao))

                code = code + "\n"

            self.txt_intermediario.insert(INSERT, code)

        if 'cod_inter' in data_view:
            cod_inter = data_view['cod_inter']
            self.txt_exe.insert(INSERT, cod_inter)

        pass

    @staticmethod
    def generate_spaces(limit, current_len):

        spaces = ''

        if current_len < limit:
            for i in range(limit - current_len):
                spaces = spaces + " "
        return spaces

    def print_mensagem(self, color, msg):
        self.label_mensagem['fg'] = color
        self.label_mensagem['text'] = msg

    def click_analisar(self):

        code = self.txt.get("1.0", "end-1c")

        data_view = {}
        data_view['code'] = code

        msg = None

        try:
            self.fun_analise(data_view)
            msg = 'Compilado com sucesso.'
            self.print_mensagem('green', 'Compilado com sucesso.')
        except Exception as e:
            self.print_mensagem('red', e)

        self.populate_grid(data_view)
