'''
# Небольшая задачка на ООП. Если все сделано, то можно за нее взяться. На звонке в пятницу на ее примере поговорм про ООП.
# Надо написать классы для треугольника и прямоугольника.
# - Для создания треугольника передаются три стороны,
# для прямоугольника две стороны.
# Также еще передается цвет фигуры.
# - У этих классов должен быть метод который выводит информацию о фигуре,
# что это за фигура и какие у нее параметры и цвет.
# И еще надо реализовать метод покраски - который принимает на вход цвет
# и меняет цвет фигуры на новый.
# Если цвет такой же, то выводится сообщение, что фигура уже такого же цвета.
# - Также у этих классов должны быть методы расчета периметра и площади.
'''
class Figure:
    def __init__(self, color):
        self.color = color

    def color_change(self, new_color):
        if new_color == self.color:
            print('Фигура уже такого цвета')
        else:
            self.color = new_color
    

class Triangle (Figure):
    def __init__(self, a, b, c, color):
        self.a = abs(a)
        self.b = abs(b)
        self.c = abs(c)
        if (self.a + self.b) > self.c and (self.b + self.c) > self.a and (self.c + self.a) > self.b:
            self.p = self.a + self.b + self.c
        else:
            raise ValueError('Невозможный треугольник, введите занчения сторон')
        self.color = color
        

    def __repr__(self):
        return f'Треугольник (a = {self.a}, b = {self.b}, c = {self.c}, color = {self.color})'

    def info(self):
        print (f'Объект: треугольник со сторонами {self.a, self.b, self.c}. Цвет: {self.color}')

    
    def perimeter(self):
        return f'Периметр = {self.p}'

    def area(self):
        hp = self.p/2
        s = (hp*(hp-self.a)*(hp-self.b)*(hp-self.c))**0.5
        return f'Площадь = {s}'
    
class Rectangle (Figure):
    def __init__(self, a, b, color):
        self.a = abs(a)
        self.b = abs(b)
        if self.a and self.b != 0:
            self.p = (self.a + self.b)*2
        else:
            raise ValueError('Невозможный прямоугольник, введите занчения сторон')
        self.color = color

    def __repr__(self):
        return f'Прямоугольник (a = {self.a}, b = {self.b}, c = {self.c}, color = {self.color})'

    def info(self):
        print (f'Объект: прямоугольник со сторонами {self.a, self.b}. Цвет: {self.color}')

    def perimeter(self):
        return f'Периметр = {self.p}'
    
    def area(self):
        return f'Площадь = {self.a*self.b}'



a = Triangle(3, 4, 5, 'red')
a.info()
a.color_change('green')
a.color_change('green')
a.info()
print(a.perimeter())
print(a.area())


b = Rectangle(10, 20, 'black')
b.info()
b.color_change('green')
b.info()
print(b.perimeter())
print(b.area())