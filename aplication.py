from flask import Flask, render_template, redirect, url_for, request, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from PIL import Image, ImageDraw, ImageFont
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


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrtuky23876213et'
login = LoginManager(app)
login.login_view = 'logi'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=50)
directorio = os.path.abspath(os.path.dirname(__file__))

def escribir(seniores, direc, transp, lugar, cui, iba, remitos, dia, mes, anio, orden, cantidad, desc, cantidad_dos, desc_dos, cantidad_tres, desc_tres, cantidad_cuatro, desc_cuatro, cantidad_cinco,desc_cinco, cantidad_seis, desc_seis):
    remit = remitos
    image = Image.open(f'{directorio}/Remitolimpio.jpg')
    draw = ImageDraw.Draw(image)
    font20 = ImageFont.truetype(f'{directorio}/arial.ttf', 20)
    font22 = ImageFont.truetype(f'{directorio}/arial.ttf', 22)
    font24 = ImageFont.truetype(f'{directorio}/arial.ttf', 24)
    draw.text((960, 216),remit, font=font22, fill="black")
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
    image.save(f'{directorio}/static/remito-{remit}.jpg')

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


class Registro(FlaskForm):
    remito = StringField('Remito N°', render_kw={'style': 'font-size: 2rem; width: 70px', "size": 3}, validators=[DataRequired(), Length(max=3)])
    dia = StringField('Dia', render_kw={'style': 'font-size: 2rem; width: 50px' , 'value':dia, "size":2}, validators=[DataRequired(), Length(max=2)])
    mes = StringField('Mes',render_kw={'style': 'font-size: 2rem; width: 50px','value':mes, "size":2}, validators=[DataRequired(), Length(max=2)])
    anio = StringField('Año', render_kw={'style': 'font-size: 2rem; width: 50px', 'value':anio_s, "size":2}, validators=[DataRequired(), Length(max=2)])
    orden = StringField('Orden de compra', render_kw={'style': 'font-size: 1.5rem'})
    seniores = StringField('Señores', render_kw={'style': 'font-size: 1.5rem; width: 170px', 'value':"Cristamine"}, validators=[DataRequired()])
    direccion = StringField('Direccion', render_kw={'style': 'font-size: 1.5rem', 'value':"Dardo Rocha 1037"}, validators=[DataRequired()])
    iva = SelectField('IVA', choices=['Responsable inscripto', 'Consumidor final', 'Exento', 'Responsable monotributista'], render_kw={'style': 'font-size: 1.5rem'})
    transportista = StringField('Transportista', render_kw={'style': 'font-size: 1.5rem; width: 170px', 'value':"Croce"}, validators=[DataRequired()])
    lugar_entrega = StringField('Lugar de entrega', render_kw={'style': 'font-size: 1rem', 'value':"Dardo Rocha 1073"}, validators=[DataRequired()])
    cuit = StringField('Cuit', render_kw={'style': 'font-size: 1.5rem; width: 240px', 'value':"30-50423240-5"}, validators=[DataRequired()])
    cantidad_uno = StringField('Cantidad', render_kw={'style': 'font-size: 1.5rem; width: 50%'}, validators=[DataRequired()])
    desc_uno = StringField('Descripcion', render_kw={'style': 'font-size: 1.5rem; width: 100%'}, validators=[DataRequired()])
    cantidad_dos = StringField('Cantidad', render_kw={'style': 'font-size: 1.5rem; width: 50%'})
    desc_dos = StringField('Descripcion', render_kw={'style': 'font-size: 1.5rem; width: 100%'})
    cantidad_tres = StringField('Cantidad', render_kw={'style': 'font-size: 1.5rem; width: 50%'})
    desc_tres = StringField('Descripcion', render_kw={'style': 'font-size: 1.5rem; width: 100%'})
    cantidad_cuatro = StringField('Cantidad', render_kw={'style': 'font-size: 1.5rem; width: 50%'})
    desc_cuatro = StringField('Descripcion', render_kw={'style': 'font-size: 1.5rem; width: 100%'})
    cantidad_cinco = StringField('Cantidad', render_kw={'style': 'font-size: 1.5rem; width: 50%'})
    desc_cinco = StringField('Descripcion', render_kw={'style': 'font-size: 1.5rem; width: 100%'})
    cantidad_seis = StringField('Cantidad', render_kw={'style': 'font-size: 1.5rem; width: 50%'})
    desc_seis = StringField('Descripcion', render_kw={'style': 'font-size: 1.5rem; width: 100%'})
    submit = SubmitField('Generar', render_kw={'style': 'font-size: 2rem'})

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

@app.route("/remitos", methods=['GET', 'POST'])
@login_required
def remitos():
    form = Registro()
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
    numero = f'remito-{numero}.jpg'
    ruta_imagen = directorio+"/static/"+numero
    return render_template('foto.html', ruta_imagen=ruta_imagen, numero=numero)
    
@app.route("/descargar/<ruta_archivo>")
def descargar(ruta_archivo):
    print("entro en descargar")
    print(ruta_archivo)
    ruta_imagen = directorio+"/static/"+ruta_archivo
    return send_file(ruta_imagen, as_attachment=True)


@login.user_loader
def load_user(id):
    return User(id)

@login.unauthorized_handler
def unauthorized():
    login_message = 'Please log in to access this page.'
    return redirect(url_for('logi', next=request.path, message=login_message))


#if __name__ == "__main__":
#    app.run(debug=True)

