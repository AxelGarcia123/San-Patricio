from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def cargar_login():
    return render_template('Login.html')

@app.route('/menu/')
def cargar_menu():
    return render_template('menu.html')