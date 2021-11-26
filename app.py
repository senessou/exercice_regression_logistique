from flask import Flask, render_template, request, flash
import numpy as np
import pandas as pd

from regression import predict

app = Flask(__name__)


def qualitative(df):
    for col in df.select_dtypes('object').columns:
        df[col] = df[col].astype('category').cat.codes
    return df


def quantitative(df):
    for col in df.select_dtypes(np.number).columns:
        df[col] = df[col] / df[col].max()
    return df


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def after():
    age = float(request.form['age'])
    sexe = str(request.form['sexe'])
    tdt = str(request.form['tdt'])
    par = float(request.form['par'])
    chol = float(request.form['chol'])
    gai = float(request.form['gai'])
    ecg = str(request.form['ecg'])
    fcmax = float(request.form['fcmax'])
    angine = float(request.form['angine'])
    depres = float(request.form['depres'])
    pente = str(request.form['pente'])
    data = np.array([[age, sexe, tdt, par, chol, gai, ecg, fcmax, angine, depres, pente]])
    data1 = pd.DataFrame(data)
    quant = quantitative(data1)
    print(quant)
    pred = predict(data1)
    print((pred))
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)

# if not age and sexe and tdt and par and chol and gai and ecg and fcmax and angine and depres and pente:
#     flash('champ is required!')
# else:
#     data = np.array([[age, sexe, tdt, par, chol, gai, ecg, fcmax, angine, depres, pente]])
#     y_pred = predit(data)
# return render_template('after.html', data=y_pred)


# créer une fonction de visualisation qui rendra un modèle affichant un formulaire
# @app.route('/post-insert', methods=['POST'])
# def insert():
#     if request.method == 'POST':
#         age = request.form['age']
#         sexe = request.form['sexe']
#         tdt = request.form['tdt']
#         par = request.form['par']
#         chol = request.form['chol']
#         gai = request.form['gai']
#         ecg = request.form['ecg']
#         fcmax = request.form['fcmax']
#         angine = request.form['angine']
#         depres = request.form['depres']
#         pente = request.form['pente']
#
# if not age and sexe and tdt and par and chol and gai and ecg and fcmax and angine and depres and pente: flash(
# 'champ is required!') else: conn = get_db_connect() conn.execute('INSERT INTO donne (age, sex, tdt, par,
# cholesterol, gai, ecg, fmax, angine, depres, pente) VALUES (?, ?)', (age, sexe, tdt, par, chol, gai, ecg, fcmax,
# angine, depres, pente)) conn.commit() conn.close() return redirect(url_for('index')) return render_template(
# 'index.html')
