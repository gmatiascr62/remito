from flask import Flask, render_template, redirect, url_for, request, send_file, jsonify, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length
from flask_login import LoginManager, login_user, current_user, login_required, UserMixin
from PIL import Image, ImageDraw, ImageFont
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import date
from datetime import timedelta



hoy = date.today()

anio_s = str(hoy.year)[-2:]
dia = hoy.day
if dia < 10 :
    dia = "0"+str(dia)
mes = hoy.month
if mes < 10 :
    mes = "0"+str(mes)

# variables de configuracion
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrtuky23876213et'
login = LoginManager(app)
login.login_view = 'logi'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=50)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('base')
db = SQLAlchemy(app)
directorio = os.path.abspath(os.path.dirname(__file__))


# precio del material de una rueda de trommel sin tapas y sin iva
pmrt = 32400

def escribir(seniores, direc, transp, lugar, cui, iba, remitos, dia, mes, anio, orden, cantidad, desc, cantidad_dos, desc_dos, cantidad_tres, desc_tres, cantidad_cuatro, desc_cuatro, cantidad_cinco,desc_cinco, cantidad_seis, desc_seis):
    remit = remitos
    image = Image.open(f'{directorio}/Remitolimpio.jpg')
    draw = ImageDraw.Draw(image)
    font20 = ImageFont.truetype(f'{directorio}/arial.ttf', 20)
    font22 = ImageFont.truetype(f'{directorio}/arial.ttf', 22)
    font24 = ImageFont.truetype(f'{directorio}/arial.ttf', 24)
    draw.text((948, 215),remit, font=font22, fill="black")
    draw.text((940, 268),dia, font=font24, fill="black")
    draw.text((985, 268),mes, font=font24, fill="black")
    draw.text((1030, 268),anio, font=font24, fill="black")
    draw.text((935, 525),orden, font=font24, fill="black")
    draw.text((455, 385),seniores, font=font22, fill="black")
    draw.text((455, 423),direc, font=font22, fill="black")
    draw.text((480, 496),transp, font=font22, fill="black")
    draw.text((500, 532),lugar, font=font22, fill="black")
    draw.text((853, 457),cui, font=font22, fill="black")
    draw.text((430, 610),cantidad, font=font20, fill="black")
    draw.text((550, 610),desc, font=font20, fill="black")
    draw.text((430, 639),cantidad_dos, font=font20, fill="black")
    draw.text((550, 639),desc_dos, font=font20, fill="black")
    draw.text((430, 668),cantidad_tres, font=font20, fill="black")
    draw.text((550, 668),desc_tres, font=font20, fill="black")
    draw.text((430, 697),cantidad_cuatro, font=font20, fill="black")
    draw.text((550, 697),desc_cuatro, font=font20, fill="black")
    draw.text((430, 726),cantidad_cinco, font=font20, fill="black")
    draw.text((550, 726),desc_cinco, font=font20, fill="black")
    draw.text((430, 755),cantidad_seis, font=font20, fill="black")
    draw.text((550, 755),desc_seis, font=font20, fill="black")
    draw.text((935, 1140),"Vto 31/12/23", font=font22, fill="black")
    if iba == 'Responsable inscripto':
        draw.text((713, 465),"x", font=font22, fill="black")
    elif iba == 'Consumidor final':
        draw.text((470, 465),"x", font=font22, fill="black")
    elif iba == 'Exento':
        draw.text((535, 465),"x", font=font22, fill="black")
    elif iba == 'Responsable monotributista':
        draw.text((628, 465),"x", font=font22, fill="black")
    image.save(f'{directorio}/static/Remito{remit}.jpg')


def calcular_chavetero_interior(diametro):
    diametro = float(diametro)
    if diametro > 9 and diametro < 13:
        return [str(diametro + 1.7), "4"]
    elif diametro > 12 and diametro < 18:
        return [str(diametro + 2.2), "5"]
    elif diametro > 17 and diametro < 26:
        return [str(diametro + 2.7), "6"]
    elif diametro > 25 and diametro < 31:
        return [str(diametro + 3.2), "8"]
    elif diametro > 30 and diametro < 39:
        return [str(diametro + 3.7), "10"]
    elif diametro > 38 and diametro < 45:
        return [str(diametro + 3.7), "12"]
    elif diametro > 44 and diametro < 51:
        return [str(diametro + 4.2), "14"]
    elif diametro > 50 and diametro < 59:
        return [str(diametro + 5.2), "16"]
    elif diametro > 58 and diametro < 69:
        return [str(diametro + 5.3), "18"]
    elif diametro > 68 and diametro < 79:
        return [str(diametro + 6.3), "20"]
    elif diametro > 78 and diametro < 93:
        return [str(diametro + 7.3), "24"]
    elif diametro > 92 and diametro < 111:
        return [str(diametro + 8.3), "28"]
    elif diametro > 110 and diametro < 131:
        return [str(diametro + 9.3), "32"]
    elif diametro > 130 and diametro < 151:
        return [str(diametro + 10.3), "36"]
    elif diametro > 150 and diametro < 171:
        return [str(diametro + 11.3), "40"]
    elif diametro > 180 and diametro < 201:
        return [str(diametro + 12.3), "45"]
    elif diametro > 200 and diametro < 231:
        return [str(diametro + 14.3), "50"]
    else:
        return ["x","x"]

def calcular_chavetero_exterior(diametro):
    diametro = float(diametro)
    if diametro > 9 and diametro < 13:
        return ["2.5", "4"]
    elif diametro > 12 and diametro < 18:
        return ["3", "5"]
    elif diametro > 17 and diametro < 26:
        return ["3.5", "6"]
    elif diametro > 25 and diametro < 31:
        return ["4", "8"]
    elif diametro > 30 and diametro < 39:
        return ["4.5", "10"]
    elif diametro > 38 and diametro < 45:
        return ["4.5", "12"]
    elif diametro > 44 and diametro < 51:
        return ["5", "14"]
    elif diametro > 50 and diametro < 59:
        return ["5", "16"]
    elif diametro > 58 and diametro < 69:
        return ["6", "18"]
    elif diametro > 68 and diametro < 79:
        return ["6", "20"]
    elif diametro > 78 and diametro < 93:
        return ["7", "24"]
    elif diametro > 92 and diametro < 111:
        return ["8", "28"]
    elif diametro > 110 and diametro < 131:
        return ["9", "32"]
    elif diametro > 130 and diametro < 151:
        return ["10", "36"]
    elif diametro > 150 and diametro < 171:
        return ["11", "40"]
    elif diametro > 180 and diametro < 201:
        return ["13", "45"]
    elif diametro > 200 and diametro < 231:
        return ["14", "50"]
    else:
        return ["x","x"]

def escribir_chavetero(diametro, tipo):
    if tipo == "interior":
        result_chavetero = calcular_chavetero_interior(diametro)
        image = Image.open(f'{directorio}/static/chli.jpg')
        draw = ImageDraw.Draw(image)
        font24 = ImageFont.truetype(f'{directorio}/arial.ttf', 60)
        draw.text((40, 280),result_chavetero[0], font=font24, fill="black")
        draw.text((330, 10),result_chavetero[1], font=font24, fill="black")
        image = image.convert("RGB")
        image.save(f'{directorio}/static/imagen_chavetero.jpg')
    elif tipo == "exterior":
        result_chavetero = calcular_chavetero_exterior(diametro)
        image = Image.open(f'{directorio}/static/imagen_redimensionada.jpg')
        draw = ImageDraw.Draw(image)
        font24 = ImageFont.truetype(f'{directorio}/arial.ttf', 60)
        draw.text((460, 180),result_chavetero[0], font=font24, fill="black")
        draw.text((245, 70),result_chavetero[1], font=font24, fill="black")
        image = image.convert("RGB")
        image.save(f'{directorio}/static/imagen_chavetero.jpg')

def calcular_cono(lista):
    mayor = float(lista[1])
    menor = float(lista[2])
    largo = float(lista[3])
    resultado = (mayor-menor)
    resultado = resultado/2
    resultado = resultado*57.3
    resultado = resultado/largo
    return str(round(resultado,2))

class MiTabla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)

    
class User(UserMixin):
    def __init__(self, id):
        self.id = id
    def is_active(self):
        return True

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Entrar')

def actual_numero():
    with app.app_context():
        resultado=MiTabla.query.filter_by(id=1).first()
        if resultado:
            valor = resultado.numero
            return valor
        else:
            return "999"

class Registro(FlaskForm):
    remito = StringField('Remito N°', render_kw={'style': 'font-size: 1rem; width: 45px', "size": 4}, validators=[DataRequired(), Length(max=4)])
    dia = StringField('Dia', render_kw={'style': 'font-size: 1rem; width: 25px' , 'value':dia, "size":2}, validators=[DataRequired(), Length(max=2)])
    mes = StringField('Mes',render_kw={'style': 'font-size: 1rem; width: 25px','value':mes, "size":2}, validators=[DataRequired(), Length(max=2)])
    anio = StringField('Año', render_kw={'style': 'font-size: 1rem; width: 25px', 'value':anio_s, "size":2}, validators=[DataRequired(), Length(max=2)])
    orden = StringField('Orden de compra', render_kw={'style': 'font-size: 1rem'})
    seniores = StringField('Señores', render_kw={'style': 'font-size: 1rem; width: 170px', 'value':"Cristamine"}, validators=[DataRequired()])
    direccion = StringField('Direccion', render_kw={'style': 'font-size: 1rem', 'value':"Dardo Rocha 1037"}, validators=[DataRequired()])
    iva = SelectField('IVA', choices=['Responsable inscripto', 'Consumidor final', 'Exento', 'Responsable monotributista'], render_kw={'style': 'font-size: 1rem'})
    transportista = StringField('Transportista', render_kw={'style': 'font-size: 1rem; width: 170px', 'value':"Croce"}, validators=[DataRequired()])
    lugar_entrega = StringField('Lugar de entrega', render_kw={'style': 'font-size: 1rem', 'value':"Dardo Rocha 1073"}, validators=[DataRequired()])
    cuit = StringField('Cuit', render_kw={'style': 'font-size: 1rem; width: 160px', 'value':"30-50423240-5"}, validators=[DataRequired()])
    cantidad_uno = StringField('Cantidad', render_kw={'style': 'font-size: 1rem; width: 50%'}, validators=[DataRequired()])
    desc_uno = StringField('Descripcion', render_kw={'style': 'font-size: 1rem; width: 100%'}, validators=[DataRequired()])
    cantidad_dos = StringField('Cantidad', render_kw={'style': 'font-size: 1rem; width: 50%'})
    desc_dos = StringField('Descripcion', render_kw={'style': 'font-size: 1rem; width: 100%'})
    cantidad_tres = StringField('Cantidad', render_kw={'style': 'font-size: 1rem; width: 50%'})
    desc_tres = StringField('Descripcion', render_kw={'style': 'font-size: 1rem; width: 100%'})
    cantidad_cuatro = StringField('Cantidad', render_kw={'style': 'font-size: 1rem; width: 50%'})
    desc_cuatro = StringField('Descripcion', render_kw={'style': 'font-size: 1rem; width: 100%'})
    cantidad_cinco = StringField('Cantidad', render_kw={'style': 'font-size: 1rem; width: 50%'})
    desc_cinco = StringField('Descripcion', render_kw={'style': 'font-size: 1rem; width: 100%'})
    cantidad_seis = StringField('Cantidad', render_kw={'style': 'font-size: 1rem; width: 50%'})
    desc_seis = StringField('Descripcion', render_kw={'style': 'font-size: 1rem; width: 100%'})
    submit = SubmitField('Generar', render_kw={'style': 'font-size: 1.5rem'})

@app.route("/login", methods=['GET', 'POST'])
def logi():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "taller":
             if form.password.data == "1342":
                user = User(id=1)
                login_user(user)
                return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route("/prueba", methods=['GET', 'POST'])
def prueba():
    form = Registro()
    return render_template('prueba.html', form=form)


@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@app.route("/cosas", methods=['GET', 'POST'])
@login_required
def cosas():
    return render_template('cosas.html')

@app.route("/remitos", methods=['GET', 'POST'])
@login_required
def remitos():
    valor_predeterminado = actual_numero()
    form = Registro(remito=valor_predeterminado)
    if form.validate_on_submit():
        remit = form.remito.data
        dia = form.dia.data
        mes = form.mes.data
        anio = form.anio.data
        senior = form.seniores.data
        dire = form.direccion.data
        transporte = form.transportista.data
        lugar = form.lugar_entrega.data
        cui = form.cuit.data
        iva = form.iva.data
        orden = form.orden.data
        cantidad = form.cantidad_uno.data
        desc = form.desc_uno.data
        cantidad_dos = form.cantidad_dos.data
        desc_dos = form.desc_dos.data
        cantidad_tres = form.cantidad_tres.data
        desc_tres = form.desc_tres.data
        cantidad_cuatro = form.cantidad_cuatro.data
        desc_cuatro = form.desc_cuatro.data
        cantidad_cinco = form.cantidad_cinco.data
        desc_cinco = form.desc_cinco.data
        cantidad_seis = form.cantidad_seis.data
        desc_seis = form.desc_seis.data
        escribir(senior, dire, transporte, lugar, cui, iva, remit, dia, mes, anio, orden, cantidad, desc, cantidad_dos, desc_dos, cantidad_tres, desc_tres, cantidad_cuatro, desc_cuatro, cantidad_cinco,desc_cinco, cantidad_seis, desc_seis)
        return redirect(url_for('remito', numero=remit))
    return render_template('remitos.html', form=form)


@app.route("/remito/<numero>")
@login_required
def remito(numero):
    numero = f'Remito{numero}.jpg'
    ruta_imagen = directorio+"/static/"+numero
    return render_template('foto.html', ruta_imagen=ruta_imagen, numero=numero)
    
@app.route("/descargar/<ruta_archivo>")
def descargar(ruta_archivo):
    print("entro en descargar")
    print(ruta_archivo)
    with app.app_context():
        resultado=MiTabla.query.filter_by(id=1).first()
        if resultado:
            print(resultado.numero)
            resultado.numero = int(ruta_archivo[6:10])+1
            print(resultado.numero)
            db.session.commit()
    ruta_imagen = directorio+"/static/"+ruta_archivo
    return send_file(ruta_imagen, as_attachment=True)

@app.route("/precios")
def precios():
    return render_template("precios.html", pmrt=pmrt)

@login.user_loader
def load_user(id):
    return User(id)

@login.unauthorized_handler
def unauthorized():
    login_message = 'Please log in to access this page.'
    return redirect(url_for('logi', next=request.path, message=login_message))

@app.route('/api', methods=['GET', 'POST'])
def api():
    datos = request.get_json()
    datos = datos['texto']
    if datos[0] == "chavetero":
        escribir_chavetero(datos[1], datos[2])
        respuesta = make_response(jsonify({'respuesta': f'{datos}'}, 200))
    elif datos[0] == "cono":
        respuesta = make_response(jsonify({'respuesta': calcular_cono(datos)}, 200))
    return respuesta

#with app.app_context():
#    db.create_all()



if __name__ == "__main__":
    app.run(debug=True)
