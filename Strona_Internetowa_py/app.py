from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user
import sqlite3 as sql
app = Flask(__name__)

#config
app.config.update(
DEBUG = True,
SECRET_KEY = 'sekretny_klucz'
)


# ustawienie flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route("/logowanie", methods=["GET","POST"])
def login():
    tytul = 'Zaloguj się'
    if request.method =='POST':
        try:
            username = request.form['login']
            password = request.form['haslo']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("SELECT COUNT(1) FROM users WHERE login = '" + username +"'")
                users = cur.fetchall()
                con.commit()

                if password == username:
                    id = username.split('user')
                    login_user(id)
                    return redirect(url_for("main"))
                else:
                    return abort(401)
        finally:
            return render_template('formularz_logowania.html', tytul=tytul)

@app.errorhandler(401)
def page_no_found(e):
    tytul="Coś poszło nie tak..."
    blad = "401"
    return render_template('blad.html', tytul=tytul, blad=blad)

@app.route("/wyloguj")
@login_required
def logout():
    logout_user()
    tytul = "Wylogowanie"
    return render_template('logout.html', tytul=tytul)

#przeladowanie uzutkownika
@login_manager.user_loader
def load_user(userid):
    return User(userid)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/dodaj")
@login_required #wymaga logowania
def dodaj():
    return render_template('dodaj.html')


@app.route("/oczekujace")
def oczekujace():
    return render_template('oczekujace.html')

@app.route("/rejestracja")
def new_uzytkownik():
 return render_template('uzytkownikadd.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            login = request.form['login']
            haslo = request.form['haslo']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO uzytkownicy (login, haslo) VALUES (?,?)",(login, haslo))
                users = cur.fetchall()
                con.commit()
                msg = "Pomyślnie założono konto"
        except:
            con.rollback()
            msg = "Blad przy zakładaniu konta"

        finally:
            return render_template("rezultat.html",msg = msg)
            con.close()

@app.route("/pag1")
def pag1():
    return render_template('pag1.html')

@app.route("/pag2")
def pag2():
    return render_template('pag2.html')

@app.route("/pag3")
def pag3():
    return render_template('pag3.html')

@app.route("/pag4")
def pag4():
    return render_template('pag4.html')

@app.route("/pag5")
def pag5():
    return render_template('pag5.html')


if __name__ == "__main__":
    app.run()