from flask import Flask, render_template, request

app = Flask(__name__)

productos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def mostrar_productos():
    return render_template('productos.html', productos=productos)

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        productos.append({'nombre': nombre, 'categoria': categoria})
    return render_template('add_producto.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
