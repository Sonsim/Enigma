"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request
from Classes import Rotor, Reflector
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# Historical Enigma rotors and reflectors
I = Rotor.Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor.Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor.Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor.Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor.Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector.Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector.Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector.Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

@app.route('/')
def home():
    rotors = [I, II, III, IV, V]
    reflectors = [A, B, C]
    return render_template('start.html', rotors=rotors, reflectors=reflectors)
@app.route('/enigma', methods=["POST"])
def EnigmaApp():
    rotor1 = int(request.form.get('rotor1'))
    rotor2 = int(request.form.get('rotor2'))
    rotor3 = int(request.form.get('rotor3'))
    reflector = int(request.form.get('reflector'))
    mainrotors = [I, II, III, IV, V]
    reflectors = [A, B, C]
    rotors = []
    selected_rotor1 = mainrotors[rotor1 - 1]
    selected_rotor2 = mainrotors[rotor2 - 1]
    selected_rotor3 = mainrotors[rotor3 - 1]
    selected_reflector = reflectors[reflector -1]
    
    rotors.append(selected_rotor1)
    rotors.append(selected_rotor2)
    rotors.append(selected_rotor3)

    return render_template('index.html', rotors=rotors, reflector=selected_reflector)
    
    


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
