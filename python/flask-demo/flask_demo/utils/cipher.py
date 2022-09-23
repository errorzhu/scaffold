import base64
import hashlib

from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto import Random

from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad


class Base64Cipher(object):
    def encrypt(self, data):
        return base64.b64encode(data)

    def decrypt(self, data):
        return base64.b64decode(data)


class AesCipher(object):
    def __init__(self):
        self.key = hashlib.sha256("zhuyu,fool".encode()).digest()
        self.iv = Random.new().read(AES.block_size)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        raw = pad(data, AES.block_size, style="pkcs7")
        return cipher.encrypt(raw)

    def decrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(data), AES.block_size, style="pkcs7")


class DesCipher(object):
    def _pad_key(self, key):
        if len(key) > 8:
            return key[:8]
        while len(key) % 8 != 0:
            key += " "
        return key

    def __init__(self):
        self.key = self._pad_key("zhuyu,fool").encode()
        self.iv = Random.new().read(DES.block_size)

    def encrypt(self, data):
        cipher = DES.new(self.key, DES.MODE_CBC, self.iv)
        raw = pad(data, DES.block_size, style="pkcs7")
        return cipher.encrypt(raw)

    def decrypt(self, data):
        cipher = DES.new(self.key, DES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(data), DES.block_size, style="pkcs7")


class Cipher(object):
    def __init__(self):
        pass

    @staticmethod
    def get_instance(type):
        if type == "base64":
            return Base64Cipher()
        if type == "aes":
            return AesCipher()
        if type == "des":
            return DesCipher()
