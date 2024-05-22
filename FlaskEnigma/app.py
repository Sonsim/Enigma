"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request
from Classes import Rotor, Reflector, Plugboard, Keyboard, EnigmaMachine
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

#Keyboard
KB = Keyboard.Keyboard()



@app.route('/')
def home():
    rotors = [I, II, III, IV, V]
    reflectors = [A, B, C]
    return render_template('start.html', rotors=rotors, reflectors=reflectors)
@app.route('/enigma', methods=["POST"])
def EnigmaApp():
    global ENIGMA

    
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

    letter1 = request.form.get('letter1')
    letter2 = request.form.get('letter2')
    
    PB = Plugboard.Plugboard([letter1.upper()+ letter2.upper()])

    key1 = request.form.get('keyletter1')
    key2 = request.form.get('keyletter2')
    key3 = request.form.get('keyletter3')
    
    ring1 = int(request.form.get('ring1'))
    ring2 = int(request.form.get('ring2'))
    ring3 = int(request.form.get('ring3'))
    
    ENIGMA = EnigmaMachine.EnigmaMachine(selected_reflector, selected_rotor1, selected_rotor2, selected_rotor3, PB, KB)
    
    
    ENIGMA.set_key(key1+key2+key3)
    ENIGMA.set_rings((ring1, ring2, ring3))

    return render_template('index.html', ENIGMA=ENIGMA)

@app.route('/enchipher', methods=["POST"])
def Convert():
    inputstring = request.form.get('inputstring')
    _Outputstring = ""
    for letter in inputstring.upper(): 
        cipher = ENIGMA.encipher(letter)
        _Outputstring = _Outputstring + cipher
    return render_template('index.html', ENIGMA=ENIGMA, output = _Outputstring)
    
    
    


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
