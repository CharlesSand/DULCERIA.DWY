import mantenedorUsuario
import claseUsuario
from flask import Flask, render_template,request,flash,redirect,url_for

app = Flask(__name__)

@app.route('/')

def Index():
    return render_template("Usuario.html")

@app.route('/mantenedor',methods=['POST'])

def mantenedor():
    if request.method == 'POST':
        try:
            auxBotonInsertar = request.form['btnGuardar']
            if auxBotonInsertar == "Guardar":
                auxId = request.form['txtId']
                auxNombre = request.form['txtNombre']
                auxRut = request.form['txtRut']
                auxUsuario = claseUsuario.Usuario(auxId,auxNombre,auxRut)
                mantenedorUsuario.insertar(auxUsuario)
                print("Datos guardados")
                flash('datos guardados')
        except:
            print("datos no guardados")
        
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(port=3000,debug=True)