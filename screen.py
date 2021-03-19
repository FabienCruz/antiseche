from tkinter import *
from tkinter import font, ttk
import service, file, sitegenerator

class Screen:
    def __init__(self, window, directory, extension):
        
        self.directory = directory
        self.extension = extension

        window.title("Machine à écrire du 'Markdown'")

        # text content
        txtframe = Frame(window)
        txtframe.grid(column=0, row=0, sticky=(N, S, W, E))

        txtFont = font.Font(family='Courier', size=18)
        self.txt = Text(txtframe, width=60, height=18, font=txtFont, padx=20, pady=20, borderwidth=1, relief=RAISED)
        self.txt.grid(column=0, row=0)

        txt_scroll = ttk.Scrollbar(window, orient=VERTICAL, command=self.txt.yview)
        txt_scroll.grid(column=3, row=0, sticky=(N,S))
        self.txt['yscrollcommand'] =txt_scroll.set

        # list from files
        listframe = ttk.Frame(window, padding=(16, 4, 4, 4))
        listframe.grid(column=0, row=1, sticky=(N, S, W, E))

        self.list_titles = self.directory.list_files(self.extension)
        self.list_choices = StringVar(value=self.list_titles)
        self.list_doc = Listbox(listframe, height=6, width=30, relief=FLAT, listvariable=self.list_choices)
        self.list_doc.grid(row=0, column=0, columnspan=2, sticky=(W,E))

        list_scroll = ttk.Scrollbar(listframe, orient=VERTICAL, command=self.list_doc.yview)
        list_scroll.grid(column=2, row=0, sticky=(N,S))
        self.list_doc['yscrollcommand'] =list_scroll.set

        # title
        titleframe = ttk.Frame(listframe, padding=(16, 4, 4, 4))
        titleframe.grid(column=3, row=0, sticky=(N, S, W, E))

        self.title_text=StringVar()
        title_entry=ttk.Entry(titleframe, textvariable=self.title_text, width=28)
        ttk.Label(titleframe, text="titre:").grid(row=0, column=0, sticky=(W))
        title_entry.grid(row=0, column=1, sticky=(W))

        self.file_name=StringVar()
        file_entry=ttk.Entry(titleframe, textvariable=self.file_name, width=28)
        ttk.Label(titleframe, text="fichier:").grid(row=1, column=0, sticky=(W))
        file_entry.grid(row=1, column=1, sticky=(W))

        self.publish_value=StringVar(value='draft')
        publish_entry=ttk.Checkbutton(titleframe, variable=self.publish_value, onvalue='publish', offvalue='draft')
        ttk.Label(titleframe, text="prêt pour publication:").grid(row=2, column=0, sticky=(E))
        publish_entry.grid(row=2, column=1, sticky=(W))

        # buttons
        buttonframe = ttk.Frame(window, padding=(16, 4, 4, 4))
        buttonframe.grid(column=0, row=2, sticky=(N, S, W, E))

        ttk.Button(buttonframe,text='ouvrir', command=self.open, width=12).grid(row=3, column=0)
        ttk.Button(buttonframe,text='supprimer', command=self.delete, width=12).grid(row=3, column=1)
        ttk.Button(buttonframe,text='nouveau', command=self.new, width=12).grid(row=3, column=2)
        ttk.Button(buttonframe,text='publier', command=self.publish, width=12).grid(row=3, column=3, sticky=(W))
        ttk.Button(buttonframe,text='enregistrer', command=self.save, width=12).grid(row=3, column=4, sticky=(W))

        #minimal responsive
        window.columnconfigure(0, weight=1)
        txtframe.columnconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(0, weight=2)
    
    # buttons actions

    def selected(self):
        index = self.list_doc.curselection()
        if index ==():
            service.alert('fichier non sélectionné')
        else:
            file_stem = self.list_titles[index[0]]
            full_path = self.directory.path / '{}{}'.format(file_stem, self.extension)
            return file.File(full_path)

    def update_list(self):
        self.list_titles = self.directory.list_files(self.extension)
        self.list_choices.set(self.directory.list_files(self.extension))

    def is_screen_empty(self):
        return self.txt.compare("end-1c", "==", "1.0") or service.alert("Le contenu en cours va être effacé")

    def erase_screen(self):
        self.txt.delete('1.0', 'end')
        self.file_name.set(value='')
        self.title_text.set(value='')
        self.publish_value.set(value='draft')

    def display(self, name, body):
        self.file_name.set(value=name)
        self.title_text.set(value=body['title'])
        self.publish_value.set(value=body['status'])
        self.txt.insert('1.0', body['text'])

    def new(self):
        if self.is_screen_empty(): self.erase_screen()
        
    def open(self):
        if self.is_screen_empty():
            self.erase_screen()
            file_selected = self.selected()
            file_selected.parse_body(file_selected.full_path.read_text())
            self.display(file_selected.full_path.stem, file_selected.body)

    def delete(self):
        file_selected = self.selected()
        if service.alert("le fichier {} va être supprimé".format(file_selected.full_path.stem)):
            file_selected.full_path.unlink()
            self.update_list()
            self.erase_screen()

    def normalize_filename(self, exts):
        if self.file_name == '':
            service.info("Le fichier n'a pas de nom")
        else:
            f_name = re.sub("\s", "-", self.file_name.get().strip())
            f_name = "{}{}".format(f_name, exts)
            return f_name

    def new_file(self, dir, exts):
        n_file = self.normalize_filename(exts)
        return self.directory.path / n_file

    def create_file(self):
        new_f = self.new_file(self.directory, self.extension)
        self.insert_frontmatter()
        new_f.write_text(self.txt.get('1.0', 'end'))
        new_f = file.File(new_f)
        new_f.parse_body(new_f.full_path.read_text())
        return new_f

    def insert_frontmatter(self):
        front_matter = "---\ntitle: {}\nstatus: {}\ndate: {}\n---\n".format(self.title_text.get(), self.publish_value.get(), service.today())
        self.txt.insert('1.0', front_matter)

    def save(self):
        name = self.file_name.get()
        if name == '':
            return service.info("Le fichier n'a pas de nom")
        else:
            self.insert_frontmatter()
            content = self.txt.get('1.0', 'end')
            file.File.save_file(self, self.directory, name, self.extension, content)
            self.update_list()
    
    # gestion des fichiers html

    def publish(self):
        sitegenerator.generate(self)