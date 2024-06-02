""" TD08 """
import struct


def read_file(fichier):
    data = open(fichier, "rb").read()
    # "rb" pour binaire
    start = data.find(b"data") + 8
    # "+8" pour "data" et sa taille
    right = []
    left = []
    size_data = struct.unpack("I", data[start - 4: start])[0]
    # On récupère la taille de data
    for i in range(size_data // 4):
        canaux = struct.unpack("hh", data[start + 4 * i: start + 4 * (i + 1)])
        # tuple de deux entiers pour deux canaux
        left.append(canaux[0])
        right.append(canaux[1])
    print(len(left))
    return left, right


def reverse(left, right, fichier):
    with open(fichier, "wb") as f:
        f.write(b"RIFF")
        f.write(struct.pack("I", 44 - 8 + len(left) * 4))
        f.write(b"WAVEfmt ")
        f.write(struct.pack("IHHIIHH", 16, 1, 2, 44100, 176400, 4, 16))

        '''
        16 : number of already written bytes,
        1 : data type encoding, 1=PCM
        2 : channel number
        44100 : sample rate
        176400 : 44100*4 : number of bytes per second
        4 : number of bytes per sample
        16 : number of bits per sample

        '''
        f.write(b"data")
        f.write(struct.pack("I", len(left) * 4))
        # 4 bytes par sample
        for i in range(len(left)):
            f.write(struct.pack("hh", right[i], left[i]))
            # on inverse les canaux en écrivant les composantes "right" à gauche et "left" à droite.


def half(left, right, fichier):
    with open(fichier, "wb") as f:
        f.write(b"RIFF")
        f.write(struct.pack("I", 44 - 8 + len(left) * 4))
        f.write(b"WAVEfmt ")
        f.write(struct.pack("IHHIIHH", 16, 1, 2, 44100, 176400, 4, 16))

        '''
        16 : number of already written bytes,
        1 : data type encoding, 1=PCM
        2 : channel number
        44100 : sample rate
        176400 : 44100*4 : number of bytes per second
        4 : number of bytes per sample
        16 : number of bits per sample

        '''
        f.write(b"data")
        f.write(struct.pack("I", len(left) * 4 // 2))
        # On divise par deux le nombre d'information donc on divise par deux la taille du fichier
        for i in range(len(left) // 2):
            f.write(struct.pack("hh", left[2 * i], right[2 * i]))


def double(left, right, fichier):
    with open(fichier, "wb") as f:
        f.write(b"RIFF")
        f.write(struct.pack("I", 44 - 8 + len(left) * 4))
        f.write(b"WAVEfmt ")
        f.write(struct.pack("IHHIIHH", 16, 1, 2, 44100, 176400, 4, 16))

        '''
        16 : number of already written bytes,
        1 : data type encoding, 1=PCM
        2 : channel number
        44100 : sample rate
        176400 : 44100*4 : number of bytes per second
        4 : number of bytes per sample
        16 : number of bits per sample

        '''
        f.write(b"data")
        f.write(struct.pack("I", len(left) * 4 * 2))
        # On double le nombre d'information donc on double la taille du fichier
        for i in range(len(left) - 1):
            f.write(struct.pack("hh", left[i], right[i]))
            f.write(struct.pack("hh", (left[i+1] + left[i])//2, (right[i+1] + right[i])//2))
            # interpolation linéaire
        f.write(struct.pack("hh", left[-1], right[-1]))


""" Exercice 1 """
read_file('the_wall.wav')


""" Exercice 2 """
left1 = read_file('the_wall.wav')[0]
right1 = read_file('the_wall.wav')[1]
reverse(left1, right1, 'the_wall_reverse.wav')
# On obtient bien des canaux inversés, on l'entend surtout de 30 à 40 secondes


""" Exercice 3 """
half(left1, right1, 'the_wall_half.wav')
# Une information sur deux est présente: le son dure deux fois moins longtemps, mais tout le morceau est la: fréquence*2


""" Exercice 4 """
double(left1, right1, 'the_wall_double.wav')
# Deux fois plus d'information: la fréquence est divisé par deux et le temps multiplié par deux

