class Caesar:
    def __init__(self, shift):
        self._shift = shift % 26

    def encrypt(self, data):
        encryptedText = ''
        for char in data:
            if char.isalpha():
                encryptedChar = chr(ord(char) + self._shift)
                if ord(encryptedChar) > 122:
                    encryptedChar = chr(ord(encryptedChar) - 26)
                encryptedText += encryptedChar
            else:
                encryptedText += char
        return encryptedText

    def decrypt(self, data):
        decryptedText = ''
        for char in data:
            if char.isalpha():
                decryptedChar = chr(ord(char) - self._shift)
                if ord(decryptedChar) < 97:
                    decryptedChar = chr(ord(decryptedChar) + 26)
                decryptedText += decryptedChar
            else:
                decryptedText += char
        return decryptedText
