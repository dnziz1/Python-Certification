import math

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def set_width(self, new_width: int) -> None:
        self._width = new_width

    def set_height(self, new_height: int) -> None:
        self._height = new_height

    def get_area(self) -> int:
        return self._width * self._height

    def get_perimeter(self) -> int:
        return 2 * (self._width + self._height)

    def get_diagonal(self) -> float:
        return math.sqrt((self._width ** 2) + (self._height ** 2))
    
    def get_picture(self) -> str:
        if self._width > 50 or self._height > 50:
            return 'Too big for picture.'
        
        result = ''
        for i in range(self._height):
            for j in range(self._width):
                result += '*'
            result += '\n'
        return result

    def get_amount_inside(self, shape):
        horizontal = self._width // shape._width
        vertical = self._height // shape._height
        return horizontal * vertical

    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'

class Square(Rectangle):
    def __init__(self, side_length: int) -> None:
        super().__init__(side_length, side_length)

    def set_width(self, new_width: int) -> None:
        self._width = new_width
        self._height = new_width

    def set_height(self, new_height: int) -> None:
        self._height = new_height
        self._width = new_height

    def set_side(self, side_length: int) -> None:
        self._width = side_length
        self._height = side_length

    def __str__(self):
        return f'Square(side={self._width})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
