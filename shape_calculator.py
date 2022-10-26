class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (self.width*2 + self.height*2)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if (self.width < 50 and self.height < 50):
      picture = ""
      for x in range(self.height):
        for y in range(self.width):
          picture += "*"
        picture += "\n"
    else:
      picture = "Too big for picture."
    return picture

  def get_amount_inside(self, shape):
    if (shape.width > self.width or shape.height > self.height):
      return 0
    else:
      return int((self.height / shape.height) * (self.width / shape.width))

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self,side):
    super().__init__(self, side)
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side
    