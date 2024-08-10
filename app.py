from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal para mostrar el formulario y manejar la solicitud POST
@app.route('/', methods=['GET', 'POST'])
def loan_request():
    if request.method == 'POST':
        # Obtener datos del formulario
        motivo = request.form.get('motivo')
        monto = request.form.get('monto')
        cuotas = request.form.get('cuotas')
        descripcion = request.form.get('descripcion')
        print(f"Motivo: {motivo}")
        print(f"Monto: {monto}")
        print(f"Cuotas: {cuotas}")
        print(f"Descripción: {descripcion}")
        
        # Redirigir después de procesar el formulario
        return redirect(url_for('loan_request'))
    
    return render_template('form.html')

@app.route('/future', methods=['GET', 'POST'])
def future_request():
    if request.method == 'POST':

        data = request.form
        return redirect(url_for('future_request'))
    
    return render_template('future_form.html')

if __name__ == '__main__':
    app.run(debug=True)