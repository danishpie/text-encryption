class CaesarCipher:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, message):
        return self.caesar(message, self.shift)
    
    def decrypt(self, message):
        return self.caesar(message, -self.shift)

    def caesar(self, message, shift):
        result = []
        for char in message.lower():
            if char.isalpha():
                index = (self.alphabet.index(char) + shift) % 26
                result.append(self.alphabet[index])
            else:
                result.append(char)
        return ''.join(result)
    
class VigenereCipher:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, key):
        self.key = [ord(k) - ord('a') for k in key.lower() if k.isalpha()]

    def encrypt(self, message):
        return self.vigenere(message, 1)
    
    def decrypt(self, message):
        return self.vigenere(message, -1)
    
    def vigenere(self, message, direction):
        result = []
        key_index = 0
        for char in message.lower():
            if char.isalpha():
                key_shift = self.key[key_index % len(self.key)]
                index = (self.alphabet.index(char) + direction * key_shift) % 26
                result.append(self.alphabet[index])
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)