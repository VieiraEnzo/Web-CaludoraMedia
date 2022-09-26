
@app.route("/media", methods = ["POST"])
def media():
    p1 = int(request.form["p1"])
    p2 = int(request.form["p2"])
    return calcula_media(p1,p2)


@app.route("/final", methods = ["POST"])
def end():
    p3 = int(request.form["p3"])
    return calcula_final(mediaf,p3)

def calcula_final(p3):
    mediaf2 = (mediaf + p3)/2
    if mediaf2 >= 5: render_template("aprovado.html", mediaf2)