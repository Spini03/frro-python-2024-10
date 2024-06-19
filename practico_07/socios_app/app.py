from flask import Flask, render_template, request, redirect, url_for, flash
from practico_06.capa_negocio import NegocioSocio, Socio

app = Flask(__name__)
app.secret_key = 'santi123'  # Para los flash messages

negocio_socio = NegocioSocio()

@app.route('/')
def index():
    socios = negocio_socio.todos()
    return render_template('index.html', socios=socios)

@app.route('/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        
        try:
            nuevo_socio = Socio(dni=dni, nombre=nombre, apellido=apellido)
            negocio_socio.alta(nuevo_socio)
            flash('Socio agregado exitosamente!')
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e))
            return redirect(url_for('alta'))
    
    return render_template('form.html', action="Alta")

@app.route('/baja/<int:id_socio>')
def baja(id_socio):
    try:
        negocio_socio.baja(id_socio)
        flash('Socio eliminado exitosamente!')
    except Exception as e:
        flash(str(e))
    
    return redirect(url_for('index'))

@app.route('/modificar/<int:id_socio>', methods=['GET', 'POST'])
def modificar(id_socio):
    socio = negocio_socio.buscar(id_socio)
    if request.method == 'POST':
        socio.dni = request.form['dni']
        socio.nombre = request.form['nombre']
        socio.apellido = request.form['apellido']
        
        try:
            negocio_socio.modificacion(socio)
            flash('Socio modificado exitosamente!')
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e))
            return redirect(url_for('modificar', id_socio=id_socio))
    
    return render_template('form.html', socio=socio, action="Modificar")

if __name__ == '__main__':
    app.run(debug=True)
