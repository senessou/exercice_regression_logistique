import sqlite3
from flask import Flask, render_template, request, flash, url_for, redirect


# connection a la base de donnée
def get_db_connect():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    return con


app = Flask(__name__)


# un décorateur qui transforme une fonction Python ordinaire en une fonction d'affichage Flask
@app.route('/')
def index():
    con = get_db_connect()
    posts = con.execute('SELECT * FROM posts').fetchall()
    con.close()
    return render_template('index.html', posts=posts)


# créer une fonction de visualisation qui rendra un modèle affichant un formulaire
@app.route('/', methods=['POST'])
def create():
    if request.method == 'POST':
        age = request.form['age']
        sexe = request.form['sexe']
        tdt = request.form['tdt']
        par = request.form['par']
        chol = request.form['chol']
        gai = request.form['gai']
        ecg = request.form['ecg']
        fcmax = request.form['fcmax']
        angine = request.form['angine']
        depres = request.form['depres']
        pente = request.form['pente']

        if not age:
            flash('Title is required!')
        else:
            conn = get_db_connect()
            conn.execute('INSERT INTO donne (age, sex, tdt, par, cholesterol, gai, ecg, fmax, angine, depres, pente) VALUES (?, ?)', (age, sexe, tdt, par, chol, gai, ecg, fcmax, angine, depres, pente))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
