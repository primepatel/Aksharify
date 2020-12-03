from PIL import Image

class AsciiArt:
    def __init__(self, image) -> None:
        self.image = Image.open(image)
        self.w, self.h = self.image.size
        self.ascii_chars = list('01')
        self.ascii_text = ''
        self.number = ""
        self.ascii_html = ''

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
    
    def primify(self, prime, binary=False):
        if binary and len(bin(int(prime))) == len(bin(self.number)):
            self.number = bin(int(prime))
        elif len(str(int(prime))) == len(str(self.number)):
            self.number = str(prime)
        else:
            print("not primified")
    
    def prime_asciify(self):
        self.ascii_text = ""
        for line in range(self.h):
            for dig in range(line*self.w, line*self.w + self.w):
                self.ascii_text += self.number[dig]
            self.ascii_text += '\n'
    
    def colorify(self):
        color = self.image.getdata()
        file = '<p>'
        if self.number[:2] != "0b":
            for line_no in range(self.h):
                for pixel in range(line_no*self.w, line_no*self.w + self.w):
                    file += self.span(self.number[pixel], color[pixel])
                file += '<br>'
        else:
            for line_no in range(self.h):
                for pixel in range(line_no*self.w, line_no*self.w + self.w):
                    file += self.span(self.number[2+pixel], color[pixel])
                file += '<br>'
        file += "</p>"
        self.ascii_html = file
    
    def ascii_show(self):
        print(self.ascii_text[:-1])

    def text_output(self, fname):
        with open(fname, "w") as file:
            file.write(self.ascii_text)

art = AsciiArt("img.png")
art.set_dim(20)
art.asciify()
art.ascii_show()
print()
art.primify(int(art.numberize()) + 1)
art.prime_asciify()
art.ascii_show()
art.text_output("text.txt")
art.colorify()