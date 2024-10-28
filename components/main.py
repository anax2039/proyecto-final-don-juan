from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def desarrolladora():
    return render_template('principal.html')

#RUTA A SOBREMI
@app.route("/sobremi")
def sobremi():
    return render_template('sobremi.html')

#RUTA PARA LEGUAJES
@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html')

#RUTA A PORTAFOLIO
@app.route("/portafolio")
def portafolio():
    return render_template('portafolio.html')

#RUTA A CONTACTANOS
@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

#RUTA A LOGIN
@app.route('/login')
def login():
    return render_template('login.html')   

if __name__=='__main__':
    app.run(debug=True)
