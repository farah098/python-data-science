class ColorCoded:
  def __init__(self):
    self.color_dict ={
        'Black': 0,
        'Brown': 1,
        'Red': 2,
        'Orange': 3,
        'Yellow': 4,
        'Green': 5,
        'Blue': 6,
        'Violet': 7,
        'Grey': 8,
        'White': 9,
    }

  def encoded(self,color):
    if len(color) < 2:
      raise ValueError("Required at least two color bands")

    first = self.color_dict[color[0].lower()]
    second = self.color_dict[color[1].lower()]

    return first * 10 + second
    
resistor = ColorCoded()

print(resistor.encoded(['brown', 'green']))

