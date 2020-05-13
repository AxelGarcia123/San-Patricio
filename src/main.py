# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, json
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost", ## Escribir aqui tu host (localhost por defecto)
    user="root", # Escribir aqui tu usuario
    passwd="3_99SA.17*Pc#2", # Escribir aqui tu contraseña
    database = "sanpatricio", # Escribir aqui el nombre de la base de datos
    auth_plugin='mysql_native_password' # Dejar esta propiedad asi
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

# /menu-responsive/
@app.route('/menu-responsive')
def cargar_menu_responsive():
    return render_template('menu_responsive.html')

# --------------------- AREAS --------------------- #

@app.route('/areas/')
def cargar_areas():
    return render_template('areas.html')

# /registro-areas
@app.route('/areas/registrar', methods=['GET', 'POST'])
def cargar_areas_registro():
    if request.method == "POST":
        detalles = request.form
        _nombre = detalles['nombre']
        _tipo = detalles['tipo']
        _ancho = detalles['ancho']
        _largo = detalles['largo']
        _umedida = detalles['umedida']
        _detalles = detalles['detalles']

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

# --------------------- ACTIVIDADES --------------------- #

# /registro-actividades
@app.route('/actividades/registrar', methods=['GET', 'POST'])
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

# --------------------- GRUPOS --------------------- #

# @app.route('/grupos/')
# def cargar_grupos():
#     return render_template('grupos.html')

#/registro-grupos
@app.route('/grupos/registrar', methods=['GET', 'POST'])
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

# --------------------- EMPLEADOS --------------------- #

# Ventana principal de empleados
@app.route('/empleados/')
def cargar_empleados():
    queryAux = "select cve_emp, puesto, concat(ap_per, ' ', am_per, ' ', nom_per) as nombre from empleado e join persona p on e.curp_per=p.curp_per where puesto="
    
    query = queryAux + "'Administrador' order by nombre"
    cur.execute(query)
    administradores = cur.fetchall()

    query = queryAux + "'Docente' order by nombre"
    cur.execute(query)
    docentes = cur.fetchall()

    query = queryAux + "'Limpieza' order by nombre"
    cur.execute(query)
    limpieza = cur.fetchall()

    query = queryAux + "'Velador' order by nombre"
    cur.execute(query)
    veladores = cur.fetchall()

    query = queryAux + "'Director' order by nombre"
    cur.execute(query)
    directores = cur.fetchall()
    return render_template('empleados.html', administradores = administradores, docentes = docentes, limpieza = limpieza, veladores = veladores, directores = directores)

@app.route('/empleado', methods=['POST'])
def empleado():
    data = request.form
    # print(data)
    # print(data['clave'])
    # resultado = "wuolaqtalatodosamigosdellutub"

    query = "select * from empleado where cve_emp=" + data['clave']
    cur.execute(query)
    resultado = cur.fetchall()
    print(resultado[0])

    aux = resultado[0]

    # cve_emp | rfc_emp | fechain_emp | fechafin_emp | puesto  | curp_per

    tupla = { "clave": aux[0], "rfc": aux[1] }

    return tupla

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    print(request.form)
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})

# Registro de empleados
@app.route('/empleados/registrar', methods=['GET', 'POST'])
def cargar_empleados_registro():
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

        _rfc = detalles['rfc']
        _fechain = detalles['fechain']
        _fechafin = detalles['fechafin']
        _puesto = detalles['puesto']

        query = "insert into empleado values (%s, %s, %s, %s, %s, %s)" 
        values = (None, _rfc, _fechain, _fechafin, _puesto, _curp)

        cur.execute(query, values)
        mydb.commit()
        pass

    query = "select * from colonia"
    cur.execute(query)
    colonias = cur.fetchall()

    return render_template('empleados_registro.html', colonias = colonias)

# --------------------- ALUMNOS --------------------- #

# /registro-alumnos
@app.route('/alumnos/registrar', methods=['GET', 'POST'])
def cargar_alumnos_registro():
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

        _estatura = detalles['estatura']
        _peso = detalles['peso']

        query = "insert into alumno values (%s, %s, %s, %s)"
        values = (None, _estatura, _peso, _curp)

        cur.execute(query, values)
        mydb.commit()
        pass

    query = "select * from colonia"
    cur.execute(query)
    colonias = cur.fetchall()

    return render_template('alumnos_registro.html', colonias = colonias)

# --------------------- PROVEEDORES --------------------- #

@app.route('/proveedores/registrar', methods=['GET', 'POST'])
def cargar_proveedores_registro():
    if request.method == "POST":
        detalles = request.form
        _empresa = detalles['empresa']
        _tel = detalles['tel']
        _calle = detalles['calle']
        _num = detalles['num']
        _orient = detalles['orient']
        _entrecalles = detalles['entrecalles']
        _col = detalles['col']

        query = "insert into proveedor values(%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (None, _empresa, _calle, _num, _orient, _entrecalles, _tel, _col)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")
        pass

    query = "select * from colonia"
    cur.execute(query)
    colonias = cur.fetchall()

    return render_template('proveedores_registro.html', colonias = colonias)

# --------------------- FOLIOS --------------------- #

# /generar-folios
@app.route('/folios/generar', methods=['GET', 'POST'])
def cargar_folios_generar():
    if request.method == "POST":
        detalles = request.form
        _fecha = detalles['fecha']
        _hora = detalles['hora']
        _costo = detalles['costo']
        _alumno = detalles['alumno']
        _actividad = detalles['actividad']

        _fechaHora = _fecha + " " + _hora

        query = "insert into folio values (%s, %s, %s, %s, %s)"
        values = (None, _fechaHora, _costo, _alumno, _actividad)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")
        pass

    return render_template('folios_generar.html')

# --------------------- INSCRIPCIONES --------------------- #

# /registro-inscripciones
@app.route('/inscripciones/registrar', methods=['GET', 'POST'])
def cargar_inscripciones_registro():
    if request.method == "POST":
        detalles = request.form
        _folio = detalles['folio']
        _fecha = detalles['fecha']
        _hora = detalles['hora']
        _importe = detalles['importe']
        _total = detalles['total']
        _grupo = detalles['grupo']

        _fechaHora = _fecha + " " + _hora

        query = "insert into registroinscripcion values (%s, %s, %s, %s, %s)"
        values = (_folio, _fechaHora, _importe, _total, _grupo)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")
        pass

    return render_template('inscripciones_registro.html')

# --------------------- MATERIALES --------------------- #

# /registro-materiales
@app.route('/materiales/registrar', methods=['GET', 'POST'])
def cargar_materiales_registro():
    if request.method == "POST":
        detalles = request.form
        _nombre = detalles['nombre']
        _marca = detalles['marca']
        _precio = detalles['precio']
        _actividad = detalles['actividad']
        _descripcion = detalles['descripcion']

        query = "insert into material values (%s, %s, %s, %s, %s, %s)"
        values = (None, _nombre, _marca, _precio, _descripcion, _actividad)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")
        pass

    query = "select cve_act, nom_act from actividad"
    cur.execute(query)
    
    actividades = cur.fetchall()

    return render_template('materiales_registro.html', actividades = actividades)

# TODO: Checar que sea correcta la ejecucion
# /resurtido-materiales
@app.route('/materiales/suministrar', methods=['GET', 'POST'])
def cargar_materiales_resurtido():
    if request.method == "POST":
        detalles = request.form
        _material = detalles['material']
        _proveedor = detalles['proveedor']
        _cantidad = detalles['cantidad']
        _ppu = detalles['ppu']
        _fechaent = detalles['fechaent']

        query = "insert into entrada values (%s, %s, %s, %s, %s, %s)"
        values = (None, _cantidad, _ppu, _fechaent, _material, _proveedor)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")
        pass

    query = "select * from material m join actividad a on m.cve_act=a.cve_act"
    cur.execute(query)
    materiales = cur.fetchall()

    query = "select * from proveedor p join colonia c on p.cve_col=c.cve_col"
    cur.execute(query)
    proveedores = cur.fetchall()

    query = "select nombre_mat, cantidad_ent, preciounidad_ent, empresa_prov, fechaent_ent from material m join entrada e on m.cve_mat=e.cve_mat join proveedor p on e.cve_prov=p.cve_prov order by fechaent_ent limit 5"
    cur.execute(query)
    listaMateriales = cur.fetchall()

    return render_template('materiales_resurtir.html', materiales = materiales, proveedores = proveedores, listaMateriales = listaMateriales)

# --------------------- NOMINAS --------------------- #

@app.route('/nominas', methods=['GET', 'POST'])
def cargar_nominas():
    if request.method == "POST":
        detalles = request.form
        _fecha = detalles['fecha']
        _monto = detalles['monto']
        _modo = detalles['modo']
        _empleado = detalles['empleado']

        query = "insert into pagoempleado values (%s, %s, %s, %s, %s)"
        values = (None, _fecha, _monto, _modo, _empleado)

        cur.execute(query, values)
        mydb.commit()

        print("INSERCION EXITOSA")
        pass

    return render_template('nominas.html')

# @app.route('/test', methods=['GET', 'POST'])
# def test():
#     if request.method == "POST":
#         detalles = request.form
#         print(detalles)
#     return render_template('test.html')