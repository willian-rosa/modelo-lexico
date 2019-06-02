from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext


class Application:

    root = None
    container_esquerdo = None
    txt = None
    txt_intermediario = None
    items_result = []
    fun_analise = None

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

    def create_textarea_pequeno(self, container, txt):
        textarea = scrolledtext.ScrolledText(container, width=60, height=10, undo=True)
        textarea.grid(columnspan=20)
        #textarea.insert(INSERT, txt)

        self.items_result.append(textarea)

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

            for j, valor in enumerate(['codigo', 'token', 'descricao']):  # Columns

                b = Entry(frame_buttons)
                b.insert(0, token[valor])
                items.append(b)
                b.grid(row=r, column=j, sticky='news')
                tabela_tokens[i][j] = b

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_buttons.update_idletasks()

        num_max = 15
        if len(tokens) < num_max:
            num_max = len(tokens)

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([tabela_tokens[0][j].winfo_width() for j in range(0, 3)])
        first5rows_height = sum([tabela_tokens[i][0].winfo_height() for i in range(0, num_max)])
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

        for widget in self.items_result:
            widget.destroy()

        code = self.txt.get("1.0", "end-1c")

        data_view = {}
        data_view['code'] = code

        msg_erro = None

        try:
            self.fun_analise(data_view)
        except Exception as e:
            msg_erro = e

        tokens_lexicos = []
        cod_inter = ''

        if 'tokens' in data_view:
            tokens_lexicos = data_view['tokens']

        if 'cod_inter' in data_view:
            cod_inter = data_view['cod_inter']



        self.create_grid(self.container_esquerdo, tokens_lexicos)

        if msg_erro == None:
            self.create_grid_sucesso(self.container_esquerdo, 'Compilado com sucesso.')
        else:
            self.create_grid_erro(self.container_esquerdo, msg_erro)

        self.create_textarea_pequeno(self.container_esquerdo, cod_inter)
