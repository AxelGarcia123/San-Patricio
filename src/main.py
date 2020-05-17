# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, json, jsonify
import mysql.connector
import json
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

# --------------------- AREAS --------------------- ## --------------------- AREAS --------------------- #

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

# --------------------- ACTIVIDADES --------------------- ## --------------------- ACTIVIDADES --------------------- #

# Ventana principal de actividades
@app.route('/actividades/')
def cargar_actividades():
    query = "select * from actividad where tipo_act='Deportiva' order by nom_act"
    cur.execute(query)
    actividadesDeportivas = cur.fetchall()

    query = "select * from actividad where tipo_act='Artistica' order by nom_act"
    cur.execute(query)
    actividadesArtisticas = cur.fetchall()

    return render_template('actividades.html', actividadesDeportivas = actividadesDeportivas, actividadesArtisticas = actividadesArtisticas)

@app.route('/actividad', methods=['POST'])
def actividad():
    data = request.form
    query = "select * from actividad where cve_act=" + data['clave']
    cur.execute(query)
    _actividad = cur.fetchall()

    actividad = _actividad[0]

    _tipo = None

    for i in actividad[2]:
        _tipo = i

    # query = "select g.* from grupo g join actividad a on g.cve_act=a.cve_act where g.cve_act=" + data['clave']
    query = "select g.*, a.nom_act, concat(p.nom_per, ' ', p.ap_per, ' ', p.am_per) from grupo g join actividad a on g.cve_act=a.cve_act join empleado e on g.cve_emp=e.cve_emp join persona p on e.curp_per=p.curp_per where g.cve_act=" + data['clave']
    cur.execute(query)
    grupos = cur.fetchall()

    grupos_dict = []

    for grupo in grupos:
        grupo_dict = {
            "horaent": str(grupo[1]),
            "horasali": str(grupo[2]),
            "fechaini": str(grupo[3]),
            "fechafin": str(grupo[4]),
            "maxalumnos": grupo[5],
            "minalumnos": grupo[6],
            "are": grupo[10],
            "emp": grupo[11]
        }
        grupos_dict.append(grupo_dict)

    tupla = {
        "actividad": [
            { "clave": actividad[0], "nom": actividad[1], "tipo": _tipo, "descrip": actividad[3] }
        ],
        "grupos": grupos_dict
    }

    return tupla

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
        return redirect(url_for('cargar_actividades'))

    return render_template('actividades_registro.html')

# --------------------- GRUPOS --------------------- ## --------------------- GRUPOS --------------------- #

# Ventana principal de grupos
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

        query = "select cve_emp, concat(ap_per, ' ', am_per, ' ', nom_per) as nombre from empleado e join persona p on e.curp_per=p.curp_per where puesto='Docente'"  
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

# --------------------- EMPLEADOS --------------------- ## --------------------- EMPLEADOS --------------------- #

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

    query = "select * from empleado e join persona p on e.curp_per=p.curp_per where cve_emp=" + data['clave']
    cur.execute(query)
    resultado = cur.fetchall()

    # print(type(resultado))
    # print(type(resultado[0]))
    # print(resultado)

    datosEmpleado = resultado[0]

    _puesto = None
    _genero = None
    _orient = None

    for x in datosEmpleado[4]: # Esta es la unica forma de acceder a un elemento de un set(conjunto)
        _puesto = x

    for x in datosEmpleado[12]:
        _genero = x

    for x in datosEmpleado[15]:
        _orient = x

    query = "select * from grupo where cve_emp=" + str(datosEmpleado[0])
    cur.execute(query)
    grupos = cur.fetchall()
    # print(grupos)
    # print(type(grupos))
    # print(type(grupos[0]))

    gruposDict = [] # Diccionario de grupos

    for grupo in grupos: # Esta es la forma mas sencilla de generar un JSON para retornar una respuesta
        grupoDict = {
            "clave": grupo[0],
            'horaent': str(grupo[1]),
            "horasali": str(grupo[2]),
            "fechaini": str(grupo[3]),
            "fechafin": str(grupo[4]),
            "maxalumnos": grupo[5],
            "minalumnos": grupo[6],
            "act": grupo[7],
            "are": grupo[8]
        }
        gruposDict.append(grupoDict)

    # x = json.dumps(grupos, indent=4, sort_keys=True, default=str) # Esto no funciona -_-
    # xX = json.loads(x) # Que perdida de tiempo e.e
    # gG = Convert(xX)

    tupla = { 
        "laborales": [
            { "clave": datosEmpleado[0], "rfc": datosEmpleado[1], "fechain": datosEmpleado[2], "fechafin": datosEmpleado[3], "puesto": _puesto }
        ],
        "personales": [
            { "curp": datosEmpleado[5], "nombre": datosEmpleado[7] + " " + datosEmpleado[8] + " " + datosEmpleado[9], "tel": datosEmpleado[10],
            "fechanac": datosEmpleado[11], "genero": _genero, 
            "domicilio": datosEmpleado[13] + " " + _orient + " " + str(datosEmpleado[14]) }
        ],
        "grupos": gruposDict
    }

    # print(tupla)
    # print("tupla = ", type(tupla))

    # print(tupla.laborales)

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
        return redirect(url_for('cargar_empleados'))
        # pass

    query = "select * from colonia"
    cur.execute(query)
    colonias = cur.fetchall()

    return render_template('empleados_registro.html', colonias = colonias)

# --------------------- ALUMNOS --------------------- ## --------------------- ALUMNOS --------------------- #

# Ventana principal de alumnos
@app.route('/alumnos/')
def cargar_alumnos():
    query = "select a.cve_alu, concat(nom_per, ' ', ap_per, ' ', am_per) from grupo g join registroinscripcion ri on g.cve_gru=ri.cve_gru join folio f on ri.folio_insc=f.folio_fol join alumno a on f.cve_alu=a.cve_alu join persona p on a.curp_per=p.curp_per where curdate() between fechaini_gru and fechafin_gru"
    cur.execute(query)
    inscritos = cur.fetchall()

    # query = "select a.cve_alu, concat(nom_per, ' ', ap_per, ' ', am_per) from folio f join alumno a on f.cve_alu=a.cve_alu join persona p on a.curp_per=p.curp_per where not exists(select folio_fol, folio_insc from folio f, registroinscripcion ri where folio_fol=folio_insc)"
    query = "select a.cve_alu, concat(nom_per, ' ', ap_per, ' ', am_per) from folio f join registroinscripcion ri on f.folio_fol!=ri.folio_insc join alumno a on f.cve_alu=a.cve_alu join persona p on a.curp_per=p.curp_per"
    cur.execute(query)
    noInscritos = cur.fetchall()

    return render_template('alumnos.html', inscritos = inscritos, noInscritos = noInscritos)

@app.route('/alumno', methods=['POST'])
def alumno():
    data = request.form

    query = "select a.*, concat(p.nom_per, ' ', ap_per, ' ', am_per) as nombre, p.tel_per, p.fechanac_per, p.genero_per, concat(p.calle_per, ' ', p.orient_per, ' ', p.numero_per) as direccion from alumno a join persona p on a.curp_per=p.curp_per where a.cve_alu=" + data['clave']
    cur.execute(query)
    _alumno = cur.fetchall()

    alumno = _alumno[0]

    _genero = None

    for i in alumno[7]:
        _genero = i

    query = "select f.*, ac.nom_act from folio f join alumno a on f.cve_alu=a.cve_alu join actividad ac on f.cve_act=ac.cve_act where f.cve_alu=" + data['clave'] + " order by fecha_fol limit 1"
    cur.execute(query)
    folio = cur.fetchall()

    # print("folio = ", folio)

    tupla = {
        "alumno": [
            { "clave": alumno[0], "estatura": alumno[1], "peso": alumno[2] }
        ],
        "personales": [
            { "curp": alumno[3], "nombre": alumno[4], "tel": alumno[5], "fechanac": str(alumno[6]), "genero": _genero, "domicilio": alumno[8] }
        ],
        "folio": folio
    }

    print(tupla)
    return tupla

@app.route('/alumnoInscribir', methods=['POST'])
def alumnoInscribir():
    data = request.form
    print("data = ", data)

    query = "insert into registroinscripcion values(%s, %s, %s, %s, %s)"
    values = (data['folio'], data['fecha'], data['importe'], data['importe'], data['grupo'])

    cur.execute(query, values)
    mydb.commit()

    return "OK"

import time

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
        # mydb.commit()

        _costo = detalles['costo']
        _act = detalles['act']

        query = "select max(cve_alu) from alumno"
        cur.execute(query)
        _alumno = cur.fetchall()

        alumno = _alumno[0]

        query = "insert into folio values(%s, %s, %s, %s, %s)"
        values = (None, time.strftime('%Y-%m-%d %H:%M:%S'), _costo, alumno[0], _act)

        cur.execute(query, values)
        mydb.commit()

        return redirect(url_for('cargar_alumnos'))

    query = "select * from colonia"
    cur.execute(query)
    colonias = cur.fetchall()

    query = "select cve_act, concat(nom_act, ' - ', tipo_act) from actividad"
    cur.execute(query)
    actividades = cur.fetchall()

    return render_template('alumnos_registro.html', colonias = colonias, actividades = actividades)

# --------------------- PROVEEDORES --------------------- ## --------------------- PROVEEDORES --------------------- #

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

# --------------------- MATERIALES --------------------- ## --------------------- MATERIALES --------------------- #

# Ventana principal de materiales
@app.route('/materiales/')
def cargar_materiales():
    return render_template('materiales.html')

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