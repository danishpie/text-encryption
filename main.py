class CaesarCipher:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, message):
        return self._cipher(message, self.shift)
    
    def decrypt(self, message):
        return self._cipher(message, -self.shift)

    def _cipher(self, message, shift):
        result = []
        for char in message.lower():
            if char.isalpha():
                index = (self.alphabet.index(char) + shift) % 26
                result.append(self.alphabet[index])
            else:
                result.append(char)
        return ''.join(result)
    
caesar = CaesarCipher(3)
encrypted = caesar.encrypt("Hello Everyone")
print(encrypted)
decrypted = caesar.decrypt(encrypted)
print(decrypted)