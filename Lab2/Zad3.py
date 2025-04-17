import sys

def decrypt(cipher):
    result = []
    i = 0
    n = len(cipher)
    while i < n:
        if cipher[i] != '.':
            result.append(cipher[i])
            i += 1
        else:
            if i + 1 < n and cipher[i+1] == '.':
                if result:
                    result.pop()
                i += 2
            else:
                i += 1
    return ''.join(result)

if __name__ == "__main__":
    input_text = sys.stdin.read().strip()
    print(decrypt(input_text))