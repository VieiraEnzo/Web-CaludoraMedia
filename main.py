from flask import Flask, request, render_template

app = Flask(__name__)

mediaf = 0
#tela logiin
def validasenha(nome,senha):

    with open("senha.txt", 'r') as f:

        line = f.readlines()

        usuario = nome +':'+ senha + '\n'

        if usuario in line:
                return render_template("calculapf.html")
        else:
            return render_template("index.html", erro = "login incorreto")
        

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods = ["POST"])
def login():

    nome= request.form["nome"]
    senha= request.form["senha"]
    return validasenha(nome,senha)


def calcula_media(p1,p2):

    mediaf = (p1+p2)/2

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