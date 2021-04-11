import pathlib, glob, re, markdown, markupsafe
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

directory = pathlib.Path.cwd() / 'contents/'
files = list(directory.glob('*.md'))

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/<file_selected>')
def open_file(file_selected):
    file_selected = directory / file_selected
    content = markdown.markdown(file_selected.read_text())
    return render_template('index.html', files=files, content=content)

'''
def parse_body(content):
    body = {}
    # parse front-matter (between "---") and store key, value in body
    fm_glob = re.split("-{3}", content)
    fm_dtl = re.findall(".*:.*", fm_glob[1])
    for item in fm_dtl:
        item_dtl = re.split(":", item)
        body[item_dtl[0]] = item_dtl[1].strip()
    # store text in body
    body['content'] = fm_glob[-1].strip()
    return body
'''