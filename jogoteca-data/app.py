from flask import Flask, render_template, request,redirect

class Jogo:
    def __init__(self, nome, categoria, console) -> str:
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo("Eve Online", "RPG Sandbox","PC")
jogo2 = Jogo("Hogwarts Legacy","RPG Action","PC/XBOX/PS4/PS5")
jogo3 = Jogo("Dota","MOBA","PC")
lista = [jogo1,jogo2,jogo3]



app = Flask(__name__)


@app.route('/')

def index():
    return render_template('lista.html', titulo="Jogos", jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome,categoria,console)
    lista.append(novo_jogo)
    return redirect('/')


app.run(host='localhost', port=8080, debug=True) 