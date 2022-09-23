import pytest
from flask_demo.utils.cipher import Cipher


def test_base64():
    raw = "zhuyu is foolish"
    cipher = Cipher.get_instance("base64")
    encrypted = cipher.encrypt(raw.encode())
    assert raw == cipher.decrypt(encrypted).decode()


def test_aes():
    raw = "zhuyu is foolish"
    cipher = Cipher.get_instance("aes")
    encrypted = cipher.encrypt(raw.encode())
    assert raw == cipher.decrypt(encrypted).decode()

def test_des():
    raw = "zhuyu is foolish"
    cipher = Cipher.get_instance("des")
    encrypted = cipher.encrypt(raw.encode())
    assert raw == cipher.decrypt(encrypted).decode()


if __name__ == "__main__":
    pytest.main(["./test_cipher.py"])
