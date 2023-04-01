from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import date

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
directorio = os.path.abspath(os.path.dirname(__file__))

def escribir(remitos, dia, mes, anio, orden, cantidad, desc, cantidad_dos, desc_dos, cantidad_tres, desc_tres, cantidad_cuatro, desc_cuatro, cantidad_cinco,desc_cinco, cantidad_seis, desc_seis):
    remit = remitos
    image = Image.open(f'{directorio}/Remitolimpio.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(f'{directorio}/arial.ttf', 32)
    draw.text((1405, 315),remit, font=font, fill="black")
    draw.text((1374, 394),dia, font=font, fill="black")
    draw.text((1442, 394),mes, font=font, fill="black")
    draw.text((1510 , 394),anio, font=font, fill="black")
    draw.text((1370, 772),orden, font=font, fill="black")
    draw.text((630, 888),cantidad, font=font, fill="black")
    draw.text((800, 885),desc, font=font, fill="black")
    draw.text((630, 930),cantidad_dos, font=font, fill="black")
    draw.text((800, 927),desc_dos, font=font, fill="black")
    draw.text((630, 972),cantidad_tres, font=font, fill="black")
    draw.text((800, 969),desc_tres, font=font, fill="black")
    draw.text((630, 1014),cantidad_cuatro, font=font, fill="black")
    draw.text((800, 1011),desc_cuatro, font=font, fill="black")
    draw.text((630, 1056),cantidad_cinco, font=font, fill="black")
    draw.text((800, 1053),desc_cinco, font=font, fill="black")
    draw.text((630, 1098),cantidad_seis, font=font, fill="black")
    draw.text((800, 1095),desc_seis, font=font, fill="black")
    image.save(f'{directorio}/static/foto.jpg')

class Registro(FlaskForm):
    remito = StringField('Remito N°', render_kw={'style': 'font-size: 2rem'}, validators=[DataRequired()])
    dia = StringField('Dia', render_kw={'style': 'font-size: 2rem', 'value':dia}, validators=[DataRequired()])
    mes = StringField('Mes',render_kw={'style': 'font-size: 2rem','value':mes}, validators=[DataRequired()])
    anio = StringField('Año', render_kw={'style': 'font-size: 2rem', 'value':anio_s}, validators=[DataRequired()])
    orden = StringField('Orden de compra', render_kw={'style': 'font-size: 2rem'})
    cantidad_uno = StringField('Cantidad', render_kw={'style': 'font-size: 2rem'}, validators=[DataRequired()])
    desc_uno = StringField('Descripcion', render_kw={'style': 'font-size: 2rem'}, validators=[DataRequired()])
    cantidad_dos = StringField('Cantidad', render_kw={'style': 'font-size: 2rem'})
    desc_dos = StringField('Descripcion', render_kw={'style': 'font-size: 2rem'})
    cantidad_tres = StringField('Cantidad', render_kw={'style': 'font-size: 2rem'})
    desc_tres = StringField('Descripcion', render_kw={'style': 'font-size: 2rem'})
    cantidad_cuatro = StringField('Cantidad', render_kw={'style': 'font-size: 2rem'})
    desc_cuatro = StringField('Descripcion', render_kw={'style': 'font-size: 2rem'})
    cantidad_cinco = StringField('Cantidad', render_kw={'style': 'font-size: 2rem'})
    desc_cinco = StringField('Descripcion', render_kw={'style': 'font-size: 2rem'})
    cantidad_seis = StringField('Cantidad', render_kw={'style': 'font-size: 2rem'})
    desc_seis = StringField('Descripcion', render_kw={'style': 'font-size: 2rem'})
    submit = SubmitField('Generar', render_kw={'style': 'font-size: 2rem'})

@app.route("/", methods=['GET', 'POST'])
def index():
    form = Registro()
    if form.validate_on_submit():
        remit = form.remito.data
        dia = form.dia.data
        mes = form.mes.data
        anio = form.anio.data
        orden = form.orden.data
        cantidad = form.cantidad_uno.data
        desc = form.desc_uno.data
        cantidad_dos = form.cantidad_dos.data
        desc_dos = form.desc_tres.data
        cantidad_tres = form.cantidad_tres.data
        desc_tres = form.desc_cuatro.data
        cantidad_cuatro = form.cantidad_cuatro.data
        desc_cuatro = form.desc_cinco.data
        cantidad_cinco = form.cantidad_cinco.data
        desc_cinco = form.desc_cinco.data
        cantidad_seis = form.cantidad_seis.data
        desc_seis = form.desc_seis.data
        escribir(remit, dia, mes, anio, orden, cantidad, desc, cantidad_dos, desc_dos, cantidad_tres, desc_tres, cantidad_cuatro, desc_cuatro, cantidad_cinco,desc_cinco, cantidad_seis, desc_seis)
        return redirect(url_for('remito'))
    return render_template('index.html', form=form)

@app.route("/remito")
def remito():
    return render_template('foto.html')

#if __name__ == "__main__":
#    app.run(debug=True)

