import pygame
from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector
from Engima import Enigma
from Draw import draw

#Setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

#Create fonts
MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

#global variables
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top":200, "bottom":100, "left":100, "right":100}
GAP = 100


INPUT = ""
OUTPUT = ""
PATH = []

# Historical Enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

#Keyboard and plugboard
KB = Keyboard()
PB = Plugboard(["BM"])

#Defines enigma machine
ENIGMA = Enigma(B, III, IV, V, PB, KB)

# Set the ring
ENIGMA.set_rings((1,1,1))

#Set message key
ENIGMA.set_key("DOG")

"""
# Enchiper message
message = "TESTINGTESTINGTESTINGTESTING"
cipher_text =""
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)
print(cipher_text)
"""

animating = True
while animating:
    #background    
    SCREEN.fill("#333333")
    
    #text input
    text = BOLD.render(INPUT, True, "grey")
    text_box = text.get_rect(center=(WIDTH/2, MARGINS["top"]/2) )
    SCREEN.blit(text, text_box)
    
    #text output
    text = MONO.render(OUTPUT, True, "grey")
    text_box = text.get_rect(center=(WIDTH/2, MARGINS["top"]/2+20) )
    SCREEN.blit(text, text_box)
    
    #Draw enigma machine
    draw(ENIGMA,PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # update screen
    pygame.display.flip()
    
    
    
    #track user input
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                II.rotate() 
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT = OUTPUT + cipher
                    