from PIL import Image

img = Image.open("img.png")

w, h = img.size

def set_dim(width=0, height=0):
    global w, h, img
    if width == 0 and height != 0:
        w, h = int(w/h * height), height * 0.5
    elif width != 0 and height == 0:
        w, h = width, int(h/w * width * 0.5) 
    else:
        w, h = width, height
    img = img.resize((w, h))

set_dim(80)
img = img.convert('L')
bwdata = img.getdata()
chars = ["0", "1", "2"]


def binary_to_decimal(binary):
        decimal = 0
        l = len(binary)
        for x in binary:
            l -= 1
            decimal += pow(2, l) * int(x)
        return int(decimal)

text = ""
div = 255//len(chars)
for line_no in range(int(h)):
    for p in range(line_no*w, line_no*w + w):
        try:
            text += chars[bwdata[p]//div -1]
        except IndexError:
            print(bwdata[p], div)
    text += '\n'

with open("text.txt", "w") as file:
    file.write(text)