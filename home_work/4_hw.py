# Задача 1
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def sqaure(self):
        return self.width * self.height
    def perimetr(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle(3, 8)
rect2 = Rectangle(11, 5)
rect3 = Rectangle(9, 9)

print(f'Площадь Rectangle1 = {rect1.sqaure()}, Периметр Rectangle1 = {rect1.perimetr()}  ')
print(f'Площадь Rectangle2 = {rect2.sqaure()}, Периметр Rectangle2 = {rect2.perimetr()}  ')
print(f'Площадь Rectangle3 = {rect3.sqaure()}, Периметр Rectangle3 = {rect3.perimetr()}  ')



# Задача 1
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f'Сложение {self.a} + {self.b} = {result}')

    def multiplication(self):
        result = self.a * self.b
        print(f'Умножение {self.a} * {self.b} = {result}')

    def division(self):
        result = self.a / self.b
        print(f'Деление {self.a} / {self.b} = {result}')

    def subtraction(self):
        result = self.a - self.b
        print(f'Вычитание {self.a} - {self.b} = {result}')

calc = Math(15, 16)
calc.addition()
calc.multiplication()
calc.division()
calc.subtraction()


# Задача 3
class Buttons:
    def __init__(self, text, type, loc=None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return('Клик по кнопке - {}'.format(self.text))

text_box = Buttons('Text Box','Кнопка', Buttons.click)
check_box = Buttons('Check Box', Buttons.click)
radio_button = Buttons('Radio Button', Buttons.click)
web_tables = Buttons('Web Tables', Buttons.click)
buttons = Buttons('Buttons', Buttons.click)
links = Buttons('Links', Buttons.click)
broken_links_images = Buttons('Broken Links - Images', Buttons.click)
upload_and_download = Buttons('Upload and Download', Buttons.click)
dynamic_properties = Buttons('Dynamic Properties', Buttons.click)

print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links_images.click())
print(upload_and_download.click())
print(dynamic_properties.click())



