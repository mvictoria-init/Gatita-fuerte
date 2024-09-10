from flask import Flask, render_template, redirect, url_for

from usuario import Usuario
from usuario_dao import UsuarioDao
from precios import Precios
from precios_dao import PreciosDao
from cliente import Cliente
from cliente_dao import ClienteDAO
from forms import UsuarioForm, LoginForm, PreciosForm, MostrarForm, ClienteForm

app = Flask(__name__)

titulo_app = 'Kitty Stronger (GYM)'
app.config['SECRET_KEY'] = '\x17?4S\xcd\xbeF\x89\xa4\xc9 .\xd0\x93\x08\x8b'

@app.route('/')
def inicio():
    
    # formulario
    usuario = Usuario()
    usuario_forma = UsuarioForm(obj= usuario)
    
    return render_template('inicio.html', forma=usuario_forma, titulo=titulo_app)

@app.route('/login', methods=['POST'])
def login():
    
    # formulario
    usuario = Usuario()
    usuario_forma = LoginForm(obj= usuario)
    app.logger.debug('Entramos a la funcion login...')
    
    if usuario_forma.validate_on_submit():
        usuario_forma.populate_obj(usuario)
        app.logger.debug('Llenamos los datos...')
        
        nombreapp =  usuario_forma.nombreapp.data
        contraseña =  usuario_forma.contraseña.data
        
        try:
            
            nombre, clave, admin = UsuarioDao.acceder_bd(usuario)
            if nombreapp == nombre and contraseña == clave and admin == 1:
                app.logger.debug('EL usuario y contraseña son validos...')
                return redirect(url_for('admin'))
            
            elif nombreapp == nombre and contraseña == clave:
                return redirect(url_for('clientes'))

        except:
            app.logger.debug('EL usuario y contraseña no son validos...')
            return redirect(url_for('error_login'))

    return redirect(url_for('error_login'))

@app.route('/logine')
def error_login():
    
    # formulario
    usuario = Usuario()
    usuario_forma = LoginForm(obj= usuario)
    
    return render_template('error_login.html', forma=usuario_forma, titulo=titulo_app)

@app.route('/clientes')
def clientes():
    
   # precios
    precio = PreciosDao.mostrar_precios()
    precio_forma = MostrarForm(obj=precio)
    
    # clientes
    clientes_db = ClienteDAO.seleccionar()
    
    return render_template('clientes.html', titulo=titulo_app, precio=precio_forma, clientes=clientes_db)

@app.route('/agregar')
def agregar():
    app.logger.debug('Entramos a agregar cliente...')
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    
    return render_template('agregar.html', titulo=titulo_app, cliente=cliente_forma)

@app.route('/guardarcliente', methods=['POST'])
def guardar_cliente():
    # creamos los objetos vacios del cliente
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    if cliente_forma.validate_on_submit():
        
        cliente_forma.populate_obj(cliente) 
        if not cliente.id: 
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)  
            
    return redirect(url_for('clientes'))

@app.route('/editarcliente/<int:id>')
def editar_cliente(id):
    
    app.logger.debug('Entramos a editar cliente...')
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    
    return render_template('agregar.html', titulo=titulo_app, cliente=cliente_forma)

@app.route('/eliminarcliente/<int:id>') 
def eliminar_cliente(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('clientes'))

@app.route('/admin')
def admin():
    
    # formulario
    usuario = Usuario()
    usuario_forma = UsuarioForm(obj= usuario)
    
    # usuarios en base de datos
    usuarios_db = UsuarioDao.consultar_bd()
    
    # precios
    precio = PreciosDao.mostrar_precios()
    precio_forma = PreciosForm(obj=precio)
    
    return render_template('admin.html', titulo=titulo_app, usuarios=usuarios_db, forma=usuario_forma, precio=precio_forma)

@app.route('/actualizarprecio', methods=['POST'])
def actualizar_precio():

    app.logger.debug('Entramos a actualizar_precio...')
    precio = Precios()
    precio_forma = PreciosForm(obj=precio)
    
    if precio_forma.validate_on_submit():
        precio_forma.populate_obj(precio)
        
        app.logger.debug('Llenamos los datos...')
        
        mensual =  precio_forma.mensual.data
        trimestral =  precio_forma.trimestral.data
        anual =  precio_forma.anual.data
        
        if mensual>0 and trimestral>0 and anual>0:
            app.logger.debug('Se actualizaron los precios...')
            PreciosDao.actualizar_precios(precio)
        else:
            app.logger.debug('No se actualizaron los precios...')
            return redirect(url_for('admin'))
    return redirect(url_for('admin')) 

@app.route('/guardar', methods=['POST'])
def guardar():
    
    app.logger.debug('Entramos a la funcion guardar...')
    usuario = Usuario()
    usuario_forma = UsuarioForm(obj=usuario)

    if usuario_forma.validate_on_submit():
        
        usuario_forma.populate_obj(usuario)
        app.logger.debug('Llenamos los datos...')
        
        if not usuario.id: #si el id es cadena vacia regresa verdadero
            # guardamos el nuevo cliente en la base de datos
            UsuarioDao.insertar_bd(usuario)
            app.logger.debug('Se agregó el usuario a la base de datos')
            
        else:
            # actualizamos el cliente en la base de datos
            UsuarioDao.actualizar_bd(usuario)  
            app.logger.debug('Se actualizó el usuario de la base de datos')
    else:
        app.logger.error('Formulario inválido')
        app.logger.debug(usuario_forma.errors)
        
    return redirect(url_for('admin')) 

@app.route('/editar/<int:id>')
def editar(id):
    
    app.logger.debug('Entramos a la funcion editar...')
    usuario = UsuarioDao.seleccionar_por_id(id)
    usuario_forma = UsuarioForm(obj=usuario)

    # usuarios en base de datos
    usuarios_db = UsuarioDao.consultar_bd()
    
    # precios
    precio = PreciosDao.mostrar_precios()
    precio_forma = PreciosForm(obj=precio)
    
    return render_template('admin.html', titulo=titulo_app, usuarios=usuarios_db, forma=usuario_forma, precio=precio_forma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    
    usuario = Usuario(id=id)
    UsuarioDao.eliminar_bd(usuario)
    
    return redirect(url_for('admin'))
 
if __name__ == '__name__':
    app.run(debug=True)