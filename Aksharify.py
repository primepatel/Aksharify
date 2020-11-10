from PIL import Image

class AsciiArt:
    def __init__(self, image) -> None:
        self.image = Image.open(image)
        self.w, self.h = self.image.size
        self.ascii_chars = list('01')
        self.ascii_text = ''
        self.number = ""

    def set_dim(self, width=0, hight=0):
        if width == 0 and hight != 0:
            self.w, self.h = int(self.w/self.h * hight), hight
        elif width != 0 and hight == 0:
            self.w, self.h = width, int(self.h/self.w * width)
        else:
            self.w, self.h = width, hight
        self.image = self.image.resize((self.w, self.h))

    def binary_to_decimal(self, binary):
        decimal = 0
        l = len(binary)
        for x in binary:
            l -= 1
            decimal += pow(2, l) * int(x)
        return int(decimal)

    def span(self, integer, integer_colour):
        return f"<span style='color: rgb{integer_colour};'><b>{integer}</b></span>"
    
    def asciify(self):
        div = 255//(len(self.ascii_chars))
        bwdata = self.image.convert('L').getdata()
        for line_no in range(self.h):
            for pixel in range(line_no*self.w, line_no*self.w + self.w):
                self.ascii_text += self.ascii_chars[bwdata[pixel]//div -1]
            self.ascii_text += '\n'
    
    def numberize(self, first_char=1):
        div, number = 255//len(self.ascii_chars), ''
        bwdata = self.image.convert('L').getdata()
        for line_no in range(self.h):
            for pixel in range(line_no*self.w, line_no*self.w + self.w):
                number += self.ascii_chars[bwdata[pixel]//div - 1]
                self.ascii_text += self.ascii_chars[bwdata[pixel]//div - 1]
            self.ascii_text += '\n'
        if number[0] == "0":
            number = str(first_char) + number[1:]
        self.number = number
        return self.number
    
    def ascii_show(self):
        print(self.ascii_text[:-1])

art = AsciiArt("img.png")
art.set_dim(40)
art.asciify()
art.ascii_show()
print(art.numberize())