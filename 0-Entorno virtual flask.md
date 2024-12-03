1. crear entorno virtual
    python -m venv env   #donde env es el nombre del entorno virtual

2. activar el entorno virtual
    env/scripts/activate  #para windows

3. instalar flask
    pip install flask

4. instalar mysql-connector para conectarse a mysql
    python -m pip install mysql-connector-python # 

5. instalar flask-wtf para manejar formularios se debe instalar la extencion WTForms
    python -m pip install flask-wtf

6. Para trabajar con login en flask
    pip install flask-login
    
# Establece la variable de entorno FLASK_APP para indicar el archivo de tu aplicación
set FLASK_APP=app.py  # Reemplaza "app.py" con el nombre de tu archivo principal si es diferente

# Establece la variable de entorno FLASK_ENV en development
set FLASK_ENV=development

# Ejecuta el servidor de desarrollo
flask run

6. correr el servidor
    flask run

7. ejecutar el servidor flask, en modo dev se activa debugger
    flask --debug run

8. cuando se trabaja con templates se debe crear una carpeta llamada templates

9. ¿Cómo generar una clave secreta con Python?
    python -c 'import os; print(os.urandom(16))'