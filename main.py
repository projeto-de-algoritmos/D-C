from cgitb import html
from re import I
from tkinter.messagebox import QUESTION
from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)  # sempre ao iniciar um site
app.config['SECRET_KEY'] = "HASH"


def merge_and_count(left, right):
    result = list()
    i, j = 0, 0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return result, inv_count


def sort_and_count(array):
    if len(array) <= 1:
        return array, 0
    meio = len(array) // 2
    left, inv_left = sort_and_count(array[:meio])
    right, inv_right = sort_and_count(array[meio:])
    merged, count = merge_and_count(left, right)
    count += (inv_left + inv_right)
    return merged, count


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        listaDePreferencias = []
        listaDePreferencias.append(request.form["question1"])
        listaDePreferencias.append(request.form["question2"])
        listaDePreferencias.append(request.form["question3"])
        listaDePreferencias.append(request.form["question4"])
        listaDePreferencias.append(request.form["question5"])
        merge_array, parecer = sort_and_count(listaDePreferencias)
        n = len(listaDePreferencias)
        repetidor = 0
        for i in range(0, n-1):
            for j in range(i+1, n-1):
                if listaDePreferencias[i] == listaDePreferencias[j]:
                    repetidor += 1
        if repetidor > 0:
            flash('Todos os campos devem ser dierentes')
            return redirect(url_for('homepage'))
        if parecer == 0:
            return redirect(url_for("animador"))
        if parecer > 0 and parecer < 4:
            return redirect(url_for("inovador"))
        if parecer > 3 and parecer < 6:
            return redirect(url_for("mediador"))
        if parecer > 5 and parecer < 9:
            return redirect(url_for("empresario"))
        if parecer > 8 and parecer <= 10:
            return redirect(url_for("consul"))

    else:
        return render_template("homepage.html")


@app.route('/animador')
def animador():
    return render_template("animador.html")


@app.route('/inovador')
def inovador():
    return render_template("inovador.html")


@app.route('/mediador')
def mediador():
    return render_template("mediador.html")


@app.route('/Empresário')
def empresario():
    return render_template("empresario.html")


@app.route('/consul')
def consul():
    return render_template("consul.html")


if __name__ == "__main__":
    app.run(debug=True)
