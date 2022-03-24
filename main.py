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
        return f"{count_inversion(listaDePreferencias)}"
    else:
        return render_template("homepage.html")


@app.route("/<quention1>")
def teste(question1):
    return f"<h1>{listaDePreferencias[0]}<h1>"


if __name__ == "__main__":
    app.run(debug=True)
