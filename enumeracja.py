from enum import Enum

from klasy import Rectangle


class Shape_Types(Enum):
    RECTANGLE = 1
    SQUARE = 2
    CIRCLE = 3

    def __str__(self):
        return "Shape_Type:"+str(self.name)+" "+str(self.value)

    @classmethod
    def create_shape(cls,shape_type, params):
        if (shape_type == Shape_Types.RECTANGLE):
            return Rectangle(params[0],params[1])
        elif (shape_type == Shape_Types.SQUARE):
            return Rectangle.create_square(params[0])


builders = {
    Shape_Types.RECTANGLE : Rectangle.create_rectange,
    Shape_Types.SQUARE : Rectangle.create_square,
}

def build_shape(shape_type, params):
    ob = builders[shape_type](params)
    return ob

# shape = Shape(3, 5)
# shape = Rectangle(3, 5)
# shape.area = 12
# #shape.set_bb_width(33)
# print(shape.area)
# print(shape.bbox_width)
# shape.i = 3
# print(shape.i)
# print(shape._private_field)
# print(str(shape))
# shape2 = Rectangle.create_square(13)
# print(shape.area)
# print(shape2.height, shape2.height)
# shape2 = shape.create_square(13)

st= Shape_Types.RECTANGLE
if (st == Shape_Types.CIRCLE):
    print("circle")
else:
    print(" co innego")

print("Nazwa:", st.name, "\t Value", st.value)
print(st)
print(list(Shape_Types))

sh = Shape_Types.create_shape(Shape_Types.RECTANGLE, [2, 7])
print("Typ:", type(sh))

sh = build_shape(Shape_Types.SQUARE, 33)
print("Typ2:", type(sh))

sh.set_bb_width(37)