class Drawing:

    def __init__(self, width, length, symb):
        self.width = width
        self.length = length
        self.img = []
        #for i in range(length):
        self.img = list(list(symb for i in range(width)) for i in range(length))
        #self.img.append(row)

    def print(self):
        for i in range(self.length):
            for j in range(self.width):
                print(self.img[i][j], end=' ')
            print()


    def setPoint(self, x, y, char):
        self.img[x][y] = char

    def drawVerticalLine(self, x1, x2, y, char):
        for j in range(x1, x2 + 1):
            self.img[j][y] = char

    def drawHorizontalLine(self, x, y1, y2, char):
        for i in range(y1, y2 + 1):
            self.img[x][i] = char

    def drawRectangle(self, x1, x2, y1, y2, char):
        self.drawHorizontalLine(x1, y1, y2, char)
        self.drawHorizontalLine(x2, y1, y2, char)
        self.drawVerticalLine(x1, x2, y1, char)
        self.drawVerticalLine(x1, x2, y2, char)

    def drawLine(self, x0, x1, y0, y1, char):
        delx = abs(x1 - x0)
        dely = abs(y1 - y0)
        err = 0
        delerr = (dely + 1)
        y = y0
        diry = y1 - y0
        if diry > 0:
            diry = 1
        if diry < 0:
            diry = -1
        for x in range(x0, x1 +1):
            self.setPoint(x, y, char)
            err = err + delerr
            if err >= (delx + 1):
                y = y + diry
                err = err - (delx + 1)

    def drawCircle(self, X1, Y1, R, char):
        x = 0
        y = R
        delta = 1 - 2 * R
        err = 0
        while y >= x:
            self.setPoint(X1 + x, Y1 + y, char)
            self.setPoint(X1 + x, Y1 - y, char)
            self.setPoint(X1 - x, Y1 + y, char)
            self.setPoint(X1 - x, Y1 - y, char)
            self.setPoint(X1 + y, Y1 + x, char)
            self.setPoint(X1 + y, Y1 - x, char)
            self.setPoint(X1 - y, Y1 + x, char)
            self.setPoint(X1 - y, Y1 - x, char)
            err = 2 * (delta + y) - 1
            if delta < 0 and err <= 0:
                x += 1
                delta += 2 * x + 1
                continue
            if delta > 0 and err > 0:
                y -= 1
                delta -= 2 * y + 1
                continue
            x += 1
            y -= 1
            delta += 2 * (x - y)

    def draw(self, x, y, drawing, char):
        for i in range(x, self.length):
            for j in range(y, self.width):
                if drawing.img[i - x][j - y] != char:
                    self.img[i][j] = drawing.img[i - x][j - y]






d1 = Drawing(20, 20, ".")
d2 = Drawing(20, 20, ".")
d3 = Drawing(20, 20, ".")
d4 = Drawing(20, 20, ".")
d5 = Drawing(20, 20, ".")
d6 = Drawing(20, 20, ".")
d7 = Drawing(20, 20, ".")
d8 = Drawing(20, 20, ".")





d1.print()
print("img")
d2.setPoint(2, 14, "x")
d2.print()
print("vertical line")
d3.drawVerticalLine(4, 17, 7, "x")
d3.print()
print("horizontal line")
d4.drawHorizontalLine(1, 1, 4, "x")
d4.print()
print("rectangle")
d5.drawRectangle(0, 4, 0, 4, "x")
d5.print()
print("line")
d6.drawLine(1, 4, 0, 2, "x")
d6.print()
print("circle")
d7.drawCircle(9, 9, 7, "x")
d7.print()
print("pic in pic")
d8.drawHorizontalLine(9,0,19,'o')
d9 = Drawing(20,20,'.')
d9.drawCircle(9, 9, 7, "x")
d8.draw(0,0, d9, '.')
d8.print()
print("house")
d1.drawRectangle(8, 18, 3, 13, "x")
d1.drawRectangle(10, 12, 5, 7, "x")
d1.drawRectangle(14, 18, 8, 11, "x")
d1.drawLine(3, 8, 8, 3, "x")
d1.drawLine(3, 8, 8, 13, "x")
d1.print()