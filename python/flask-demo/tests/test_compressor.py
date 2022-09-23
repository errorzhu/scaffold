import pytest

from flask_demo.utils.compressor import Compressor


def test_zlib():
    raw = "zhuyu is foolish"
    compressor = Compressor.get_instance("zlib")
    result = compressor.compress(raw.encode())
    assert raw == compressor.decompress(result).decode()


def test_lzma():
    raw = "zhuyu is foolish"
    compressor = Compressor.get_instance("lzma")
    result = compressor.compress(raw.encode())
    assert raw == compressor.decompress(result).decode()


if __name__ == "__main__":
    pytest.main(["./test_compressor.py"])
