from flask import Flask, render_template, request, redirect, url_for
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
    # if request.method == "POST":
    #     detalles = request.form
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

@app.route('/registro-actividades', methods=['GET', 'POST'])
def cargar_actividades_registro():
    if request.method == "POST":
        detalles = request.form
        _nombre = detalles['nombre']
        _tipo = detalles['tipo']
        _descripcion = detalles['descripcion']

        query = "insert into actividad values(%s, %s, %s, %s)"
        values = (None, _nombre, _tipo, _descripcion)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")

        pass

    return render_template('actividades_registro.html')

# @app.route('/grupos/')
# def cargar_grupos():
#     return render_template('grupos.html')

@app.route('/registro-grupos', methods=['GET', 'POST'])
def cargar_grupos_registro():
    if request.method == "GET":
        query = "select cve_act, nom_act from actividad"     
        cur.execute(query)
        actividades = cur.fetchall()

        query = "select cve_are, nombre_are from area"
        cur.execute(query)
        areas = cur.fetchall()

        query = "select cve_emp, concat(ap_per, ' ', am_per, ' ', nom_per) as nombre from empleado e join persona p on e.curp_per=p.curp_per"  
        cur.execute(query)
        empleados = cur.fetchall()

        return render_template('grupos_registro.html', actividades = actividades, areas = areas, empleados = empleados)

    if request.method == "POST":
        detalles = request.form
        _horaent = detalles['horaent']
        _horasali = detalles['horasali']
        _fechaini = detalles['fechaini']
        _fechafin = detalles['fechafin']
        _minalumnos = detalles['minalumnos']
        _maxalumnos = detalles['maxalumnos']
        _actividad = detalles['actividad']
        _area = detalles['area']
        _empleado = detalles['empleado']

        query = "insert into grupo values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (None, _horaent, _horasali, _fechaini, _fechafin, _maxalumnos, _minalumnos, _actividad, _area, _empleado)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")
        pass

    return render_template('grupos_registro.html')

### TODO: CHECAR QUE SEA CORRECTA LA EJECUCION
@app.route('/registro-personas', methods=['GET', 'POST'])
def cargar_personas_registro():      
    if request.method == "POST":
        detalles = request.form
        _curp = detalles['curp']
        _nombre = detalles['nombre']
        _ap = detalles['ap']
        _am = detalles['am']
        _tel = detalles['tel']
        _fechanac = detalles['fechanac']
        _genero = detalles['genero']
        _calle = detalles['calle']
        _num = detalles['num']
        _orient = detalles['orient']
        _entrecalles = detalles['entrecalles']
        _col = detalles['col']

        query = "insert into persona values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (_curp, _nombre, _ap, _am, _tel, _fechanac, _genero, _calle, _num, _orient, _entrecalles, _col)

        cur.execute(query, values)
        # mydb.commit()

        return redirect(url_for('cargar_alumnos_registro', curp = _curp))
        # return render_template('alumnos_registro.html', curp = _curp) ## NO funciona

    query = "select * from colonia"
    cur.execute(query)
    colonias = cur.fetchall()

    return render_template('personas_registro.html', colonias = colonias)

### TODO: CHECAR QUE SEA CORRECTA LA EJECUCION
@app.route('/registro-alumnos/<curp>', methods=['GET', 'POST'])
def cargar_alumnos_registro(curp):
    if request.method == "POST":
        detalles = request.form
        _estatura = detalles['estatura']
        _peso = detalles['peso']

        query = "insert into alumno values (%s, %s, %s, %s)"
        values = (None, _estatura, _peso, curp)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")

        pass

    return render_template('alumnos_registro.html', curp = curp)

# @app.route('/test', methods=['GET', 'POST'])
# def test():
#     if request.method == "POST":
#         detalles = request.form
#         print(detalles)
#     return render_template('test.html')