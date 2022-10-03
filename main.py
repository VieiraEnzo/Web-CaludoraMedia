from flask import Flask, request, render_template
import sqlite3

conn = sqlite3.connect("pf.db", check_same_thread=False)
c = conn.cursor()

app = Flask(__name__)

mediaf = 0
print(id(mediaf))

#tela login
def validasenha(dre,senha):

        senha_db = c.execute("SELECT senha FROM alunos WHERE dre = ?", (dre,)).fetchall()
        #oq ele retorna sem o fetchall e o local de memoria do "c" ou da senha?    
        if senha_db[0][0] == senha:
                return render_template("calculapf.html")
        else:
            return render_template("index.html", erro = "login incorreto")


def register(nome, senha, dre):

    logins = c.execute("SELECT dre FROM alunos")
    if dre in logins:

        return render_template("setup.html", erro = "usuario ja possui uma conta")

    else:

        c.execute("INSERT INTO alunos VALUES (?,?,?)", (dre,nome,senha,))
        conn.commit()
        return render_template("index.html")


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods = ["POST"])
def login():

    dre= request.form["dre"]
    senha= request.form["senha"]
    return validasenha(dre,senha)


@app.route("/setup", methods =["POST"])
def setup():
    nome = request.form["nome"]
    senha = request.form["senha"]
    dre = request.form["dre"]
    return register(nome,senha,dre)


@app.route("/tsetup")
def tela_setup():
    return render_template("setup.html")


def calcula_media(p1,p2):
    
    mediaf = (p1+p2)/2
    print(id(mediaf))

    if mediaf >= 7:
        return render_template("calculapf.html", mediaf = (p1+p2)/2, aprovado = 'Voce foi aprovado com media ')
    elif mediaf < 3:
        return render_template("calculapf.html", mediaf = (p1+p2)/2, reprovado = 'voce foi reprovado com media ')
    else:
        return render_template("final.html", mediaf = (p1+p2)/2)


@app.route("/media", methods = ["POST"])
def media():

    p1 = int(request.form["p1"])
    p2 = int(request.form["p2"])
    return calcula_media(p1,p2)


def calcula_final(p3):

    mediaf2 = (mediaf + p3)/2

    if mediaf2 >= 5: return render_template("aprovado.html", mediaf2 = (mediaf + p3)/2)

    else:  return render_template("reprovado.html", mediaf2 = (mediaf + p3)/2)


@app.route("/final", methods = ["POST"])
def end():

    p3 = int(request.form["p3"])
    return calcula_final(p3)


app.run()



