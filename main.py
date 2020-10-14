from PIL import Image

img = Image.open("img.png")

w, h = img.size
aspect_ratio = h/w
w = 120
h = aspect_ratio * w * 0.5
img = img.resize((w, int(h)))
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