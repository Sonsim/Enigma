class Keyboard: 
    
    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal
    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter
    def to_dict(self):
        return {}


