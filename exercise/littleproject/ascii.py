from PIL import Image
import argparse

#字符画的字符集，采用顺序排列，小的灰度值用初始值代替，大的灰度值用的大的值代替
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#rgb转换成灰度值，采用 gray = 0.2126 * r + 0.7152 * g + 0.0722 * b


def get_ascii(r, g, b, alpha = 255):
    if alpha == 0:
        return ""
    length = len(ascii_char)
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    #每个灰度值间隔的大小
    unit = (255.0) / length

    return ascii_char[int(gray / unit)]


def read_image(image_address):
    image = Image.open(image_address)

def main():
    read_image("C:\\Users\\zhangcheng\\Pictures\\test.jpeg")


if __name__ == "__main__":
    main()


