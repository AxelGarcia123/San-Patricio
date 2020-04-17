from flask import Flask, render_template, request
# from flaskext.mysql import MySQL
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="3_99SA.17*Pc#2",
  database = "sanpatricio",
  auth_plugin='mysql_native_password'
)

cur = mydb.cursor()

@app.route('/', methods=['GET', 'POST'])
def cargar_login():
    if request.method == "POST":
        detalles = request.form
        # print(detalles)
        # _username = detalles['username']
        # _password = detalles['password']
        # cur = mysql.get_db().cursor()
        # cur.execute("select * from test")
        # data = cur.fetchall()
        # print(str(data))
        # print(type(data))
        # cur.close()
        # return render_template('menu.html')
    return render_template('Login.html')

@app.route('/menu/')
def cargar_menu():
    return render_template('menu.html')

@app.route('/menu-responsive/')
def cargar_menu_responsive():
    return render_template('menu_responsive.html')

@app.route('/areas/')
def cargar_areas():
    return render_template('areas.html')

@app.route('/registro-areas', methods=['GET', 'POST'])
def cargar_areas_registro():
    if request.method == "POST":
        detalles = request.form
        _nombre = detalles['nombre']
        _tipo = detalles['tipo']
        _ancho = detalles['ancho']
        _largo = detalles['largo']
        _umedida = detalles['umedida']
        _detalles = detalles['detalles']

        # print(detalles)

        query = "insert into area values(%s, %s, %s, %s, %s, %s, %s)"
        values = (None, _nombre, _tipo, _ancho, _largo, _umedida, _detalles)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")

        #######################

        # cur.execute("select * from test")
        # data = cur.fetchall()

        # print(str(data))


        # _ancho = detalles['ancho']

        # query = "insert into test values(%s, %s)"
        # values = (None, _ancho)

        # cur.execute(query, values)
        # mydb.commit()

        # print("insertado exitosamente")

        pass

    return render_template('areas_registro.html')

# @app.route('/test', methods=['GET', 'POST'])
# def test():
#     if request.method == "POST":
#         detalles = request.form
#         print(detalles)
#     return render_template('test.html')