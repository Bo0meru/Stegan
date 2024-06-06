import secrets
import string

from PIL import Image, ImageDraw
import numpy as np


def read_color(img_path, color_metod):

    img = Image.open(img_path)
    img_pix = img.load()

    width = img.size[0]
    height = img.size[1]

    red = []
    green = []
    blue = []
    for x in range(width):
        for y in range(height):
            r, g, b = img_pix[x, y]
            red.append(r)
            green.append(g)
            blue.append(b)

    img.close()

    if color_metod == 'red':
        return red
    elif color_metod == 'green':
        return green
    elif color_metod == 'blue':
        return blue
    elif color_metod == 'pixels':
        data = []
        for i in range(len(red)):
            data.append(red[i])
            data.append(green[i])
            data.append(blue[i])
        return data
    else:
        return red + green + blue


def save_color(img_old_path, img_new_path, img_pix_new, color_metod):


    img = Image.open(img_old_path)
    img_draw = ImageDraw.Draw(img)
    img_pix = img.load()

    width = img.size[0]
    height = img.size[1]

    index = 0
    for x in range(width):
        for y in range(height):
            r, g, b = img_pix[x, y]
            if color_metod == 'red':
                img_draw.point((x, y), (img_pix_new, g, b))
            elif color_metod == 'green':
                img_draw.point((x, y), (r, img_pix_new, b))
            elif color_metod == 'blue':
                img_draw.point((x, y), (r, g, img_pix_new))
            elif color_metod == 'pixels':
                red = img_pix_new[index]
                green = img_pix_new[index+1]
                blue = img_pix_new[index+2]
                img_draw.point((x, y), (red, green, blue))
                index += 3
            else:
                red = img_pix_new[0:len(r)]
                green = img_pix_new[len(r):len(g)]
                blue = img_pix_new[len(g):]
                img_draw.point((x, y), (red, green, blue))

    img.save(img_new_path, "BMP")
    img.close()


def get_size(img_path):

    img = Image.open(img_path)
    width = img.size[0]
    height = img.size[1]
    img.close()

    return width, height


def text_to_binary(text):


    text = text.encode("utf-8")
    data = []
    for c in text:
        data.append(c)
    return data


def binary_to_text(data):

    return bytes(data).decode("utf-8")


def number_to_bin_arr(data):


    return [1 if data & (1 << (7 - n)) else 0 for n in range(8)]


def bin_arr_to_number(data):


    out = 0
    for bit in data:
        out = (out << 1) | bit
    return out


def set_bit(value, bit):

    """
  операция побитового сдвига. Она сдвигает число 1 влево на bit позиций, создавая число, у которого только один бит равен 1, а остальные — 0
    операция побитового ИЛИ (OR). Она устанавливает бит на позиции bit в числе value в 1, независимо от его предыдущего значени
    """

    return value | (1<<bit)


def clear_bit(value, bit):
    """
перация побитового отрицания (NOT). Она инвертирует все биты, создавая маску, где все биты равны 1, кроме одного, который равен 0 операция побитового И (AND). Она очищает бит на позиции bit в числе value, устанавливая его в 0, независимо от его предыдущего значения     """

    return value & ~(1<<bit)


def find_SubarrayStartIndex(array, subArray):


    index = -1
    for i in range(len(array) - len(subArray) + 1):
        index = i
        for j in range(len(subArray)):
            if array[i + j] != subArray[j]:
                index = -1
                break
        if index >= 0:
            return index
    return -1


def subarr_extract(bit_start, arr, bit_end):


    index_bs = find_SubarrayStartIndex(arr, bit_start)
    index_be = find_SubarrayStartIndex(arr, bit_end)
    return arr[index_bs+len(bit_start):index_be]


def retn_bit(num, pos):

    array_bit = number_to_bin_arr(num)
    return array_bit[pos]


def mod_on_2(vector):

    div_vector = vector.copy()
    div_vector.fill(2)
    return np.remainder(vector, div_vector)


def reverse_bit(vector, index):

    if index == -1:
        return vector
    if vector[index] == 1:
        vector[index] = 0
    else:
        vector[index] = 1
    return vector


def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits + string.punctuation
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    return crypt_rand_string