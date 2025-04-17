import sys
import unittest

def decrypt(cipher):
    result = []
    i = 0
    n = len(cipher)
    while i < n:
        if cipher[i] != '.':
            result.append(cipher[i])
            i += 1
        else:
            if i + 1 < n and cipher[i + 1] == '.':
                if result:
                    result.pop()
                i += 2
            else:
                i += 1
    return ''.join(result)

class TestDecrypt(unittest.TestCase):
    def test_no_dots(self):
        self.assertEqual(decrypt("абра-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("abc"), "abc")

    def test_single_dots(self):
        self.assertEqual(decrypt("абра."), "абра")
        self.assertEqual(decrypt("a.b.c"), "abc")
        self.assertEqual(decrypt("."), "")

    def test_double_dots(self):
        self.assertEqual(decrypt("абраа..-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абр......a."), "a")
        self.assertEqual(decrypt("1..2.3"), "23")

    def test_multiple_dots(self):
        self.assertEqual(decrypt("абраа..-.кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абра--..кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абрау...-кадабра"), "абра-кадабра")

    def test_edge_cases(self):
        self.assertEqual(decrypt("абра........"), "")
        self.assertEqual(decrypt("1......................."), "")
        self.assertEqual(decrypt(""), "")

    def test_spaces(self):
        self.assertEqual(decrypt(" абраа..-.кадабра"), " абра-кадабра")
        self.assertEqual(decrypt("  abc..def  "), "  abdef  ")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(decrypt(input_text))
    else:
        unittest.main()