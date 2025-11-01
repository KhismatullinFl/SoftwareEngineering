# Тема 8. Введение в ООП.
Отчет по Теме #8 выполнил(а):
- Хисматуллин Андрей Дмитриевич
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |


знак '+' - задание выполнено; знак '-' - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
my_car = Car("Toyota", "Corolla")
```

### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/l1.png)

## Выводы
Код создает объект класса Car

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.drive()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/l2.png)

## Выводы
Код создает объект класса Car с атрибутами и методом Drive

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Михаил А. Панов Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
from lab2 import Car

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")
        
my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/l3.png)

## Выводы
Код создает объект класса ElectricCar, который наследует класс Car

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self._make = make 
        self.__model = model 

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")
my_car = Car ("Toyota", "Corolla")
print(my_car._make)
my_car.drive()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/l4.png)

## Выводы
Код создает объект класса Car с защищенным атрибутом _make и приватным атрибутом __model

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width* self.height

class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
r1 = Rectangle(4,5)
print(r1.area())
c1 = Circle(5)
print(c1.area())
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/l5.png)

## Выводы
Код создает объектs классов Rectangle и Circle, которые наследуют класс Shape 

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Animal:
    def __init__(self, family, name):
        self.family = family
        self.name = name
animal1 = Animal("Feline", "Cat")
print(animal1.family, animal1.name)
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/s1.png)

## Выводы
Код создает объект класса Animal

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Animal:
    def __init__(self, family, name):
        self.family = family
        self.name = name
    def text(self):
        print(f"{self.name} belong to the {self.family} family")
animal1 = Animal("Feline", "Cat")
animal1.text()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/s2.png)

## Выводы
Код создает объект класса Animal с атрибутами и методом text

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Animal:
    def __init__(self, family, name):
        self.family = family
        self.name = name
    def text(self):
        print(f"{self.name} belong to the {self.family} family")

class ColorAnimal(Animal):
    def __init__(self, family, name, color):
        super().__init__(family, name)
        self.color = color

    def text2(self):
        print(f" This {self.name} of the {self.family} family is {self.color} in color")
        
animal1 = ColorAnimal("Feline", "Cat", "Black")
animal1.text()
animal1.text2()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/s3.png)

## Выводы
Код создает объект класса ColorAnimal, который наследует класс Animal

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Animal:
    def __init__(self, family, name):
        self._family = family
        self.__name = name
    def text(self):
        print(f"{self.__name} belong to the {self._family} family")
animal1 = Animal("Feline", "Cat")
print(animal1._family)
animal1.text()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/s4.png)

## Выводы
Код создает объект класса Animal с защищенным атрибутом _family и приватным атрибутом __name

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Animal:
    def __init__(self, family, name):
        self.family = family
        self.name = name
    def text(self):
        print(f"{self.name} belong to the {self.family} family")

class ColorAnimal(Animal):
    def __init__(self, family, name, color):
        super().__init__(family, name)
        self.color = color

    def text2(self):
        print(f" This {self.name} of the {self.family} family is {self.color} in color")
        
class NicknameAnimal(Animal):
    def __init__(self, family, name, nickname):
        super().__init__(family, name)
        self.nickname = nickname

    def text2(self):
        print(f" This {self.name} of the {self.family} family has the nickname {self.nickname}")
       
animal1 = ColorAnimal("Feline", "Cat", "Black")
animal1.text()
animal1.text2()
animal2 = NicknameAnimal("Feline", "Cat", "Ryzhyk")
animal2.text()
animal2.text2()
```
### Результат.
![Меню](https://github.com/KhismatullinFl/SoftwareEngineering/blob/tema_8/images/s5.png)

## Выводы
Код создает объектs классов ColorAnimal и NicknameAnimal, которые наследуют класс Animal 

## Общие выводы по теме
В ходе лабораторной работы по теме "Введение в ООП" я освоил базовые концепции объектно‑ориентированного программирования: создание классов и объектов, определение атрибутов и методов, использование конструктора __init__ и ключевого слова self. На практике применял принципы инкапсуляции для скрытия состояния объекта, реализовывал наследование для переиспользования кода и знакомился с полиморфизмом. Полученные навыки позволят мне уверенно применять концепции ООП в последующих задачах.