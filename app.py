from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://leomarcosos6440:<75869470leo.>@cluster0.kwlgaue.mongodb.net/?retryWrites=true&w=majority')
db = client['IBJV'] 
membros_collection = db['membros']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        membros_collection.insert_one({'nome': nome, 'email': email})

        return redirect(url_for('cadastro_sucesso'))

    return render_template('cadastro.html')

@app.route('/registro_membros')
def registro_membros():
    return render_template('registro_membros.html')

@app.route('/loga')
def loga():
    return render_template('loga.html')

@app.route('/cadastro_sucesso')
def cadastro_sucesso():
    return render_template('cadastro_sucesso.html')
if __name__ == '__main__':
    app.run(debug=True)