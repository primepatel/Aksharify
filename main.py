from PIL import Image

img = Image.open("img.png")

w, h = img.size
aspect_ratio = h/w
w = 120
h = aspect_ratio * w * 0.5
img = img.resize((w, int(h)))
img = img.convert('L')
bwdata = img.getdata()
chars = ["0", "1"]

text = ""
div = 255//2
for line_no in range(int(h)):
    for p in range(line_no*w, line_no*w + w):
        try:
            text += chars[bwdata[p]//div -1]
        except IndexError:
            print(bwdata[p], div)
    text += '\n'

with open("text.txt", "w") as file:
    file.write(text)