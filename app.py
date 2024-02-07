
# from __future__ import print_function # In python 2.7
from flask import Flask

app = Flask(__name__)

@app.route('/presentacion/datos/personales/<nombre>/<apellido>/<numero>')
def index(nombre, apellido, numero):
    c = ""
    for i in range(0,int(numero)):
        c = '%s<b>%s %s</b><br/>' % (c, nombre, apellido)

    return c

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
