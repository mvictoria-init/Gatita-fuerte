from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField, PasswordField, BooleanField, HiddenField
from wtforms.validators import data_required

from utils import calcular_edad

class UsuarioForm(FlaskForm):
    id = HiddenField('id')
    cedula = IntegerField('Cédula', validators=[data_required()])
    nombre = StringField('Nombre', validators=[data_required()])
    apellido = StringField('Apellido', validators=[data_required()])
    cumpleaños = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[data_required()])
    nombreapp = StringField('Nombre de usuario', validators=[data_required()])
    contraseña = PasswordField('Contraseña', validators=[data_required()])
    administrador = SelectField('Administrador', choices=[('1', 'Si'), ('0', 'No')])
    enviar = SubmitField('Enviar')
    
class LoginForm(FlaskForm):
    nombreapp = StringField('Nombre de usuario', validators=[data_required()])
    contraseña = PasswordField('Contraseña', validators=[data_required()])
    enviar = SubmitField('Enviar')
    
class PreciosForm(FlaskForm):
    mensual = IntegerField('Mensual:', validators=[data_required()])
    trimestral = IntegerField('Trimestral:', validators=[data_required()])
    anual = IntegerField('Anual', validators=[data_required()])
    enviar = SubmitField('Enviar')

class ClienteForm(FlaskForm):
    id = HiddenField('id')
    cedula = IntegerField('Cédula', validators=[data_required()])
    nombre = StringField('Nombre', validators=[data_required()])
    apellido = StringField('Apellido', validators=[data_required()])
    cumpleaños = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[data_required()])
    membresia = IntegerField('Membresía', validators=[data_required()])
    tipo_membresia = SelectField('Tipo de Membresía', choices=[('mensual', 'Mensual'), 
                                                            ('trimestral', 'Trimestral'), ('anual', 'Anual')])
    fecha_suscripcion =  DateField('Fecha de Suscripción', format='%Y-%m-%d', validators=[data_required()])
    enviar = SubmitField('Enviar')
    
    
    