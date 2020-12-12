import os, glob, pathlib, re, datetime
from tkinter import *
from tkinter import font, ttk, messagebox

# tkinter application
window=Tk()

window.title("Machine à écrire du 'Markdown'")

def alert(msg):
    messagebox.askokcancel("Typewriter", msg)

def today():
    time = datetime.datetime.now()
    return time.strftime("%d-%m-%Y")

def path_content():
    return pathlib.Path.cwd()/'content/'

def parse_frontmatter(file_path, file_content):
    text = file_path.read_text()
    text_fm = re.split("-{3}", text)
    text_fm_dtl = re.findall(".*:.*", text_fm[1])
    for itm in text_fm_dtl:
        itm_dtl = re.split(":", itm)
        file_content[itm_dtl[0]] = itm_dtl[1].strip()
    file_content['text'] = text_fm[-1].strip()
    return file_content

def list_md():
    path = path_content()
    if path.exists():
        list_files = []
        for f in list(path.glob('*md')):
            list_files.append(f.stem)
        return list_files

def file_selected():
    idxs = list_doc.curselection()
    if idxs ==():
        return alert('fichier non sélectionné')
    else:
        return list_titles[idxs[0]]

def open_md():
    file_stem = file_selected()
    path = path_content()
    file_txt = read_md(path/'{}.md'.format(file_stem))
    update_screen(file_txt)

def read_md(file_path):
    file_content = {
        'file': file_path.stem,
    }
    md_content = parse_frontmatter(file_path, file_content)
    return md_content

def erase_screen():
    content.delete('1.0',END)
    file_entry.delete(0, END)
    title_entry.delete(0, END)
    publish_value.set(value='draft')

def update_screen(md_content):
    if content.compare("end-1c", "!=", "1.0"):
        alert("Le contenu en cours va être effacé")
        erase_screen()
    else:
        erase_screen()
    file_entry.insert(0, md_content['file'])
    title_entry.insert(0, md_content['title'])
    publish_value.set(value=md_content['status'])
    content.insert('1.0', md_content['text'])

def insert_frontmatter():
    date = today()
    front_matter = "---\ntitle: {}\nstatus: {}\ndate: {}\n---\n".format(title_entry.get(), publish_value.get(), date)
    content.insert('1.0', front_matter)

def create_filename():
    file_name = re.sub("\s", "-", file_text.get().strip())
    file_name = "{}.md".format(file_name)
    return file_name

def save():
    # message si fichier existe déjà
    insert_frontmatter()
    path = path_content()/create_filename()
    file_text = content.get('1.0', 'end')
    path.write_text(file_text)
    alert("enregistrement effectué")
    list_choices.set(list_md())

def delete():
    file_stem = file_selected()
    path = path_content()/"{}.md".format(file_stem)
    alert("le fichier {} va être supprimé".format(file_stem))
    path.unlink()
    list_choices.set(list_md())

# text content
contentframe = Frame(window)
contentframe.grid(column=0, row=0, sticky=(N, S, W, E))

contentFont = font.Font(family='Courier', size=18)
content = Text(contentframe, width=60, height=18, font=contentFont, padx=20, pady=20, borderwidth=1, relief=RAISED)
content.grid(column=0, row=0)

content_scroll = ttk.Scrollbar(window, orient=VERTICAL, command=content.yview)
content_scroll.grid(column=3, row=0, sticky=(N,S))
content['yscrollcommand'] =content_scroll.set

# list
listframe = ttk.Frame(window, padding=(16, 4, 4, 4))
listframe.grid(column=0, row=1, sticky=(N, S, W, E))

list_titles = list_md()
list_choices = StringVar(value=list_titles)
list_doc = Listbox(listframe, height=6, width=30, relief=FLAT, listvariable=list_choices)
list_doc.grid(row=0, column=0, columnspan=2, sticky=(W,E))

list_scroll = ttk.Scrollbar(listframe, orient=VERTICAL, command=list_doc.yview)
list_scroll.grid(column=2, row=0, sticky=(N,S))
list_doc['yscrollcommand'] =list_scroll.set

# title
titleframe = ttk.Frame(listframe, padding=(16, 4, 4, 4))
titleframe.grid(column=3, row=0, sticky=(N, S, W, E))

title_text=StringVar()
title_entry=ttk.Entry(titleframe, textvariable=title_text, width=28)
ttk.Label(titleframe, text="titre:").grid(row=0, column=0, sticky=(W))
title_entry.grid(row=0, column=1, sticky=(W))

file_text=StringVar()
file_entry=ttk.Entry(titleframe, textvariable=file_text, width=28)
ttk.Label(titleframe, text="fichier:").grid(row=1, column=0, sticky=(W))
file_entry.grid(row=1, column=1, sticky=(W))

publish_value=StringVar(value='draft')
publish_entry=ttk.Checkbutton(titleframe, variable=publish_value, onvalue='publish', offvalue='draft')
ttk.Label(titleframe, text="prêt pour publication:").grid(row=2, column=0, sticky=(E))
publish_entry.grid(row=2, column=1, sticky=(W))

# buttons
buttonframe = ttk.Frame(window, padding=(16, 4, 4, 4))
buttonframe.grid(column=0, row=2, sticky=(N, S, W, E))

ttk.Button(buttonframe,text='ouvrir', command=open_md, width=12).grid(row=3, column=0)
ttk.Button(buttonframe,text='supprimer', command=delete, width=12).grid(row=3, column=1)
ttk.Button(buttonframe,text='nettoyer', command=erase_screen, width=12).grid(row=3, column=2)
ttk.Button(buttonframe,text='enregistrer', command=save, width=12).grid(row=3, column=3, sticky=(W))

#minimal responsive
window.columnconfigure(0, weight=1)
contentframe.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(0, weight=2)

window.mainloop()