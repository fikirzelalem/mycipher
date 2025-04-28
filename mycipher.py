import sys

def main():
    shift = int(sys.argv[1])
    text = ""
    for line in sys.stdin:
        text += line.strip()

    text = text.upper()
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if shifted > ord('Z'):
                shifted -= 26
            encrypted += chr(shifted)

    for i in range(0, len(encrypted), 5):
        print(encrypted[i:i+5], end=' ')
        if (i // 5 + 1) % 10 == 0:
            print()

if __name__ == "__main__":
    main()
