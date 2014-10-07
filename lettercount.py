from sys import argv

script, filename = argv

def main():

    text = open(filename)
    filetext = text.read()
    filetext.lower()
    text.close()

    full_text = [0]*26

    for char in filetext:
        if ord(char) in range(97,123):
            index = ord(char) - ord('a')
            full_text[index] += 1

    print full_text


if __name__ == '__main__':
    main()



