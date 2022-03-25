from cgitb import html
from tkinter.messagebox import QUESTION
from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)  # sempre ao iniciar um site


def count_inversion(lst):
    return merge_count_inversion(lst)[1]


def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int(len(lst) / 2)
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)


def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        listaDePreferencias = []
        listaDePreferencias.append(request.form["question1"])
        listaDePreferencias.append(request.form["question2"])
        listaDePreferencias.append(request.form["question3"])
        listaDePreferencias.append(request.form["question4"])
        listaDePreferencias.append(request.form["question5"])
        # return f"{count_inversion(listaDePreferencias)}"
        parecer = count_inversion(listaDePreferencias)
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
    return render_template("motivador.html")


@app.route('/Empresário')
def empresario():
    return render_template("empresario.html")


@app.route('/consul')
def consul():
    return render_template("consul.html")


if __name__ == "__main__":
    app.run(debug=True)
