from sys import argv

script, filename = argv

def main():

    text = open(filename)
    filetext = text.read()
    filetext = filetext.lower()
    text.close()

    full_text = [0]*26
    ORD_A = ord('a')
    for char in filetext:
        if 97 <= ord(char) <= 122: 
            index = ord(char) - ORD_A
            full_text[index] += 1

    print full_text


if __name__ == '__main__':
    main()



