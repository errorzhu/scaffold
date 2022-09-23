import zlib
import lzma


class ZlibCompressor(object):
    def compress(self, data):
        return zlib.compress(data)

    def decompress(self, data):
        return zlib.decompress(data)


class LzmaCompressor(object):
    def compress(self, data):
        return lzma.compress(data)

    def decompress(self, data):
        return lzma.decompress(data)


class Compressor(object):
    @staticmethod
    def get_instance(type):
        if type == "zlib":
            return ZlibCompressor()
        if type == "lzma":
            return LzmaCompressor()
