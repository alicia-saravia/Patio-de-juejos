from Patio_de_juegos import app
from flask import render_template, request, redirect


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

'''
@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<cantidad>')
def play_cantidad(cantidad):
    veces = int(cantidad)
    return render_template("cantidad.html",veces=veces)
'''
@app.route('/play')
@app.route('/play/<cantidad>')
@app.route('/play/<cantidad>/<color>')
def play_color(cantidad=3,color="aquamarine"):
    veces = int(cantidad)
    return render_template("color.html",veces=veces,color=color)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404