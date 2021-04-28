
class Shape:
    area = 0

    def __init__(self, bb_w, bb_h):
        self.bbox_width = bb_w
        self.bbox_height = bb_h
        self._private_field = "PRIVATE"

    #Only One constructor to a class
    # def __init__(self):
    #     print("default constructor")

    def set_bb_width(self, width):
        self.bbox_width= width


class Rectangle(Shape):

    def __init__(self, w, h):
        #Parent super() and invoke its constuctor
        super().__init__(w,h)
        self.width = w
        self.height= h
        self.area = w*h

    def __str__(self):
        return "Rectange object"

    @classmethod
    def create_square(cls, width):
        shape = Rectangle(width, width)
        print("pole a", cls.area)
        return shape



shape = Shape(3, 5)
shape = Rectangle(3, 5)
shape.area = 12
#shape.set_bb_width(33)
print(shape.area)
print(shape.bbox_width)
shape.i = 3
print(shape.i)
print(shape._private_field)
print(str(shape))
shape2 = Rectangle.create_square(13)
print(shape.area)
print(shape2.height, shape2.height)
shape2 = shape.create_square(13)

